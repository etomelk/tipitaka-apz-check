# text-apz, Dīgha Nikāya: 43 confirmed meaning errors (model-written and partly rewritten entries)

Run against commit **e4db85e** of pathnirvana/tipitaka.lk.

**What was read.** The 913 entries of `public/static/text-apz/dn-*.json` that are model-written or partly rewritten
(under 90% of their words de Zoysa's) and had no `ai` flag at 974bd90, in all eleven files. Each was read in full
against its BJT Pāli entry, clause by clause. Only errors of meaning against the Pāli are reported; word choice,
glosses, spelling, style and passages abbreviated or written out differently from the Pāli are left alone.

**Attached: `dn-step1_e4db85e.tsv`, 43 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at e4db85e, copied by script;
`proposed_text` changes only what is wrong.

| kind | rows |
|---|---|
| pali-left-in (Pāli left untranslated in the entry) | 12 |
| clause-missing | 9 |
| clause-added (text that belongs to another entry, or is not in the Pāli) | 9 |
| wrong-number | 6 |
| wrong-word (the wrong person, item or thing) | 4 |
| negation (reversed) | 2 |
| wrong-script | 1 |

By file: dn-1 1, dn-1-3 5, dn-1-6 10, dn-1-11 5, dn-2 12, dn-2-3 1, dn-2-7 1, dn-3 4, dn-3-5 3, dn-3-10 1
(dn-2-4: none).

**Attached separately: `dn-step1_e4db85e_unsure.tsv`, 11 rows** in the same format. These are not sure: mostly Pāli
that stands beside its own translation, a single compound not rendered, or a repetition the Pāli writes out and the
Sinhala shortens. Apply them only if you agree on reading them.
