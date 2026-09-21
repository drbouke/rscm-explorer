# Release policy

The RSCM dataset is a living assessment. National post-quantum programs move quickly, so the
published scores are issued as dated snapshots on a fixed cadence rather than edited ad hoc.

## Cadence

- A dated snapshot is published every six months, in March and September.
- Each snapshot is identified by its date (for example `2026-09-21`) and by the Explorer version
  that first carried it. The Explorer always shows the snapshot date as "Dataset last updated".
- Between snapshots, corrections of clear errors may be published immediately and are listed in
  `CHANGELOG.md`; scheduled re-assessment waits for the next snapshot.

## What every snapshot contains

1. An update scan of every country in the sample over the period since the previous snapshot,
   restricted to public, citable artifacts. Every changed cell records its new justification and
   source in the country record.
2. A blind second coding of the maker-gate cells (B1 indigenous PQC primitive, B2 PQC
   implementation control, B3 PQC validation and evaluation) for every country, by a coder who
   has not seen the snapshot's own levels. The maker verdict rests only on these cells, so this is
   the reliability measurement that matters for the headline result. The agreement statistics and
   the list of countries whose verdict differs between coders are published with the snapshot as
   `releases/<date>/gate_reliability.md`.
3. The frozen dataset, `releases/<date>/data.json`, identical to the `src/data.json` that built
   the Explorer at that date, so any published figure can be reproduced from its snapshot.
4. A `CHANGELOG.md` entry listing every level change with its artifact, the evidence-only
   updates, and the resulting class counts.

## Citing a snapshot

Cite the RSCM paper for the model and the snapshot date for the numbers, for example
"RSCM dataset, snapshot 2026-09-21, https://github.com/drbouke/rscm-explorer/tree/main/releases/2026-09-21".

## Proposing changes between snapshots

See `CONTRIBUTING.md`. Accepted proposals are queued for the next snapshot unless they correct a
clear error.
