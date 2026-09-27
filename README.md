# latin-edit-script-review

Browse the predicted token-level edit scripts of the Loci Similes pairs: for every pair of a source passage and a
later text that reuses it, which reuse word comes from which source word, and by which operation (COPY, INFLECT,
SUBST, SPLIT, MERGE; FRAME, INS and DEL for words without a link).

Live: <https://julianschelb.github.io/latin-edit-script-review/>

A static page (Vite, React, Tailwind, as `loci-similes-demo-page`), deployed to GitHub Pages on every push to `main`.

## What it shows

- **The pair list** (left): all 1,490 pairs, with search, filters (reference type, source and reuse author and work,
  pairs with a predicted SUBST or INFLECT), sorting and pages.
- **The pair** (right): the two passages' citations, authors, works and lengths, the annotator's note; the mapping
  from source to reuse words as arrows, horizontal or vertical, with a legend of every label; the Latin texts with
  their English translations; the predicted links with their probabilities.

The selected pair is in the URL (`#p0006`), so a link opens the same pair.

## Layout

| Path | What it holds |
| --- | --- |
| `index.html`, `src/` | the app: `src/App.jsx`, `src/components/`, `src/data.js` (loads the input), `src/filters.js`, `src/labels.js` |
| `public/data/` | the input, `gold_2026-09-24.populated.records.jsonl`: one pair per line in the paper's storage format |
| `corrections/` | for corrections files sent back later |
| `.github/workflows/` | build and deploy to GitHub Pages |

## Run locally

```bash
npm install
npm run dev        # http://localhost:5173/latin-edit-script-review/
```

## Data

`public/data/gold_2026-09-24.populated.records.jsonl` is copied from the paper repository
(`notebooks/80_Edit_Script_Generation/data/gold_full/`, written by `tools/populate_gold.py`): the frozen gold labels
with every storage-format field filled, and the predictions of the stretch-and-link pointer with the COPY gate, each
pair from the fold in which it was test data. The page shows the predictions only.
