# Data dictionary

**Unit for `Table1_initial_cohort_metrics.csv`:** one row per included season (2024-II; 2025-I).

| Field | Definition |
|---|---|
| `season` | Study extract's season label. |
| `projects` | Number of project records included in the extract (not guaranteed individually historical-source-certified). |
| `unique_winning_mfys` | Count of distinct nonmissing MFY identifiers linked to extract project rows. |
| `total_votes` | Sum of vote counts associated with included winning project rows, **not** total ballots cast nationally. |
| `total_funding_uzs` | Sum of recorded allocation/grant amounts, in nominal UZS, **not** audited disbursement/expenditure. |
| `project_hhi_region` | 10,000 × sum of squared shares of project counts across regions. |
| `funding_gini_project` | Gini of allocated values across project records, **not** need-adjusted geographical inequality. Cannot be recalculated from this aggregate table alone. |

**Unit for `Table2_region_summary.csv`:** one season-region combination. There are 14 observed region labels per season.

| Field | Definition |
|---|---|
| `season` | Project extract's season label. |
| `region` | Region name as reported in source/export (Cyrillic). |
| `project_rows` | Number of included project records in that region and season. |
| `share` | `project_rows` / season total project records. |

No normalization by population, eligible MFYs, total applications, local fiscal need, or all-cast votes is performed. The data do not support a causal effect of the 2025 pause/cooldown policy.
