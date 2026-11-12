# Checking text-apz for tipitaka.lk — instructions for Claude

This repository holds the tools and the results of a check of `public/static/text-apz` in
github.com/pathnirvana/tipitaka.lk (the "simplified Sinhala" text based on A. P. de Zoysa's translation, cut to the
Buddha Jayanthi (BJT) entries) for its maintainer, Path Nirvana. The owner of this repository (etomelk@gmail.com, Hemal)
reads Sinhala and English; reply in plain English, keep Pāli and Sinhala in Sinhala script. It is not a website and has
nothing to do with the owner's Nikāya sites, which show the archived de Zoysa and are not changed by this work.

**Accuracy matters more than anything else.** A row sent to the maintainer changes his text. Never report an error you
have not read in the Pāli entry, never invent a reading, and when in doubt put the row in the unsure file or leave it out.

## History

- 2026-11-11: first check, by script, of text-apz at 974bd90 against the archived de Zoysa (pathnirvana/pitaka.lk-archive)
  and the BJT entries: four Nikāyas (15,264 rows) and twelve Khuddaka books (5,061 rows), with a confirmed list of 528.
- 2026-11-12: the maintainer's reply. He applied the 33 id lines, an-4-4 page 3 entries 1 and 3, the `ai` flag on the
  2,181 unflagged entries, and is retranslating the 283 entries left in Pāli. Two of our rows were wrong (below). He set
  the brief that follows. Pilot the same day on `dn-1` at e4db85e: 22 entries read, 1 confirmed row, 2 unsure.

## The maintainer's brief (2026-11-12): what counts, and what to send

**Only confirmed errors.** The BJT Pāli decides, not de Zoysa: the model often corrected de Zoysa, and those corrections
stand. A row is useful only if the current text is wrong against the Pāli entry. Report only **meaning errors**:
a negation reversed; the wrong person or subject; a wrong number; a clause missing or added; text that belongs to
another entry; Pāli left in.

**Order of work** (`tools/work.py list <step>`):
1. The model-written and partly rewritten entries of the four Nikāyas that had no `ai` flag at 974bd90 (under 90% of
   their words de Zoysa's; 5,250 entries at e4db85e). Read each against its Pāli entry.
2. `duplicate`, `length-long` (not `-abbr`) and `moved` (302 entries).
3. `dropped` (526 entries): only where something in the Pāli entry is really untranslated.
4. The `pali-words` rows of the four Nikāyas (202): drop names, uddāna key words and quoted formulas.
5. The Khuddaka, starting with the Dhammapada and the Udāna. (Checked 2026-11-12: the archived Dhammapada is the same
   de Zoysa text; text-apz adds a verse number to every entry and writes out de Zoysa's cross-references, which is why
   few entries are word for word. Without the verse numbers 190 of 433 verses are word for word.)

**Skip:** all of group E (`added`, `changed-*`, `word-dropped`), `dropped-gloss`, `dropped-repeat`, `dropped-abbr`,
`dropped-between*`, `number`, `footnote-mark`.

**Format:** one TSV per batch, one row per entry:
`file  page_idx  entry_idx  kind  current_text  proposed_text  pali_excerpt  reason`
- `current_text`: the whole entry exactly as in text-apz (he applies a row only if it still matches). `tools/work.py
  batch` copies it from the file; never type it.
- `proposed_text`: the whole corrected entry. **Change only what is wrong; keep the existing wording everywhere else.**
- New Sinhala (a missing clause, untranslated Pāli) follows his guidelines, `dev/apz-trans/prompt-v2.md` in tipitaka.lk
  (fetched by `tools/setup.sh`; read it before writing any): plain modern Sinhala for an ordinary reader, dignified,
  following BJT's reading; never copy BJT's Sinhala as it stands (old forms, and some entries hold only
  `__missing translation__`); curly quotes; the paragraph number kept; -පෙ- kept where the Pāli has it.
- `pali_excerpt`: the Pāli words the correction rests on, copied from the Pāli entry (the script checks they are in it).
- `reason`: one line.
- Anything not sure: the separate unsure file, or left out.

**Where:** one GitHub issue per batch on pathnirvana/tipitaka.lk, with the TSV attached, naming the commit it was run
against. Claude cannot post there: the owner posts each batch. His fixes change the text, so every batch is built
against the latest commit (`tools/setup.sh` always moves to it).

## How to read an entry (rules learned so far)

- Read the **whole** apz entry against the **whole** Pāli entry, clause by clause: every clause, name, number and list
  item. Use the BJT Sinhala shown beside it only to see how BJT reads a doubtful word, never as the standard.
- **Look for a clause everywhere in the entry before calling it missing.** Our first report said `mn-1` page 10 entry 0
  lacked අජ්ඣත්තං කථංකථී හොති; it was translated at the end of the sentence. Sinhala puts the verb and its
  complement last.
- **Names are not untranslated Pāli.** River names, personal names, uddāna key words and quoted formulas
  (“ඉතිපි සො භගවා...”) stay as they are (our `an-8` page 43 row was wrong for this reason).
- A different but defensible word choice, a gloss in brackets, de Zoysa's or the model's explanatory additions that BJT's
  Sinhala also has, old spellings, and style are **not** errors. Where the Sinhala follows a reading other than BJT's
  Pāli, check BJT's Sinhala: if BJT's own Sinhala reads the same, it is not an error (dn-1 §28, අනිය්යානං).
- Where the Pāli abbreviates (-පෙ-) and the Sinhala writes the passage out, or the reverse with an abbreviation mark,
  that is not an error. Where the Pāli writes a passage out and the Sinhala gives "..." for it, it is (an-7-2 page 33).
- An entry that repeats its neighbour while the Pāli entries differ is the kind of error most worth finding (an-4-4
  page 3, entries 1 and 3): compare each entry with the one before it when the Pāli entries are near-twins.
- For the wording of a correction, find how text-apz itself renders the same Pāli elsewhere (grep the phrase) and use
  the most frequent form, so that a fix reads like its surroundings.
- The pilot's yield was low (1 sure in 22). Most entries are sound. Do not lower the bar to find more.

## Tools

- `bash tools/setup.sh` fetches the sources into `../apz-sources` (or `$APZ_SRC`), moves to the latest commit and prints
  `APZ_SRC=` and `COMMIT=`; export `APZ_SRC`.
- `python3 tools/analyse.py dn mn sn an` lines every text-apz entry up with the archived de Zoysa (`out/<nik>.json`, not
  committed); `python3 tools/findings.py dn mn sn an` classifies (`findings/<nik>.tsv`, not committed). Khuddaka books:
  `kn-khp kn-dhp kn-ud kn-iti kn-snp kn-vv kn-pv kn-thag kn-thig kn-ap kn-bv kn-jat`. Run both after every setup: the
  text changes upstream.
- `python3 tools/work.py list <step> [nik]`, `show <step> <file> [start] [n]`, `done <step> <file> <pi>:<ei> …`,
  `batch <name> <file> …`, `status`. Entries read are recorded in `data/read.json`; findings in
  `verdicts/<file>.json` (format in `tools/work.py`); batches in `batches/`.
- `data/ai_flagged_at_974bd90.json`: the entries flagged `ai` before the maintainer flagged ours (outside step 1).

## Branches

Work goes to the branch `autopilot`; the owner reads each finished batch, posts it as an issue, and merges into `main`.
Commit messages: plain English, what was read and what was found.
