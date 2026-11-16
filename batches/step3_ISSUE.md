# text-apz, four Nikāyas: 16 more confirmed errors against the Pāli (entries where words of de Zoysa were dropped)

Run against commit **e4db85e** of pathnirvana/tipitaka.lk.

**What was read.** The 526 entries of `public/static/text-apz/{dn,mn,sn,an}-*.json` in which a comparison with the
archived de Zoysa shows a run of his words dropped (DN 106, MN 136, SN 129, AN 155; in 74 files). Each was read in
full against its BJT Pāli entry, clause by clause. A row is given only where something in the Pāli entry is missing,
wrong or reversed, where words stand that the Pāli does not have, or where Pāli is left in the text; restatements,
loose wording, word choice, glosses, spelling and style are left alone, and so are entries that write out what the
Pāli abbreviates. In most of the 526 the dropped words were a repetition, a gloss or an expansion the Pāli entry does
not have, and nothing is missing.

**Attached: `step3_e4db85e.tsv`, 16 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at e4db85e, copied by script;
`proposed_text` changes only what is wrong. None of these rows is in the collections sent before (DN, MN, SN, AN,
and the moved / long entries); entries of this list that were already reported there are not repeated. Five of the
rows (`sn-3-1-2` 67:2, `sn-4-1-12` 7:3, `an-10-2` 78:0 – 78:2) are entries beside the ones on the list, found while
reading them; their reasons say so.

| kind | rows |
|---|---|
| clause-missing | 5 |
| pali-left-in | 3 |
| list-item-missing | 2 |
| phrase-missing | 2 |
| negation | 2 |
| clause-added | 1 |
| other-entry-text | 1 |

- `mn-3-4` 38:0 and `sn-4-1-12` 7:3 (clause-missing): the monks' request to the elder (විභජතායස්මා … අගරුං කරිත්වා)
  is left out; in `mn-3-4` 38:0 also සො චෙව පනෙතස්ස කාලො අහොසි.
- `sn-2` 11:3 (list-item-missing): the cessation chain goes from clinging straight to birth; භවනිරොධො is not there.
- `sn-3-1-2` 67:2, 68:1 (pali-left-in): “නු ඛො” stands in the Sinhala sentence.
- `sn-3-7` 26:11 (pali-left-in): the Pāli closing line “සත්තපඤ්ඤාසසුත්තන්තං නිට්ඨිතං.” at the head of the entry.
- `sn-4` 74:2 (other-entry-text): the entry opens with the last sentence of the entry before it.
- `an-4` 43:16 (list-item-missing): ඉති විඤ්ඤාණං is not translated, as it is for the other four aggregates.
- `an-5-2` 27:0 (clause-missing): the monk's thought (තස්ස එවං හොති: යන්නූනාහං ආරාමං ගන්ත්වා …) is not translated.
- `an-5-4` 42:1 (negation): පජත්ථාව බ්රාහ්මණස්ස බ්රාහ්මණී හොති given as “දරුවන් පිණිස නොවන්නීය”.
- `an-6` 49:11 (phrase-missing): මහතා භික්ඛුසඞ්ඝෙන සද්ධිං is not translated.
- `an-7-2` 39:6 (clause-missing): “...” stands for ධම්මෙ සගාරවො සඞ්ඝෙ සගාරවො, which the Pāli entry writes out.
- `an-10-2` 78:0, 78:1, 78:2 (the fifth, sixth and seventh of the ten kāmabhogī): 78:0 and 78:1 say the man seeks
  wealth rightly only, where the Pāli has ධම්මාධම්මෙන … සාහසෙන පි අසාහසෙන පි, and 78:0 first says he shares and
  makes merit; 78:2 adds a sentence that blames him for seeking rightly and gives න අත්තානං සුඛෙති පීනෙති as
  “සුවපත් නොකෙරෙයි. පිනවයි.”
- `an-10-2` 85:3 (clause-missing): යං ඛො පන කිඤ්චි භූතං සංඛතං චෙතයිතං පටිච්චසමුප්පන්නං is not translated; the
  entry opens “එය අනිත්‍යය”.

**Unsure: none** (`step3_e4db85e_unsure.tsv` has no rows).
