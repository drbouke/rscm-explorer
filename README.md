# RSCM Explorer

An interactive explorer of post-quantum cryptographic sovereignty across countries. It
decomposes sovereignty into three distinct constructs, indigenous cryptographic capacity (ICC),
indigenous post-quantum control, and external dependency (ED), and certifies a country as a
post-quantum maker only through a strict gate of demonstrated, institutionally sustained
capability. Companion to the RSCM paper ([arXiv:2609.18477](https://arxiv.org/abs/2609.18477)).

Live: https://drbouke.github.io/rscm-explorer/

The published page is a single self-contained `index.html` (Bootstrap, D3, TopoJSON, the world
atlas and the dataset inlined), so it runs offline and on any static host with no external requests.
It opens on an animated world view: countries colored by class, readiness, creation or dependency;
makers pulse at a rate set by their creation score; countries whose post-quantum layer is
foreign-supplied receive an inbound flow from the NIST standardization hub; a spotlight cycles through
the sample with each country's scores and key evidence.

## Repository layout

```
index.html            Built, self-contained page (served by GitHub Pages)
src/
  template.html       HTML + CSS + JavaScript source
  data.json           Country dataset (scores, classes, per-cell evidence and citations)
  build.py            Inlines vendor/ and data.json into index.html
  vendor/             Pinned Bootstrap 5.3.3, D3 7.9.0, topojson-client 3.1.0, world-atlas 2.0.2 (countries-110m.json)
.github/ISSUE_TEMPLATE Dataset-update issue form
releases/<date>/      Frozen dataset snapshots (data.json, gate_reliability.md)
```

## Build

```
python src/build.py
```

This inlines the vendored libraries, the world atlas, and `src/data.json` into
`src/template.html` and writes `index.html` at the repository root. There is
no toolchain to install; any Python 3 works.

## Data

`src/data.json` holds one record per country with the readiness, capacity, creation, and
dependency scores, the class and maker type, uncertainty intervals and retention, and the per-cell
levels with their evidence grade, justification, and source URL for the post-quantum control (B1 to
B5) and external-dependency cells. Scores are ordinal levels 0 to 4 coded from cited public
evidence; the maker gate requires level 3 on at least one creation layer (design, implementation,
or validation) on a sustained institutional basis. The exact field format is documented in the
Explorer's *Data & extend* tab under *Format guide*.

## Releases

The dataset is published as dated snapshots every six months, each with a blind second coding of
the maker-gate cells and a frozen copy under `releases/<date>/`. See `RELEASES.md` and
`CHANGELOG.md`.

## Extending the dataset

The Explorer lets anyone download the dataset or a template, add or update countries with their
coded levels and sources, and upload the file to preview how the rules score it, entirely in the
browser (nothing is uploaded). To propose a change for the published dataset, open a
[dataset-update issue](https://github.com/drbouke/rscm-explorer/issues/new/choose) with the filled
template and its sources. Every proposed level must carry a public, citable source; the review
protocol and contributor credit are described in `CONTRIBUTING.md`.

## Citation

If you use these scores, please cite the RSCM paper:

M. A. Bouke, "A Global Readiness and Sovereignty Capability Model for Post-Quantum Cryptography
Migration," arXiv:2609.18477, 2026. https://doi.org/10.48550/arXiv.2609.18477

```bibtex
@misc{bouke2026globalreadinesssovereigntycapability,
  title={A Global Readiness and Sovereignty Capability Model for Post-Quantum Cryptography Migration},
  author={Mohamed Aly Bouke},
  year={2026},
  eprint={2609.18477},
  archivePrefix={arXiv},
  primaryClass={cs.CR},
  url={https://arxiv.org/abs/2609.18477}
}
```

## License

Code is released under the MIT License (see `LICENSE`). The assessment dataset accompanies the RSCM
paper and is provided for research and educational use.
