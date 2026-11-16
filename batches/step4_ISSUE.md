# text-apz, four Nikāyas: 56 more confirmed rows, mostly Pāli left in the text (the entries with Pāli words)

Run against commit **e4db85e** of pathnirvana/tipitaka.lk.

**What was read.** The 202 entries of `public/static/text-apz/{dn,mn,sn,an}-*.json` in which a script finds Pāli
word forms in the Sinhala text (DN 44, MN 28, SN 86, AN 44). Each was read in full against its BJT Pāli entry.
Names, summary-verse (uddāna) key words, sutta names in headings and quoted formulas (“ඉතිපි සො භගවා …”) are left as
they are. 77 of the 202 were already rows of the collections sent before (DN, MN, SN, AN) and are not repeated here.

**Attached: `step4_e4db85e.tsv`, 56 rows** (one per entry: `file  page_idx  entry_idx  kind  current_text
proposed_text  pali_excerpt  reason`). `current_text` is the whole entry as it stands at e4db85e, copied by script;
`proposed_text` changes only what is wrong.

| kind | rows |
|---|---|
| pali-left-in | 52 |
| wrong-person | 4 |

By Nikāya: DN 11, MN 8, SN 26, AN 11.

- **A Pāli sentence or phrase before or after its own translation** (the Pāli is taken out, the translation kept):
  `dn-1-3` 20:7, 23:1, 68:0; `dn-1-6` 12:5; `dn-1-11` 63:2; `dn-2-3` 7:7; `dn-3-5` 28:3; `mn-1-3` 33:2, 34:2, 37:0;
  `mn-2-3` 60:0; `mn-3-2` 16:2; `sn-2` 14:8, 16:0, 17:6; `sn-4-1-12` 37:5; `an-6-2` 19:9; `an-10` 18:4; and the
  closing lines `dn-2` 53:2 and `mn-3-5` 48:9 (the bracketed translation kept alone).
- **Pāli with no translation beside it** (translated in the words text-apz has for the same sentence elsewhere, or
  on the entry's own pattern): `dn-2` 41:9 (five of the six feelings); `dn-3` 52:5; `dn-3-5` 90:1; `mn-2-4` 41:0
  (උළාරාය ච මං පූජාය පූජෙසි); `mn-3-5` 40:2 (එවං මෙ සුතං); `sn-5-11` 43:3 (එකං සමයං භගවා සක්කෙසු විහරති);
  `an-1` 33:8 (එවමෙව ඛො භික්ඛවෙ; ලොකෙ උප්පන්නො added too); `an-4-4` 27:0 (තස්ස ච සඞ්ඝස්ස දුග්ගහීතන්ති).
- **`sn-5-12`, 21 entries of the Āmakadhañña peyyāla** (45:12 – 50:2): each ends “-පෙ- යොගො කරණීයොති.”; given
  “-පෙ- වීර්යය කළ යුතුය.”, as 45:6 and 45:9 of the same vagga have it (and as 46:17, sent with the SN collection).
- **`an-3-2` 7:1, 7:2, 8:0** (the three knowledges, Tikaṇṇa sutta): each opens with its first sentence wholly or
  half in Pāli (… ඤාණාය චිත්තං අභිනින්නාමෙති); given in the words of 9:5, the same sentence in the next sutta.
  7:1 also lacks the thirty births (තිංසම්පි ජාතියො), and 7:1 and 7:2 give “...” where the Pāli entry writes the
  passage out; in 7:2 the two sentences on the beings of bad and good conduct are newly written.
- **Four rows found in passing** beside `an-4-4` 27:0 (wrong-person; their reasons say so): 27:2, 27:4, 28:1, 28:3.
  In the second, third and fourth great references the Sinhala says “මේ භික්‍ෂුව” where the Pāli has the Saṅgha
  (තස්ස ච සඞ්ඝස්ස), those elders (තෙසඤ්ච ථෙරානං) and that elder (තස්ස ච ථෙරස්ස).

**Unsure: none** (`step4_e4db85e_unsure.tsv` has no rows).

**Two things left as they are, for you to decide once rather than row by row:**
- `dn-3-10` (Saṅgīti, Dasuttara): the bold Pāli head of each set (“අපරාපි **තිස්සො ධාතුයො:**” …) stands before its
  list in every entry of the file, some with a translation after it and some without. Left alone as the form the
  whole file has.
- `an-4-2` 14:1, 14:10, 14:17: three headings keep the Pāli heading in square brackets before the Sinhala title
  (“[රූප (ප්පමාණ) සුත්තං] - රූප්පමාණ සූත්‍රය”). Sutta names, left alone.
