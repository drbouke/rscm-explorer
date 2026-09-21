# Contributing to the RSCM dataset

Contributions are welcome from researchers, national agencies, and practitioners, in particular
from countries where public evidence is thin or published only in languages the maintainer does
not read. The unit of contribution is a coded cell with its evidence, not an opinion about a
country's standing.

## What a contribution must contain

For every cell you propose to add or change:

- the country and the cell (R1 to R5, A1 to A5, B1 to B5, or ED);
- the proposed level (0 to 4) chosen against the codebook anchor for that cell (the anchors are
  in the Explorer's *About* tab and in the paper);
- a public, citable source (a URL to an official document, standards body page, published
  algorithm or library, peer-reviewed paper, or a reputable press report) that a reader can open;
- one sentence stating what the source shows and why it meets the anchor;
- an evidence grade, High (primary official artifact), Medium (secondary or partial), or Low
  (thin or inferred).

Announced or planned capability is coded below the operational level. Absence of public evidence
is coded as the lower level and graded Low; it is not evidence that a capability is absent.
Quantum key distribution is never coded as post-quantum cryptography. Algorithm authorship is
credited to the designers' country, not to the body that standardized the scheme.

## How to submit

1. In the Explorer's *Data & extend* tab, download the template, fill it, and upload it to check
   that the rules score it as you expect. Nothing leaves your browser at this step.
2. Open a [dataset update issue](https://github.com/drbouke/rscm-explorer/issues/new/choose)
   with the filled template and the sources, or email it to bouke@ieee.org.

## How contributions are reviewed

- The maintainer checks every source against the anchor. A proposal whose source cannot be
  opened or does not show what is claimed is returned with a note, not merged.
- Any proposal that touches a maker-gate cell (B1, B2, B3) is included in the blind second coding
  of the next snapshot before it is merged, because these cells decide the maker verdict.
- Accepted changes are merged at the next dated snapshot (see `RELEASES.md`), listed in
  `CHANGELOG.md` with the contributor's name or handle, and the contributor is added to the
  contributors list below. Corrections of clear errors are merged immediately.
- Editorial authority over the codebook and the final level stays with the maintainer, so that
  levels remain comparable across countries. Disagreements that cannot be resolved are recorded
  in the changelog with both readings.

## Proposing a new country

A country enters the sample when it has a documented national cryptographic footprint: a national
PKI or certificate authority, a national cryptographic or standards agency with published output,
documented cryptographic or quantum research, or participation in ISO/IEC JTC 1/SC 27. Propose all
sixteen cells with sources; partially coded countries are held until complete.

## Contributors

- Mohamed Aly Bouke (maintainer)
