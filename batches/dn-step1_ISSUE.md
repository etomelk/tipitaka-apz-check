# text-apz, Dīgha Nikāya: 59 confirmed errors against the Pāli (model-written and partly rewritten entries)

Run against commit **e4db85e** of pathnirvana/tipitaka.lk.

**What was read.** The 913 entries of `public/static/text-apz/dn-*.json` that are model-written or partly rewritten
(under 90% of their words de Zoysa's) and had no `ai` flag at 974bd90, in all eleven files. Each was read in full
against its BJT Pāli entry, clause by clause. A row is given only where something in the Pāli is missing, wrong or
reversed, or where Pāli is left in the text; restatements, redundancy, loose wording, word choice, glosses, spelling
and style are left alone.

**Attached: `dn-step1_e4db85e.tsv`, 59 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at e4db85e, copied by script;
`proposed_text` changes only what is wrong.

| kind | rows |
|---|---|
| pali-left-in (Pāli left in the entry; where its translation stands beside it, the Pāli is taken out) | 20 |
| clause-missing (a clause, a phrase or list items missing; or “...” where the Pāli writes the passage out) | 17 |
| clause-added (words that are not in the Pāli: “සතිය පිහිටුවා ගෙන” for සතා, nine entries of dn-2) | 9 |
| wrong-number | 6 |
| wrong-word (the wrong person, item or thing) | 4 |
| negation (reversed) | 2 |
| wrong-script | 1 |

By file: dn-1 2, dn-1-3 4, dn-1-6 10, dn-1-11 5, dn-2 16, dn-2-3 1, dn-2-7 3, dn-3 12, dn-3-5 5, dn-3-10 1
(dn-2-4: none).

Nine of the clause-missing rows (dn-1-3 63:0, dn-1-11 47:2, 48:1, 49:0, 50:2, dn-3 59:0, 62:0–63:1) fill a “...” that
stands where the Pāli writes a repeated passage out in full; each is filled with text-apz's own wording of the same
passage from a nearby entry, copied by script. If you would rather leave those as they are, skip those rows.

**Attached separately: `dn-step1_e4db85e_unsure.tsv`, 3 rows**, where the reading itself is in doubt.

**One question.** Two of the unsure rows (dn-1-3 36:4, dn-1-6 0:3) are examples of a rendering that stands in many
entries of all four Nikāyas: සො ධම්මං දෙසෙති ආදිකල්යාණං මජ්ඣෙකල්යාණං පරියොසානකල්යාණං සාත්ථං සබ්යඤ්ජනං,
කෙවලපරිපුණ්ණං පරිසුද්ධං බ්රහ්මචරියං පකාසෙති is given as one clause (“… පිරිසිදු බ්‍රහ්මචර්යාව ප්‍රකාශ කරයි”), with
no “he teaches the Dhamma” of its own. Do you want a row for each such entry, or is this rendering to stay?
