# text-apz, Saṃyutta Nikāya: 87 confirmed errors against the Pāli (model-written and partly rewritten entries)

Run against commit **e4db85e** of pathnirvana/tipitaka.lk.

**What was read.** The 1,630 entries of `public/static/text-apz/sn-*.json` that are model-written or partly rewritten
(under 90% of their words de Zoysa's) and had no `ai` flag at 974bd90, in all twenty-three files. Each was read in full
against its BJT Pāli entry, clause by clause. A row is given only where something in the Pāli is missing, wrong or
reversed, or where Pāli is left in the text; restatements, redundancy, loose wording, word choice, glosses, spelling
and style are left alone.

**Attached: `sn-step1_e4db85e.tsv`, 87 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at e4db85e, copied by script;
`proposed_text` changes only what is wrong.

| kind | rows |
|---|---|
| pali-left-in (Pāli left in the entry; where its translation stands beside it, the Pāli is taken out) | 38 |
| clause-missing (a clause, a phrase or list items missing; or “...” where the Pāli writes the passage out) | 22 |
| wrong-word (the wrong item or thing) | 9 |
| negation / negation-reversed (a negation missing, added or reversed) | 6 |
| wrong-person (the wrong speaker, person addressed or grammatical person) | 5 |
| wrong-number | 4 |
| clause-added (words that are not in the Pāli entry) | 3 |

By file: sn-1 3, sn-1-3 7, sn-2 3, sn-2-2 2, sn-2-5 5, sn-3 7, sn-3-1-2 2, sn-3-2 14, sn-3-7 1, sn-4 1, sn-4-8 7,
sn-5 3, sn-5-2 6, sn-5-3 1, sn-5-4 1, sn-5-7 4, sn-5-11 9, sn-5-12 11 (sn-1-7, sn-2-1-5, sn-3-1-3, sn-4-1-12 and
sn-4-2: none).

Nine of the clause-missing rows (sn-2 20:0, sn-2-5 0:10, sn-5-7 64:0, 64:1, 64:2, 65:0, sn-5-11 12:5, 14:0,
sn-5-12 12:8) fill a “...” that stands where the Pāli writes the passage out in full; each is filled with the
entry's or the file's own wording of the same passage. If you would rather leave those as they are, skip those rows.

Three wrong-person rows (sn-5-11 50:8, 51:2, 51:5) change one word each: the Buddha speaks to a Sakyan layman
(නන්දිය, භද්දිය, මහානාම) and the Sinhala says “මහණෙනි” at that one place.

One wrong-number row (sn-5-12 28:1) rests on a difference of editions: the BJT Pāli entry has සතධා භින්නස්ස වාළස්ස
and BJT's footnote gives සත්තධා as the other editions' reading; text-apz says seven. Skip it if you want that reading
kept.

**No unsure file this time:** `sn-step1_e4db85e_unsure.tsv` has no rows.
