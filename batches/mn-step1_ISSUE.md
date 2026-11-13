# text-apz, Majjhima Nikāya: 69 confirmed errors against the Pāli (model-written and partly rewritten entries)

Run against commit **e4db85e** of pathnirvana/tipitaka.lk.

**What was read.** The 1,089 entries of `public/static/text-apz/mn-*.json` that are model-written or partly rewritten
(under 90% of their words de Zoysa's) and had no `ai` flag at 974bd90, in all fifteen files. Each was read in full
against its BJT Pāli entry, clause by clause. A row is given only where something in the Pāli is missing, wrong or
reversed, or where Pāli is left in the text; restatements, redundancy, loose wording, word choice, glosses, spelling
and style are left alone.

**Attached: `mn-step1_e4db85e.tsv`, 69 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at e4db85e, copied by script;
`proposed_text` changes only what is wrong.

| kind | rows |
|---|---|
| pali-left-in (Pāli left in the entry; where its translation stands beside it, the Pāli is taken out) | 25 |
| clause-missing (a clause, a phrase or list items missing; or “...” where the Pāli writes the passage out) | 18 |
| wrong-person (the wrong speaker, person addressed or grammatical person) | 7 |
| wrong-word (the wrong item or thing, or the reverse of the Pāli word) | 7 |
| clause-added (words that are not in the Pāli entry; three entries that hold their text three times) | 5 |
| moved (text standing in the entry after its own) | 5 |
| wrong-number | 2 |

By file: mn-1 8, mn-1-2 11, mn-1-3 8, mn-1-5 1, mn-2-2 2, mn-2-3 4, mn-2-4 13, mn-2-5 1, mn-3 3, mn-3-2 7, mn-3-3 3,
mn-3-4 1, mn-3-5 7 (mn-1-4 and mn-2: none).

Rows that belong together and should be applied together:
- mn-2-4 79:2, 79:3, 79:4, 80:0, 80:1 (the Kaṇṇakatthala's opening): the Sinhala of these five entries stands one
  entry late against the Pāli.
- mn-3-3 23:1 and 24:0 (the Dantabhūmi): five list items stand at the end of the entry before their own.

Five of the clause-missing rows (mn-3 58:2, 59:1, mn-3-5 30:3, 30:4, 31:0) fill a “...” that stands where the Pāli
writes a repeated sentence out in full; each is filled with the entry's own wording of that sentence, by script. If
you would rather leave those as they are, skip those rows.

Three rows are for entries outside the list read (mn-3-2 5:1, 6:1, mn-3-3 24:0): they carry the same error as, or
the other half of, a row beside them; only that part of them was read.

**Attached separately: `mn-step1_e4db85e_unsure.tsv`, 3 rows** (mn-1 76:4, mn-1-2 17:3, mn-3-3 60:6), where the
reading itself is in doubt.
