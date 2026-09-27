// The app's input: the annotation file, one pair per line in the paper's storage format
// (gold links, lookups, ours' prediction), served from public/data/.
export const DATA_FILE = "gold_2026-09-24.populated.records.jsonl";

export async function loadRecords(file = DATA_FILE) {
  const response = await fetch(`${import.meta.env.BASE_URL}data/${file}`);
  if (!response.ok) throw new Error(`${file}: HTTP ${response.status}`);
  const text = await response.text();
  return text.split("\n").filter((line) => line.trim()).map((line) => JSON.parse(line));
}
