# text-apz, four Nikāyas: සො ධම්මං දෙසෙති … බ්රහ්මචරියං පකාසෙති run together, 26 rows (asked for in #158)

Run against commit **6a14af6** of pathnirvana/tipitaka.lk.

**What was read.** Every entry of `public/static/text-apz/{dn,mn,sn,an}-*.json` whose BJT Pāli entry has the
formula ධම්මං දෙසෙති ආදිකල්යාණං මජ්ඣෙකල්යාණං පරියොසානකල්යාණං සාත්ථං සබ්යඤ්ජනං, කෙවලපරිපුණ්ණං පරිසුද්ධං
බ්රහ්මචරියං පකාසෙති in any person or tense (දෙසෙති, දෙසෙමි, දෙසෙස්සති, දෙසෙන්ති, දෙසෙථ): 60 entries (DN 19, MN 15,
SN 9, AN 17). The 33 other entries with ආදිකල්යාණ have a different formula (යෙ තෙ ධම්මා ආදිකල්යාණා … අභිවදන්ති)
and are not part of this.

**Attached: `step6_6a14af6.tsv`, 26 rows** (`file  page_idx  entry_idx  kind  current_text  proposed_text
pali_excerpt  reason`; `current_text` copied by script from 6a14af6). In each, “teaches the Dhamma” has no verb of
its own and the qualities of the Dhamma are run into the clause on the holy life. Each is split as you split
`dn-1-6` 0:3 in 6a14af6: ආදිකල්යාණං … සාත්ථං සබ්යඤ්ජනං with the Dhamma, කෙවලපරිපුණ්ණං පරිසුද්ධං with the holy
life. Only “ධර්මය දේශනා කරති.” (in the verb form of the entry's own sentence) is added; nothing else is changed,
except where said below.

| Nikāya | rows | entries |
|---|---|---|
| DN | 12 | `dn-1` 53:7; `dn-1-3` 0:4, 11:3, 66:6; `dn-1-6` 34:2, 58:4; `dn-1-11` 2:2, 28:4, 34:4, 66:6; `dn-2` 34:1; `dn-3` 64:4 |
| MN | 7 | `mn-1-3` 64:0; `mn-1-4` 66:0; `mn-1-5` 0:4; `mn-2` 53:2; `mn-2-5` 0:3, 6:0; `mn-3-3` 24:1 |
| SN | 6 | `sn-4-8` 8:1, 8:2, 8:3, 9:1, 9:2, 9:3 |
| AN | 1 | `an-4-4` 5:4 |

- `dn-1-3` 0:4 and `mn-2-5` 0:3 give the whole as one clause on the Dhamma (“… ධර්මානුශාසනාව ප්‍රකාශ කරණසේක”,
  “… ධර්මය ප්‍රකාශ කරණසේක”) with no words for the holy life: “බ්‍රහ්මචර්යාව ප්‍රකාශ කරණසේක” is added.
- `dn-2` 34:1 also has no words for කෙවලපරිපුණ්ණං: given in the words of 34:0, the same sentence on the same page.
- `dn-3` 64:4 has the formula twice (Metteyya, and “as I now”); both are split.
- `an-4-4` 5:4: the sentence breaks off after “අග යහපත්.”; joined and split.

**Unsure, attached separately: `step6_6a14af6_unsure.tsv`, 4 rows** (`mn-2-5` 35:4; `an-3` 22:2, 22:3, 23:0). These
name the Dhamma but give the two clauses one verb (“… ධර්මය පිරිසිදුවූ බ්‍රහ්මචරියාව දේශනා කරණසේක”; “… ධර්මය, …
බ්‍රහ්මචර්‍ය්‍යාව දේශනා කෙරෙද්ද”). Apply them if you count this as run together.

**Already split, no row** (30 entries): the two you fixed, and those where “ධර්මය දේශනා කරයි” stands as its own
clause, also where it stands before the list (`an-6-2` 5:1, `an-9` 9:1) or where the formula is abbreviated with
-පෙ- as in the Pāli (`an-6-2` 5:2, 5:4, 5:5; `an-9` 9:2–9:5).
