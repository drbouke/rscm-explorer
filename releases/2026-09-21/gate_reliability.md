# Gate-cell reliability, snapshot 2026-09-21

Computed 2026-09-21 from `CODING_SHEET_GATE_CODED.csv`.

| Cells | n | Exact | Within one | Weighted kappa |
|---|---|---|---|---|
| B1-B3 (all gate cells) | 171 | 75% | 99% | 0.91 |
| B1 primitive | 57 | 82% | 100% | 0.95 |
| B2 implementation | 57 | 79% | 98% | 0.92 |
| B3 validation | 57 | 65% | 100% | 0.86 |

Maker verdict agreement: 56/57 countries.

Countries whose verdict differs between coders (snapshot verdict, second coder):

- Vietnam: maker, non-maker

## Protocol

The second coder was a language-model-based coder working blind: it received only the blind codebook
(no gate rule, no classification) and the sheet with each cell's recorded source URL, and was instructed
to fetch the source, search independently, apply the announced-versus-operational and missing-evidence
rules, and never consult the Explorer or the paper. It did not see the snapshot's levels. Because the
coder saw the same source pointers as the snapshot, these figures measure how reproducibly the codebook
maps a given artifact to a level, not how reproducibly a coder would find the artifact; the earlier
second coding reported in the model paper, with weaker source pointers, reached a gate-cell kappa of
0.71 and a verdict agreement of 14 of 20. The completed sheet is `CODING_SHEET_GATE_CODED.csv`.
