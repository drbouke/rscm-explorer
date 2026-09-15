# RSCM Explorer

An interactive explorer of post-quantum cryptographic sovereignty across 57 countries. It
decomposes sovereignty into three distinct constructs, indigenous cryptographic capacity (ICC),
indigenous post-quantum control, and external dependency (ED), and certifies a country as a
post-quantum maker only through a strict gate of demonstrated, institutionally sustained
capability. Companion to the RSCM paper.

Live: https://drbouke.github.io/rscm-explorer/

The published page is a single self-contained `index.html` (Bootstrap and the dataset inlined),
so it runs offline and on any static host with no external requests.

## Repository layout

```
index.html            Built, self-contained page (served by GitHub Pages)
src/
  template.html       HTML + CSS + JavaScript source
  data.json           Country dataset (scores, classes, per-cell evidence and citations)
  build.py            Inlines vendor/ and data.json into index.html
  vendor/             Pinned Bootstrap 5.3.3 (bootstrap.min.css, bootstrap.bundle.min.js)
.github/ISSUE_TEMPLATE Dataset-update issue form
```

## Build

```
python src/build.py
```

This inlines `src/vendor/bootstrap.min.css`, `src/vendor/bootstrap.bundle.min.js`, and
`src/data.json` into `src/template.html` and writes `index.html` at the repository root. There is
no toolchain to install; any Python 3 works.

## Data

`src/data.json` holds one record per country with the readiness, capacity, creation, and
dependency scores, the class and maker type, uncertainty intervals and retention, and the per-cell
levels with their evidence grade, justification, and source URL for the post-quantum control (B1 to
B5) and external-dependency cells. Scores are ordinal levels 0 to 4 coded from cited public
evidence; the maker gate requires level 3 on at least one creation layer (design, implementation,
or validation) on a sustained institutional basis. The exact field format is documented in the
Explorer's *Data & extend* tab under *Format guide*.

## Extending the dataset

The Explorer lets anyone download the dataset or a template, add or update countries with their
coded levels and sources, and upload the file to preview how the rules score it, entirely in the
browser (nothing is uploaded). To propose a change for the published dataset, open a
[dataset-update issue](https://github.com/drbouke/rscm-explorer/issues/new/choose) with the filled
template and its sources. Every proposed level must carry a public, citable source.

## Citation

If you use these scores, please cite the RSCM paper (see the paper for the full reference).

## License

Code is released under the MIT License (see `LICENSE`). The assessment dataset accompanies the RSCM
paper and is provided for research and educational use.
