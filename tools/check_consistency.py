"""Інтеграційний аудит узгодженості специфікацій (ЛР№6, Завд.4).

Перевіряє:
1. ENUM-типи: DECISIONS.md (4.6) = docs/2_design.md (2.7.2) = docs/api/openapi.yaml (components.schemas).
2. Поля схем OpenAPI ↔ колонки таблиць ERD (Mermaid erDiagram у 2_design.md) за явною мапою;
   похідні поля (JOIN, обчислення) перелічено в DERIVED з поясненням.
3. Статуси, які алгоритми ALG-01…03 присвоюють полям `status`, належать відповідним ENUM.
4. Ідентифікатори SRS-FUN-NN і API-REQ-NN у openapi.yaml існують у srs.md / DECISIONS.md.
Код виходу 1 — є розбіжності.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
design = (ROOT / "docs/2_design.md").read_text(encoding="utf-8")
decisions = (ROOT / "DECISIONS.md").read_text(encoding="utf-8")
srs = (ROOT / "docs/srs.md").read_text(encoding="utf-8")
api = yaml.safe_load((ROOT / "docs/api/openapi.yaml").read_text(encoding="utf-8"))
schemas = api["components"]["schemas"]
problems: list[str] = []


def enum_table(text: str, start: str) -> dict[str, list[str]]:
    block = text[text.index(start):]
    out = {}
    for m in re.finditer(r"^\| `(\w+)` \| ([^|]+)\|", block, re.M):
        vals = re.findall(r"`([A-Z0-9_]+)`", m.group(2))
        if vals:
            out[m.group(1)] = vals
        if len(out) >= 11:
            break
    return out


dec_enums = enum_table(decisions, "### 4.6.")
erd_enums = enum_table(design, "### 2.7.2.")
api_map = {"user_role": "UserRole", "project_status": "ProjectStatus", "run_status": "RunStatus",
           "source_code": "SourceCode", "detection_method": "DetectionMethod", "niche_status": "NicheStatus",
           "uncertainty_level": "UncertaintyLevel", "criterion_code": "CriterionCode",
           "argument_kind": "ArgumentKind", "report_format": "ReportFormat",
           "competitor_metric": "CompetitorMetric"}
for name, vals in dec_enums.items():
    if erd_enums.get(name) != vals:
        problems.append(f"ENUM {name}: DECISIONS {vals} != ERD {erd_enums.get(name)}")
    api_vals = schemas.get(api_map[name], {}).get("enum")
    if api_vals != vals:
        problems.append(f"ENUM {name}: DECISIONS {vals} != OpenAPI {api_vals}")
print(f"[1] ENUM: перевірено {len(dec_enums)} типів")

# --- 2. Поля API ↔ колонки БД
tables: dict[str, set[str]] = {}
for block in re.findall(r"```mermaid\nerDiagram\n(.*?)```", design, re.S):
    for t, body in re.findall(r"^\s+(\w+) \{\n(.*?)^\s+\}", block, re.S | re.M):
        cols = {ln.split()[1] for ln in body.strip().split("\n") if len(ln.split()) >= 2}
        tables[t] = cols

MAP = {
    "Project": "research_projects", "CollectionRun": "collection_runs",
    "CollectionRunSource": "collection_run_sources", "Complaint": "complaints",
    "ScoringRun": "scoring_runs", "NicheSummary": "niches", "Competitor": "competitors",
    "CompetitorMetricValue": "competitor_metrics", "Report": "reports", "DataSource": "data_sources",
    "AuditEvent": "audit_events", "Evidence": "score_evidence", "ScoreComponent": "score_components",
    "Argument": "niche_arguments",
}
DERIVED = {
    "Project.keywords": "project_keywords.keyword (JOIN)",
    "Project.source_codes": "project_sources → data_sources.code (JOIN)",
    "CollectionRun.sources": "collection_run_sources (вкладений масив)",
    "CollectionRunSource.source_code": "data_sources.code через source_id",
    "Complaint.cluster_id": "cluster_memberships останнього COMPLETED clustering_run",
    "Complaint.source_code": "documents.source_id → data_sources.code",
    "Complaint.url": "documents.url", "Complaint.published_at": "documents.published_at",
    "ScoringRun.scoring_model_version": "scoring_models.version через scoring_model_id",
    "NicheSummary.rank": "niche_scores.rank", "NicheSummary.score": "niche_scores.score",
    "NicheSummary.confidence_interval": "niche_scores.ci_low, ci_high",
    "NicheSummary.uncertainty_level": "niche_scores.uncertainty_level",
    "NicheSummary.complaints_count": "niche_scores.complaints_count",
    "Competitor.metrics": "competitor_metrics (останні значення)",
    "Report.download_url": "підписаний URL за file_path, не зберігається",
    "Evidence.text": "complaints.text", "Evidence.url": "documents.url",
    "Evidence.source_code": "data_sources.code", "Evidence.pain_score": "complaints.pain_score",
    "ScoreComponent.weight": "scoring_model_weights.weight через scoring_run",
    "ScoreComponent.contribution": "v_score_contributions (обчислення)",
    "Argument.criterion": "niche_arguments.criterion",
}
checked = 0
for schema, table in MAP.items():
    props = schemas[schema].get("properties", {})
    for prop in props:
        checked += 1
        key = f"{schema}.{prop}"
        if prop in tables.get(table, set()) or key in DERIVED:
            continue
        if prop == "criterion" and "criterion" in tables.get(table, set()):
            continue
        problems.append(f"API {key}: немає колонки в {table} і не позначено як похідне")
print(f"[2] Поля API ↔ БД: перевірено {checked} полів у {len(MAP)} схемах, таблиць ERD: {len(tables)}")

# --- 3. Статуси в алгоритмах
alg = design[design.index("### 2.7.5."):]
run_vals = set(dec_enums["run_status"])
niche_vals = set(dec_enums["niche_status"]) | set(dec_enums["uncertainty_level"])
for m in re.finditer(r"(\w+)\.status := ([A-Z_]+)", alg):
    owner, val = m.group(1), m.group(2)
    allowed = niche_vals if owner.startswith("Niche") else run_vals
    if val not in allowed:
        problems.append(f"ALG: {owner}.status := {val} — значення відсутнє в ENUM")
used = set(re.findall(r"\.status := ([A-Z_]+)", alg))
print(f"[3] Алгоритми: присвоєні статуси {sorted(used)}")

# --- 4. Посилання на вимоги і маршрути
ops = [(p, mth, op) for p, item in api["paths"].items() for mth, op in item.items() if isinstance(op, dict) and "operationId" in op]
for p, mth, op in ops:
    for fid in re.findall(r"SRS-FUN-\d\d", op.get("summary", "")):
        if f'id="{fid.lower()}"' not in srs:
            problems.append(f"OpenAPI {mth.upper()} {p}: {fid} відсутній у srs.md")
    rid = op.get("x-route-id")
    if not rid or rid not in decisions:
        problems.append(f"OpenAPI {mth.upper()} {p}: route id {rid} відсутній у DECISIONS.md")
print(f"[4] Операцій OpenAPI: {len(ops)}")

print()
if problems:
    print(f"РОЗБІЖНОСТІ: {len(problems)}")
    for pr in problems:
        print(" -", pr)
    sys.exit(1)
print("Розбіжностей не виявлено")
