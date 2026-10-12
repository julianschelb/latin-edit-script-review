"""Build a static copy of the review page that runs from a local folder.

    python scripts/static_build.py --records data/records.js --out ../static-review

The records file is `window.RECORDS = [...]` with the fields the page reads (id, fold, benchmark_id, pair_label,
source, reuse, pred.links, pred.frame_spans). The page is built with vite.static.config.js (relative paths, one
classic script), the records are copied next to it, and index.html loads them before the app.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--records", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    out = args.out.resolve()
    subprocess.run(["npx", "vite", "build", "--config", "vite.static.config.js", "--outDir", str(out), "--emptyOutDir"],
                   cwd=HERE, check=True)
    for f in (out / "data").glob("*.jsonl"):      # the served records file is not needed: the page inlines them
        f.unlink()
    (out / "data").mkdir(exist_ok=True)
    shutil.copyfile(args.records, out / "data" / "records.js")
    html = (out / "index.html").read_text(encoding="utf-8")
    # a classic script in <head> would run before #root exists; defer it as the module script was
    html = html.replace(" crossorigin", "").replace(' type="module"', " defer")
    html = re.sub(r"(\s*)(<script defer src=\"\./assets/)", r'\1<script src="./data/records.js"></script>\1\2', html, count=1)
    assert "records.js" in html, "no app script tag found in index.html"
    (out / "index.html").write_text(html, encoding="utf-8")
    print(f"static page written to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
