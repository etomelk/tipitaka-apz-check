# Autopilot log

## 2026-11-12 (interactive session, the pilot)

Commit e4db85e. Read all 22 step-1 entries of `dn-1`. Findings: 39:4 pali-left-in (sure); 64:5 clause-missing (unsure);
63:5 clause-added (unsure). Batch `batches/dn-1_e4db85e.tsv` (1 row) and `_unsure.tsv` (2 rows). The other 19 entries are sound.

## 2026-11-12 (autopilot run 1)

Commit e4db85e (unchanged upstream since the pilot). Step 1, `dn-1-3`: all 137 entries read, each in full against its
Pāli; the file is finished in step 1. Batch `batches/dn-1-3_e4db85e.tsv` (5 rows, 0 unsure, nothing refused).

Findings, all sure:
- 12:1 pali-left-in: the entry opens with the Pāli of its own passage (“ඉධ අම්බට්ඨ, භික්ඛු පාණාතිපාතං පහාය... ඉදම්පි’ස්ස හොති
  සීලස්මිං.”) before a complete translation; the Pāli is removed.
- 23:0 wrong-word: ඉදම්පි’ස්ස හොති විජ්ජාය is given as “සීලාදියෙහි වන්නකි”; pages 24–27 of the same file give “විද්‍යාවෙහි”.
- 22:2 wrong-word: the same closing sentence. This entry is not on the step-1 list (it is 90% or more de Zoysa); only
  its closing sentence was read against the Pāli, when checking how the file renders the formula. Take the row out if
  rows from outside the list are not wanted.
- 36:4 clause-missing: සො ධම්මං දෙසෙති is not translated (wording taken from 49:6 of the same file).
- 63:0 clause-missing: the Pāli writes the four groups out; the Sinhala gives “...” for the members of groups 2–4.

Left alone, as the rules say: glosses in brackets (53:6 “(ධර්ම දේශනා කරති)”), dropped single words (සද්ධෙන 42:0, පාණෙහි
40:7), other word choices, and 61:0, where the Sinhala opens with a clause that belongs to the entry before it in the
Pāli (a different cut of the same passage, nothing lost).

Seen in passing, not read, not reported: 20:6 (not on the step-1 list) ends with a sentence that looks like the
Sāmaññaphala's refrain where the Pāli has ඉදම්පි’ස්ස හොති චරණස්මිං; it should come up in step 2 or 3, or be read then.

The add_repo tool named in the task prompt was not available in this session; the repository was already cloned in
the workspace with push access, so the run went ahead.

Left in step 1: 5,091 of 5,250 entries (DN: 754 of 913; next file `dn-1-6`, 212 entries).

## 2026-11-12 (autopilot run 2)

Commit e4db85e (unchanged upstream). Step 1, `dn-1-6`: the first 116 of its 212 entries read (pages 0–26: the Mahāli,
Jāliya and the first half of the Mahāsīhanāda sutta), each in full against its Pāli. The file is not finished, so no
batch file was written; the findings are in `verdicts/dn-1-6.json` (`work.py batch` was tried on them: 5 rows, 1 unsure,
nothing refused, and the trial files removed).

Findings, sure:
- 14:7 wrong-script: the first two letters of අන්නපානයෙන් are Telugu (అన్న). It is the only run of another script
  in the whole of text-apz (counted by script).
- 22:2, 23:4, 23:5 wrong-number: සායතතියකම්පි උදකොරොහන… is given as “දින තුනකට වරක් දියට බැසීමේ” (once in three
  days); it is three times a day, the evening the third. 25:1 of the same file has “සවස තුන්වැනි කොට (දිනකට තුන් වරක්)”;
  the correction uses “සවස තුන්වැනි කොට”.
- 26:5 pali-left-in: “සොතෙන සද්දං සුත්වා -පෙ- … කායෙන ඵොට්ඨබ්බං ඵුසිත්වා -පෙ-” stands in Pāli in the Sinhala; replaced
  by the wording text-apz uses for the same run elsewhere.

Unsure:
- 0:3 clause-missing: සො ධම්මං දෙසෙති has no verb of its own; the Dhamma's qualities are run into “බ්‍රහ්මචර්යාව ගෙන හැර
  දක්වති”. **For the owner:** this is de Zoysa's stock rendering of the formula (at least seven entries of DN and MN 1
  have it in this form), so it is a feature of the translation more than a slip of one entry. Run 1 reported one such
  entry as sure (`dn-1-3` 36:4); consider moving that row to the unsure file, or leaving the formula out altogether.
  From here on the formula is noted once per file as unsure, not per entry.

Left alone: “මුත්‍රාචාර” for මුත්තාචාරො (24:3; also an-4-4 and dn-3, there with the gloss “ආචාරශීලී පැවතුම් නැතිව”): a
habitual spelling, not a slip of one entry, though the word as spelt means something else; single dropped words
(දාරුපත්තික 5:2, සක්යපුත්තො 0:3, විඤ්ඤූ 19:2); CST-style instructions in brackets left out (15:1); passages the Pāli
abbreviates and the Sinhala writes out.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,975 of 5,250 entries (DN: 638 of 913; `dn-1-6` 96 left, starting at page 26).

## 2026-11-13 (autopilot run 3)

Commit e4db85e (unchanged upstream). Step 1, `dn-1-6`: the last 96 of its 212 entries read (pages 27–79: the end of
the Mahāsīhanāda, the Poṭṭhapāda and the Subha sutta), each in full against its Pāli; the file is finished in step 1.
Batch `batches/dn-1-6_e4db85e.tsv` (10 rows: run 2's 5 and this run's 5) and `_unsure.tsv` (1 row, run 2's);
nothing refused.

Findings of this run, all sure:
- 27:3 negation: අප්පහීණෙ is given as “පහකළාවූ”, so the monk sees the *abandoned* hindrances as a debt, a sickness
  and so on; corrected to “පහනොකළාවූ” (38:6 of the same file has “පහනොකළ” for the same sentence).
- 37:3 wrong-word: අබ්යාසෙකසුඛං is given as “අශ්‍රැතවත් (අබ්‍යාසේක) සැපය” (unlearned happiness); corrected to
  “කෙලෙසුන්ගෙන් තෙත් නොවූ”, the wording of mn-1-3 65:2 and mn-1-4 67:3.
- 69:4, 70:1, 71:2 pali-left-in (Subha sutta, first, second and fourth jhāna): the sentence “සො ඉමමෙව කායං …” stands
  in Pāli in the Sinhala, and in 70:1 and 71:2 the next clause (“නාස්ස කිඤ්චි … අප්ඵුටං හොති”) is not translated at
  all. Translated in the wording of 71:0 (the third jhāna of the same sutta). These may be among the entries the
  maintainer is already retranslating; a row applies only while the text still matches.

Left alone: 27:3 addresses “කාශ්‍යපය” where BJT's Pāli entry has ආවුසො (the sutta is spoken to Kassapa; the Pāli entry
seems to carry the address of another sutta); 34:2 has the stock rendering of සො ධම්මං දෙසෙති without a verb of its
own (noted once for this file in run 2, unsure); 44:4–11 give තථාගතො as “සත්ත්වයා” (the commentary's reading);
53:4–5 give ඔළාරිකො / මනොමයො අත්තපටිලාභො as “කාමභවයෙහි / රූපභවයෙහි ආත්ම ලැබීම” (a gloss, while 52:1 says “මනෝමය”);
single dropped words (අරියො 71:2, එවං පස්සතො 79:1); passages abbreviated in the Pāli.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,879 of 5,250 entries (DN: 542 of 913; next file `dn-1-11`, 114 entries).

## 2026-11-13 (autopilot run 4)

Commit e4db85e (unchanged upstream). Step 1, `dn-1-11`: all 114 entries read (the Kevaḍḍha sutta from §38, the
Lohicca sutta, the Tevijja sutta), each in full against its Pāli; the file is finished in step 1. Batch
`batches/dn-1-11_e4db85e.tsv` (5 rows) and `_unsure.tsv` (none); nothing refused.

Findings, all sure, all kind clause-missing:
- 48:4 (Lohicca §76): ආවීභාවං තිරොභාවං (he appears, he vanishes) is not translated; added as “ප්‍රකට බවටද,
  අප්‍රකට බවටද පැමිණෙයි” (the wording of dn-3-5; “ප්‍රකට බවට, මුවහ බවට” is the commonest form but does not stand as a
  sentence here). In the same entry පල්ලඞ්කෙන is “පරෙවි අයුරින් (පළඟින්)” (in the manner of a dove); changed to
  “පළඟින් හිඳගෙනම”, as text-apz has it elsewhere.
- 47:2, 48:1, 49:0, 50:2 (Lohicca §69, 73, 77, 83): after the simile the Pāli writes the passage out in full and the
  Sinhala gives “...” for part of it: in 47:2 the eight qualities of the mind and the whole description of the body, in
  48:1 and 49:0 the eight qualities, in 50:2 the qualities and the kinds of mind between the first and the last two.
  Each is filled with the wording of the entry just before it, copied by script, nothing newly written. Where the
  “...” stands for the Pāli's own -පෙ- it is kept.

**For the owner:** these four rows rest on the rule in `CLAUDE.md` (“where the Pāli writes a passage out and the
Sinhala gives "..." for it, it is [an error]”). They lose a repetition, not a new statement; if the maintainer does
not want such rows, drop them from the batch. 49:2 (§79) has the same “...”, but what it leaves out stands in the
first half of the same entry, so it was left alone.

Left alone: the barber's name, “රොසික” where BJT's Pāli has භෙසිකා (28:5 gives it as “රොසික (භේසික)” at the first
mention, de Zoysa's own note of the two readings; 29:3 ends with “භේසිකය”); “කල්ප විස්සකින් යුත් කල්පයන්” for
සංවට්ටකප්පෙ (19:1, de Zoysa's gloss); the glosses “මිථ්‍යාදෘෂ්ටි නමැති නරාවළ”, “ධර්මදේශනාව නමැති අතින්” (54:4);
“මසුන් රංචුද” in the man's thought where BJT's Pāli entry has no මච්ඡගුම්බා there (54:0); the Pāli formula
“අයමෙව උජුමග්ගො …” kept with its translation in brackets (58:0, 59:2, 60:2, 61:2: a quoted formula); single dropped
words (දක්ඛො 17:0, බලං 29:1, මහින්ද spelt “මහින්ධි” 62:1).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,765 of 5,250 entries (DN: 428 of 913; next file `dn-2`, 79 entries).
