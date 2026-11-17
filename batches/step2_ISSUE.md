# text-apz, four Nikāyas: 11 more confirmed errors against the Pāli (entries moved, or much longer than their Pāli)

Run against commit **6a14af6** of pathnirvana/tipitaka.lk, as asked in #158 (none of these entries was changed between e4db85e and 6a14af6; every row was rebuilt against 6a14af6 and still matches).

**What was read.** The 302 entries of `public/static/text-apz/{dn,mn,sn,an}-*.json` that a comparison with the archived
de Zoysa marks as moved from another place, as much longer than their Pāli entry, or as a duplicate (DN 20, MN 18,
SN 142, AN 122; in 52 files). Each was read in full against its BJT Pāli entry, clause by clause. A row is given only
where something in the Pāli is missing, wrong or reversed, where words stand that the Pāli does not have, or where
Pāli is left in the text; restatements, loose wording, word choice, glosses, spelling and style are left alone, and so
are entries that write out what the Pāli abbreviates.

**Attached: `step2_6a14af6.tsv`, 11 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at 6a14af6, copied by script;
`proposed_text` changes only what is wrong. None of these rows is in the four collections sent before (DN, MN, SN,
AN); entries of this list that were already reported there are not repeated.

| kind | rows |
|---|---|
| clause-added (words that are not in the Pāli entry) | 7 |
| wrong-word | 2 |
| clause-missing | 1 |
| list-item-missing | 1 |

- `sn-1` 49:3, 49:11, 49:19, 50:6 (clause-added): each entry's Pāli has only එකමන්තං ඨිතො ඛො … දෙවපුත්තො …, and
  the sutta opens at Sāvatthi in the entry before; the opening written out in these entries puts it at Rājagaha.
- `sn-3` 37:4 (wrong-word): අත්තදීපා … අත්තසරණා given as the Dhamma for one's lamp and refuge.
- `sn-3-1-3` 32:13, 32:16 (clause-added): “තදින් අල්ලා නොගැනීමෙන්” (අනුපාදාය) added to the question
  කල්ලන්නු තං සමනුපස්සිතුං.
- `sn-3-7` 1:10 (clause-missing): “(පෙ)” stands over Ānanda's words විප්පසන්නානි ඛො තෙ ආවුසො සාරිපුත්ත, ඉන්ද්රියානි …,
  which the Pāli writes out.
- `an-3-3` 42:13 (wrong-word): “සූනපක සමාධිය”, a garbled word, for the first concentration in five of the nine
  places (the other four have “සුඤ්ඤත සමාධිය”).
- `an-7` 8:7 (list-item-missing): the seven persons are six; දිට්ඨප්පත්තො is not there.
- `an-10-3` 26:6 (clause-added): the Pāli names only right view as the forerunner of wholesome qualities; the Sinhala
  says the same of each of the other nine factors. The nine added sentences are taken out; if you would rather keep
  de Zoysa's expansion, skip this row.

**Unsure: none** (`step2_6a14af6_unsure.tsv` has no rows).
