"""Генерація UML Use Case діаграми DemandLens у форматі StarUML (.mdj) і експорт PNG через StarUML CLI.

Використання: python tools/gen_usecase_mdj.py
Результат: docs/uml/use-case-diagram.mdj, docs/uml/use-case-diagram.png
Ідентифікатори прецедентів відповідають DECISIONS.md (4.4).
"""
from __future__ import annotations

import itertools
import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "uml"
STARUML = r"C:\Program Files\StarUML\StarUML.exe"
_ids = itertools.count(1)


def nid() -> str:
    return f"DL{next(_ids):08d}"


def ref(x: str) -> dict:
    return {"$ref": x}


# --- Модель -------------------------------------------------------------
ACTORS = {  # key: (name, left, top, primary)
    "analyst": ("Аналітик", 60, 400, True),
    "admin": ("Адміністратор", 60, 700, True),
    "hn": ("HN Search API", 1520, 140, False),
    "se": ("Stack Exchange API", 1520, 300, False),
    "gh": ("GitHub REST API", 1520, 460, False),
    "wm": ("Wikimedia Analytics API", 1520, 620, False),
}
UCS = {  # key: (name, left, top)
    "uc01": ("UC-01 Автентифікуватися в системі", 300, 60),
    "uc02": ("UC-02 Створити дослідницький проєкт", 300, 150),
    "uc03": ("UC-03 Запустити збір даних", 300, 240),
    "uc04": ("UC-04 Запустити ранжування ніш", 300, 330),
    "uc05": ("UC-05 Переглянути пояснення рейтингу ніші", 300, 420),
    "uc06": ("UC-06 Порівняти конкурентів ніші", 300, 510),
    "uc07": ("UC-07 Експортувати звіт", 300, 600),
    "uc08": ("UC-08 Керувати джерелами даних", 300, 720),
    "uc09": ("UC-09 Переглянути журнал аудиту", 300, 810),
    "uc12": ("UC-12 Отримати публікації з джерела", 860, 190),
    "uc11": ("UC-11 Повторити збір після збою джерела", 860, 380),
    "uc10": ("UC-10 Перевірити токен доступу", 920, 620),
}
UC_W, UC_H = 290, 56
ACT_W, ACT_H = 40, 80
ASSOC = [("analyst", u) for u in ("uc01", "uc02", "uc03", "uc04", "uc05", "uc06", "uc07")] + [
    ("admin", "uc08"), ("admin", "uc09"),
    ("uc12", "hn"), ("uc12", "se"), ("uc12", "gh"), ("uc12", "wm"), ("uc06", "gh"),
]
INCLUDES = [("uc03", "uc12")] + [(u, "uc10") for u in ("uc02", "uc03", "uc04", "uc05", "uc06", "uc07", "uc08", "uc09")]
EXTENDS = [("uc11", "uc03")]
GENERALIZATIONS = [("admin", "analyst")]


def box(key: str) -> tuple[float, float, float, float]:
    if key in ACTORS:
        _, x, y, _ = ACTORS[key]
        return x, y, ACT_W, ACT_H
    name, x, y = UCS[key]
    return x, y, uc_width(name), UC_H


def uc_width(name: str) -> int:
    """Ширина еліпса, близька до автоматичної ширини StarUML для напівжирного Arial 13."""
    return int(len(name) * 12 + 75)


def border_point(key: str, tx: float, ty: float) -> tuple[int, int]:
    x, y, w, h = box(key)
    cx, cy = x + w / 2, y + h / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return int(cx), int(cy)
    if key in UCS:  # еліпс
        t = 1 / math.sqrt((dx / (w / 2)) ** 2 + (dy / (h / 2)) ** 2)
    else:  # прямокутник актора
        t = min(abs((w / 2 + 6) / dx) if dx else math.inf, abs((h / 2) / dy) if dy else math.inf)
    return int(cx + dx * t), int(cy + dy * t)


def points(a: str, b: str) -> str:
    ax, ay, aw, ah = box(a)
    bx, by, bw, bh = box(b)
    p1 = border_point(a, bx + bw / 2, by + bh / 2)
    p2 = border_point(b, ax + aw / 2, ay + ah / 2)
    return f"{p1[0]}:{p1[1]};{p2[0]}:{p2[1]}"


def build() -> dict:
    proj_id, model_id, diag_id, subj_id = nid(), nid(), nid(), nid()
    el: dict[str, dict] = {}
    model_elements = []
    for k, (name, *_rest) in ACTORS.items():
        el[k] = {"_type": "UMLActor", "_id": nid(), "_parent": ref(model_id), "name": name, "ownedElements": []}
    for k, (name, *_rest) in UCS.items():
        el[k] = {"_type": "UMLUseCase", "_id": nid(), "_parent": ref(model_id), "name": name, "ownedElements": []}
    rels = []
    for a, b in ASSOC:
        rid = nid()
        rel = {"_type": "UMLAssociation", "_id": rid, "_parent": ref(el[a]["_id"]),
               "end1": {"_type": "UMLAssociationEnd", "_id": nid(), "_parent": ref(rid), "reference": ref(el[a]["_id"])},
               "end2": {"_type": "UMLAssociationEnd", "_id": nid(), "_parent": ref(rid), "reference": ref(el[b]["_id"]),
                        "navigable": "navigable"}}
        el[a]["ownedElements"].append(rel)
        rels.append(("UMLAssociationView", rid, a, b))
    for kind, pairs, view in (("UMLInclude", INCLUDES, "UMLIncludeView"), ("UMLExtend", EXTENDS, "UMLExtendView"),
                              ("UMLGeneralization", GENERALIZATIONS, "UMLGeneralizationView")):
        for a, b in pairs:
            rid = nid()
            el[a]["ownedElements"].append({"_type": kind, "_id": rid, "_parent": ref(el[a]["_id"]),
                                           "source": ref(el[a]["_id"]), "target": ref(el[b]["_id"])})
            rels.append((view, rid, a, b))

    views, vid = [], {}
    views.append({"_type": "UMLUseCaseSubjectView", "_id": nid(), "_parent": ref(diag_id), "model": ref(subj_id),
                  "left": 260, "top": 15, "width": 1180, "height": 880})
    for k in ACTORS:
        x, y, w, h = box(k)
        vid[k] = nid()
        views.append({"_type": "UMLActorView", "_id": vid[k], "_parent": ref(diag_id), "model": ref(el[k]["_id"]),
                      "left": x, "top": y, "width": w, "height": h,
                      "suppressAttributes": True, "suppressOperations": True})
    for k in UCS:
        x, y, w, h = box(k)
        vid[k] = nid()
        views.append({"_type": "UMLUseCaseView", "_id": vid[k], "_parent": ref(diag_id), "model": ref(el[k]["_id"]),
                      "left": x, "top": y, "width": w, "height": h,
                      "suppressAttributes": True, "suppressOperations": True})
    for view, rid, a, b in rels:
        views.append({"_type": view, "_id": nid(), "_parent": ref(diag_id), "model": ref(rid),
                      "tail": ref(vid[a]), "head": ref(vid[b]), "lineStyle": 1, "points": points(a, b)})

    model_elements.append({"_type": "UMLUseCaseDiagram", "_id": diag_id, "_parent": ref(model_id),
                           "name": "DemandLens — Use Case Diagram", "defaultDiagram": True, "ownedViews": views})
    model_elements.append({"_type": "UMLUseCaseSubject", "_id": subj_id, "_parent": ref(model_id),
                           "name": "DemandLens (система)"})
    model_elements += list(el.values())
    return {"_type": "Project", "_id": proj_id, "name": "DemandLens",
            "ownedElements": [{"_type": "UMLModel", "_id": model_id, "_parent": ref(proj_id),
                               "name": "Use Case Model", "ownedElements": model_elements}]}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    mdj = OUT / "use-case-diagram.mdj"
    mdj.write_text(json.dumps(build(), ensure_ascii=False, indent=1), encoding="utf-8")
    png = OUT / "use-case-diagram.png"
    subprocess.run([STARUML, "image", str(mdj), "-f", "png", "-o", str(png)], check=True, timeout=180)
    from PIL import Image
    im = Image.open(png).convert("RGBA")
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    Image.alpha_composite(bg, im).convert("RGB").save(png)
    print(f"OK {mdj.relative_to(ROOT)} {png.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
