# text-apz, Aṅguttara Nikāya: 146 confirmed errors against the Pāli (model-written and partly rewritten entries)

Run against commit **6a14af6** of pathnirvana/tipitaka.lk, as asked in #158 (none of these entries was changed between e4db85e and 6a14af6; every row was rebuilt against 6a14af6 and still matches).

**What was read.** The 1,618 entries of `public/static/text-apz/an-*.json` that are model-written or partly rewritten
(under 90% of their words de Zoysa's) and had no `ai` flag at 974bd90, in all twenty-eight files. Each was read in full
against its BJT Pāli entry, clause by clause. A row is given only where something in the Pāli is missing, wrong or
reversed, or where Pāli is left in the text; restatements, redundancy, loose wording, word choice, glosses, spelling
and style are left alone.

**Attached: `an-step1_6a14af6.tsv`, 146 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at 6a14af6, copied by script;
`proposed_text` changes only what is wrong.

| kind | rows |
|---|---|
| clause-missing, phrase-missing, list-item(s)-missing (a clause, a phrase or list items missing; or “...” where the Pāli writes the passage out) | 56 |
| pali-left-in (Pāli left in the entry; where its translation stands beside it, the Pāli is taken out) | 32 |
| wrong-word, wrong-sense (the wrong item or thing) | 21 |
| wrong-number | 14 |
| wrong-subject, wrong-person (the wrong subject, speaker, person addressed or grammatical person) | 11 |
| negation / negation-reversed (a negation missing, added or reversed) | 8 |
| clause-added (words that are not in the Pāli entry) | 3 |
| other-entry-text (text that belongs to another entry) | 1 |

By file: an-1 3, an-3 8, an-3-2 8, an-3-3 3, an-4 2, an-4-4 7, an-4-5 1, an-5-2 3, an-5-3 2, an-5-4 5, an-5-5 2,
an-6 22, an-6-2 5, an-7 3, an-7-2 14, an-8 6, an-8-2 10, an-9 14, an-10 8, an-10-2 14, an-10-3 1, an-10-4 2,
an-10-5 1, an-11 2 (an-2, an-4-2, an-4-3 and an-5: none).

Twenty of the rows (an-3-2 35:2, an-3-3 26:14, an-5-4 41:4, an-6 27:0, 27:1, 27:2, 27:3, 28:5, 28:6, 29:0, 29:2,
29:3, an-7-2 32:5, 32:7, 32:8, 33:0, 33:1, an-8-2 35:1, an-10-2 62:4, 63:1) fill a “...” that stands where the Pāli
writes the passage out in full; each is filled with the entry's or the file's own wording of the same passage. If you
would rather leave those as they are, skip those rows.

Forty-one rows are entries outside the list above (mostly de Zoysa’s own text), found
beside an entry of the list because they have the same error in the same sentence or verse: an-3 15:8, 33:2, 33:7,
33:10, an-3-2 33:0, 34:0, 34:1, an-3-3 28:5, an-5-2 46:15, an-5-4 20:4, 20:6, an-6 55:8, 56:0, an-7-2 2:3, 4:1, 4:6,
an-8-2 42:1, 42:3, 42:7, 43:1, 43:3, 43:5, an-9 7:4, 8:0, 19:1, 19:2, 19:3, 20:0, 20:1, 20:3, an-10 71:3, 74:6, 75:0,
75:1, an-10-2 42:1, 69:7, 71:0, 71:1, 80:6, an-10-3 18:0, an-11 3:5.

One row (an-11 45:7) is in a vagga's summary verse (uddāna): දසමො ද්වෙ ච ගොපාලො is given as one sutta, “the
Gopāla sutta, the tenth”. Skip it if the summary verses are to stay as they are.

**Unsure, attached separately: `an-step1_6a14af6_unsure.tsv`, 1 row** (an-7-2 6:6: the Pāli gives both alternatives
of the gods' knowledge and the Sinhala only one; it may be meant as a rendering).
