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

- 2026-11-13: the owner sent three sample rows of `dn-1`; the maintainer's answer: the sample is good, go ahead with
  the full run. 39:4 accepted; 64:5 accepted and belonged in the main file (a real omission); 63:5 left (a restatement).
  His added instruction is the paragraph "Added 2026-11-13" below; the findings of runs 1–6 were gone over again by it
  the same day (see `AUTOPILOT_LOG.md`).

## The maintainer's brief (2026-11-12): what counts, and what to send

**Only confirmed errors.** The BJT Pāli decides, not de Zoysa: the model often corrected de Zoysa, and those corrections
stand. A row is useful only if the current text is wrong against the Pāli entry. Report only **meaning errors**:
a negation reversed; the wrong person or subject; a wrong number; a clause missing or added; text that belongs to
another entry; Pāli left in.

**Added 2026-11-13 (the maintainer, after the sample).** Do not report restatements, redundancy or wording that is
only loose. Report a row only when something in the Pāli is **missing, wrong or reversed**, or when **Pāli is left in
the text**. When you are sure an entry is wrong against the Pāli, put it in the **main file even if the sense can be
pieced together from nearby text** (dn-1 64:5: the sentence left out ඉමමෙව කායං and නිප්පීතිකෙන). So:
- "Unsure" is for doubt about the **reading** (is it really wrong against the Pāli?), not for doubt about whether a
  sure error matters. A sure omission of a phrase or of list items goes in the main file, also when the words added
  are newly written (by his guidelines).
- An extra sentence that restates the Pāli (dn-1 63:5) is not a row. An added clause is a row only when it says
  something the Pāli does not, or says it wrongly (dn-2 39:4, “සතිය පිහිටුවා ගෙන” for සතා).
- Pāli left in the text is a row also when its translation stands beside it in brackets (the Pāli is taken out, the
  translation kept, by script), and when it is a stray Pāli word or heading. Names, uddāna key words and quoted
  formulas still stay.
- A single dropped word that changes nothing (an epithet, a particle, one of two synonyms) is still left alone.
- One open question for him, kept in the unsure files and not multiplied: de Zoysa's stock rendering of
  සො ධම්මං දෙසෙති ආදිකල්යාණං … බ්රහ්මචරියං පකාසෙති as one clause (“… පිරිසිදු බ්‍රහ්මචර්යාව ප්‍රකාශ කරයි”), with no
  “teaches the Dhamma” of its own; it stands in many entries (dn-1-3 36:4, dn-1-6 0:3). Do not add a row per entry;
  the DN issue text asks him once.
- **The commit:** he asked that every batch is run against **e4db85e** and holds his other edits to text-apz until
  the batches are in. `data/pin_commit.txt` holds `tools/setup.sh` to it.
- **The collections:** DN, MN, SN, AN, then the Khuddaka books, each posted as a GitHub issue when it finishes, so
  that he can apply them as they come. He asked Claude to post them; Claude has no access to pathnirvana/tipitaka.lk,
  so the owner posts each one (the run builds the files and the issue text and notifies him).

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
against one commit: from 2026-11-13 the pinned e4db85e (`data/pin_commit.txt`), as he asked.

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
- Do not leave a sure error out, or in the unsure file, because the reader could work the sense out from the
  sentence beside it (2026-11-13).

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
