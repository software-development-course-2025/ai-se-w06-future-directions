# AI Impact Map

## Purpose
Map each proposed AI direction to stakeholders, expected value, risks, and initial dependencies.

| Direction | Primary Stakeholders | Value (H/M/L) | Key Risks | Dependencies |
|-----------|----------------------|---------------|----------|--------------|
| Code-centric LLM agents | Developers, CI teams | H | Incorrect changes, security | Access to CI artifacts, safe sandbox |
| Automated test generation | QA, Developers | H | Flaky tests, false positives | Test frameworks, coverage data |
| Self-healing CI | DevOps, SRE | M | unintended rollbacks | Observability & safe rollback protocols |
| Requirements mining | Product, BA | M | misinterpreted specs | Rich historical docs, issue trackers |
| Productivity lenses | Developers, PMs | L | notification fatigue | Telemetry & IDE integrations |

## Visuals & recommended KPIs
- Time-to-fix reduction (%)  
- Test coverage increase (absolute %)  
- Mean time to detect/resolve (MTTD/MTTR)  
- Developer satisfaction (NPS-like survey)
