#!/usr/bin/env python3
"""Reproducible internal checks for two *aggregate* historical-extract CSVs.

No data harvest; does NOT validate source-level membership or produce project-level Gini.
"""
from __future__ import annotations
import csv
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

def rows(path):
    with (BASE / path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))

summary_list = rows("data/Table1_initial_cohort_metrics.csv")
region_list = rows("data/Table2_region_summary.csv")
summary = {r["season"]: r for r in summary_list}
assert len(summary_list) == len(summary) == 2
assert set(summary) == {"2024-II", "2025-I"}
assert len(region_list) == 28
seen = set()
for record in region_list:
    key = (record["season"], record["region"])
    assert key not in seen, f"Duplicate season-region: {key}"
    seen.add(key)

expected_counts = {"2024-II": (1772, 1538), "2025-I": (2369, 1972)}
for season, (expected_projects, expected_mfys) in expected_counts.items():
    s = summary[season]
    project_total = int(s["projects"])
    mfy_total = int(s["unique_winning_mfys"])
    assert (project_total, mfy_total) == (expected_projects, expected_mfys)
    assert int(s["total_votes"]) > 0
    assert int(s["total_funding_uzs"]) > 0
    gini = float(s["funding_gini_project"])
    assert 0 <= gini <= 1
    group = [r for r in region_list if r["season"] == season]
    assert len(group) == 14
    assert all(int(r["project_rows"]) >= 0 for r in group)
    assert sum(int(r["project_rows"]) for r in group) == project_total
    assert math.isclose(sum(float(r["share"]) for r in group), 1., abs_tol=1e-12)
    for r in group:
        assert math.isclose(float(r["share"]), int(r["project_rows"]) / project_total, abs_tol=1e-12)
    calculated_hhi = 10000 * sum((int(r["project_rows"]) / project_total) ** 2 for r in group)
    assert math.isclose(calculated_hhi, float(s["project_hhi_region"]), abs_tol=1e-8)
    print(f"PASS {season}: projects={project_total}; MFYs={mfy_total}; 14 regions; project HHI={calculated_hhi:.3f}")

# Set arithmetic below checks *reported constants*, not original project-to-MFY mappings.
A, B, AB = 1538, 1972, 767
union = A + B - AB
assert union == 2743 and B - AB == 1205 and A - AB == 771
assert round(AB / union, 4) == 0.2796
print(f"PASS reported set arithmetic: overlap={AB}; union={union}; Jaccard={AB/union:.6f}")
print("LIMITATION: project-level membership, funding Gini, and administrative rosters are NOT independently reproduced.")
