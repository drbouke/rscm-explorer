"""Build the single-file RSCM Explorer.

Inlines the Bootstrap stylesheet and script and the country dataset into the HTML
template, producing a self-contained index.html at the repository root that runs
offline and on any static host with no external requests.

Usage: python src/build.py
"""
import json
import os

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)

tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
css = open(os.path.join(HERE, "vendor", "bootstrap.min.css"), encoding="utf-8").read()
js = open(os.path.join(HERE, "vendor", "bootstrap.bundle.min.js"), encoding="utf-8").read()
data = open(os.path.join(HERE, "data.json"), encoding="utf-8").read()

# reserialize the dataset compactly and confirm it is valid JSON
data = json.dumps(json.loads(data), ensure_ascii=False, separators=(",", ":"))

html = (tpl
        .replace("__BS_CSS__", css)
        .replace("__BS_JS__", js)
        .replace("__DATA__", data))

for marker in ("__BS_CSS__", "__BS_JS__", "__DATA__"):
    assert marker not in html, f"placeholder {marker} was not replaced"

dst = os.path.join(ROOT, "index.html")
open(dst, "w", encoding="utf-8").write(html)
print("wrote", os.path.abspath(dst), "|", len(html), "bytes")
