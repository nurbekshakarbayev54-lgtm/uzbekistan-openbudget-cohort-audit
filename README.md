# Uzbekistan OpenBudget: reconstructed winner-cohort descriptive audit

**Status (2026-11-03): pre-submission research companion; derived aggregates only.**

This repository contains two small *derived aggregate CSV tables* and a standard-library Python check for numerical internal consistency, associated with a draft study entitled *When Winner Lists Change: Cohort Reconstruction and Locality-Level Turnover in Uzbekistan’s Participatory Budgeting*.

## Scope

Two project-list-defined historical extracts were analyzed:

| Season | Project rows | Distinct mahalla (MFY) IDs | Project-linked votes | Recorded allocated amounts (UZS) |
|---|---:|---:|---:|---:|
| 2024-II | 1,772 | 1,538 | 6,567,681 | 2,108,655,762,183 |
| 2025-I | 2,369 | 1,972 | 7,934,739 | 2,911,424,578,419 |

The overlap of unique MFY IDs in the two *study extracts* is 767; set union 2,743; Jaccard similarity 0.279621. The extracts are **not completely certified as exact contemporaneous initial-winner rosters, record by record**. They are count-matched analytic extracts. Do not use them as the official baseline population or causal treatment groups.

## Contents

- `data/Table1_initial_cohort_metrics.csv`: project counts, unique MFYs, votes on included winning-project rows, recorded financing totals, regional project HHI and project-funding Gini.
- `data/Table2_region_summary.csv`: per-season regional project counts and shares (14 regions per season).
- `scripts/validate_summaries.py`: stand-alone numeric verification of *these exports*, including total/count/region-HHI consistency and set arithmetic.
- `docs/DATA_DICTIONARY.md`: variable descriptions and units.
- `docs/SOURCE_BOUNDARIES.md`: unresolved provenance/denominator conflicts.
- `docs/PUBLICATION_AND_LICENSE_REVIEW.md`: redistribution and review-anonymity checklist.
- `docs/ORIGINAL_SOURCE_LINKS.md`: third-party source pointers, not licensed mirrors.

## Run verification

Python 3.9+ is sufficient, without third-party dependencies:

```bash
python scripts/validate_summaries.py
```

**What this does not reproduce:** the original download/API harvest, project-level historical winner membership, source-archive timestamp, individual source-to-ID links, project-level funding Gini, district-level calculations or causal effects. Agreement of this verifier with the CSVs is not independent historical source validation.

## Official provenance versus derived results

Ministry/portal announcements have values that are distinct from our extracts. In 2025-I, the official 2,011-MFY figure differs from 1,972 extracted MFYs. The corrected 823-MFY administrative pause list differs from the 767-MFY extracted overlap. For 2025-II, a 2,332-project initial official announcement differs from a later observed 2,367-project portal snapshot. These are **different source boundaries**; differences cannot be assigned record-by-record without dated source registries. Details and official URLs: `docs/SOURCE_BOUNDARIES.md`.

## Data availability and redistribution

Only original **aggregated summaries produced for the analysis** are included here. The 2.3-MB 33-sheet research workbook, project-level records, publisher submission materials and private author-approval forms are **deliberately excluded**. Their historical membership and source redistribution rights remain unresolved. No blanket CC0/CC BY/ODbL license is claimed on third-party source records. Confirm any permissions and authors' approvals before making even this repository public.

For double-anonymous peer review, keep the repository **private**, or use an approved anonymized review mechanism if the journal asks for reviewer access. The repository URL and GitHub owner can disclose information about authors, preparers and revision history.

## Notes

The repository is an audit companion for descriptive research, not an official OpenBudget dataset and not a validated policy-impact evaluation. All interpretations in any publication must be limited to the populations and timepoints described above.
