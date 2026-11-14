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

## 2026-11-13 (autopilot run 5)

Commit e4db85e (unchanged upstream). Step 1, `dn-2`: all 79 entries read (the Mahāpadāna sutta and the Mahānidāna
sutta), each in full against its Pāli; the file is finished in step 1. Batch `batches/dn-2_e4db85e.tsv` (12 rows) and
`_unsure.tsv` (2 rows); nothing refused.

Findings, sure:
- 6:0 pali-left-in (Mahāpadāna §15, the monks' report): two stretches stand in Pāli, the opening
  (“අච්ඡරියං ආවුසො … සාවකසන්නිපාතතොපි අනුස්සරිස්සති”) and the first question (“කින්නු ඛො ආවුසො … ඉතිපීති?”).
  Translated with the wording text-apz has for the same passage at 4:3 and 5:0 and the list of the entry's own third
  part, put together by script; nothing newly written.
- 21:0 pali-left-in (§61): the answer of the one gone forth (the six “සාධු …”) stands in Pāli; translated in the
  words the same entry uses for the prince's reply.
- 38:2 clause-missing (§122): of the six ways of recollecting, by name and by clan (නාමතොපි, ගොත්තතොපි) are not
  in the Sinhala; added in the entry's own form.
- 39:4, 39:5, 39:6, 39:7, 40:0, 40:1, 40:2, 40:3, 40:4 clause-added (Mahānidāna §3, the nine questions): පුට්ඨෙන සතා
  is given as “ඇසූ කල්හි සතිය පිහිටුවා ගෙන” (when asked, having set up mindfulness). සතා is “being” (by one who is
  asked), not sati; BJT's Sinhala has “විචාරන ලද්දාහු විසින්”. The words are removed and the address ආනන්ද, which
  the Sinhala lacks, stands in their place. One reading, nine rows; the commentary was not at hand in this run, so
  the rows rest on the grammar and on BJT's Sinhala.

Unsure:
- 46:0 (§22): (එත්තාවතා) ඉත්ථත්තං පඤ්ඤාපනාය is not translated; the added words are newly written after BJT's reading.
- 47:2 (§28): the entry opens with a Pāli heading, “නඅත්තපඤ්ඤත්ති”, and gives the number 28 twice (the Pāli entry
  has no heading); not an error of meaning.

Left alone: a stray Pāli “ඛො” in 17:0 (“‘එසේය දේවයන් වහන්සැයි’ ඛො මහණෙනි”); the Pāli sentence kept with its
translation in brackets after it (51:8 “නො හෙතං භන්තෙ”, 53:1 the closing line); “පබ්බජිත නාම නම් සාධුය” in 21:0
(de Zoysa keeps “පබ්බජිත නාම” in 20:3 too); උස්සඞ්ඛපාදො as “උස්ව සිටි විලුම්” (11:8; BJT “බොලට”); එවංගොත්තා
missing from the first list of 6:0 (a single word); “අත්ථි ඉදප්පච්චයා ජරාමරණං” given as “when this condition is
there, is there ageing and death?” (39:4 and the eight after it; the answer still reads rightly).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,686 of 5,250 entries (DN: 349 of 913; next file `dn-2-3`, 46 entries).

## 2026-11-13 (autopilot run 6)

Commit e4db85e (unchanged upstream). Step 1, three files finished: `dn-2-3` (46 entries, the Mahāparinibbāna sutta),
`dn-2-4` (17, the Mahāsudassana, Janavasabha and Mahāgovinda suttas) and `dn-2-7` (30, the Mahāsamaya, Sakkapañha,
Mahāsatipaṭṭhāna and Pāyāsi suttas): 93 entries, each read in full against its Pāli. Batches
`batches/dn-2-3_e4db85e.tsv` (1 row), `dn-2-4_e4db85e.tsv` (no rows), `dn-2-7_e4db85e.tsv` (1 row) and
`dn-2-7_e4db85e_unsure.tsv` (2 rows); nothing refused.

Findings, sure:
- dn-2-3 54:6 pali-left-in (the four places to be seen): the third place stands in Pāli (“මෙහි තථාගතෙන අනුත්තරං
  ධම්මචක්කං පවත්තිතන්ති”); the other three are translated. Replaced with the wording of the same clause in entry 9 of
  the same page, copied by script.
- dn-2-7 0:2 pali-left-in (Mahāsamaya §1): the last sentence stands in Pāli (“අථ ඛො චතුන්නං සුද්ධාවාසකායිකානං
  දෙවතානං එතදහොසි:”). Replaced with text-apz's own wording of the sentence in `sn-1` 23:0 (the Samaya sutta),
  copied by script.

Unsure:
- dn-2-7 50:3 (separation from the dear): ජෙට්ඨා වා කනිට්ඨා වා is missing from the list of relatives; two list
  words, and the added words are newly written.
- dn-2-7 61:5 (Pāyāsi §2): the whole Pāli paragraph stands in the entry with its translation after it in brackets;
  the proposed text is the bracketed translation alone. The translation is sound, so not an error of meaning.

Left alone: the gloss “(සංඝයාගේ මනා පිළිවෙතට ද)” added in brackets to the verse of dn-2-4 35:1; “(බුදු වී අටවැනි
සතියෙහි)” in dn-2-3 33:5; three words for the four of අඛණ්ඩානි අච්ඡිද්දානි අසබලානි අකම්මාසානි (dn-2-3 8:0); “ප්‍රිය”
dropped once in a repeated sentence (dn-2-4 5:6); “ආනන්ද” for “ආනන්දය” (dn-2-3 54:6, 54:7). In dn-2-4 41:2 the BJT
Sinhala shown beside the entry belongs to another of the eight praises; the apz entry agrees with its Pāli.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,593 of 5,250 entries (DN: 256 of 913; next file `dn-3`, 87 entries).

## 2026-11-13 (autopilot run 7)

Commit e4db85e (unchanged upstream). Step 1, one file finished: `dn-3` (87 entries: the Pāthika, Udumbarika,
Cakkavatti and Aggañña suttas), each read in full against its Pāli. Batches `batches/dn-3_e4db85e.tsv` (4 rows) and
`dn-3_e4db85e_unsure.tsv` (2 rows); nothing refused.

Findings, sure:
- 28:3 wrong-number (Udumbarika §1): තිංසමත්තෙහි පරිබ්බාජකසතෙහි, thirty hundred wanderers, is given as three hundred
  (“තුන් සියයක් පමණ”). One word changed (“තුන් දහසක් පමණ”); text-apz has “තුන් දහසක් පමණවූ” for the same words in
  `dn-1-6`, and BJT's Sinhala has තුන් දහසක්.
- 33:5 negation (Udumbarika §8, the ascetic who sorts his food): තං සාපෙක්ඛො පජහති, “gives it up with longing”, is
  given as “අපේක්ෂා රහිතව දුරු කරයි” (without longing), the same words the purified ascetic gets for අනපෙක්ඛො in
  36:3. One word changed (“අපේක්ෂා සහිතව”).
- 61:0 and 61:1 wrong-number (Cakkavatti §18): the life span of 320 years (වීසංතිවස්සසතායුකා: 160, 320, 640) is given
  as 360 (“තුන්සිය හැටක්”) in both entries. Changed to “තුන්සිය විස්සක්” (text-apz writes “එකසිය විස්සක්”,
  “දෙසිය විස්සක්” elsewhere).

Unsure:
- 36:4 (Udumbarika §11): ලාභසක්කාරසිලොකනිකන්තිහෙතු is not in the Sinhala; added in the words of the matching entry
  34:0. One compound, and the quoted thought carries most of its sense.
- 59:0 (Cakkavatti §16): the Pāli writes the application of the hunter simile out in full, the Sinhala gives “...”;
  filled with the entry's own words, copied by script. A repetition inside the entry, nothing of the meaning lost.

Left alone: 26:0 opens with the last sentences of the Pāli entry before it (a different cut of the same passage,
nothing lost) and gives “...” for the gods' gazing at each other, which the entry before it has in full; the going
forth abbreviated with the -පෙ- passage in 26:2; අජ්ඣාසයං not rendered in 29:2 and 30:1 (30:2 has it); භාතු පි භාතරි
(brother to brother) missing from the list of 59:0 (one list item); the list of abstentions given as “ප්‍රාණඝාතයෙන්...”
in 62:0–63:1 where the Pāli repeats it in full; “එවං මෙ සුතං:” kept before its translation in 47:2; ලොකක්ඛායිකං as
“ලොකායත කථාය” (28:4).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,506 of 5,250 entries (DN: 169 of 913; next file `dn-3-5`, 96 entries, then `dn-3-10`, 73: the DN
batch for the owner is due when both are read).

## 2026-11-13 (autopilot run 8)

Commit e4db85e (unchanged upstream). Step 1, one file finished: `dn-3-5` (96 entries: the end of the Sampasādanīya,
the Pāsādika, the Lakkhaṇa, the whole Siṅgāla and the Āṭānāṭiya suttas), each read in full against its Pāli. Batches
`batches/dn-3-5_e4db85e.tsv` (3 rows) and `dn-3-5_e4db85e_unsure.tsv` (2 rows); nothing refused.

Findings, sure:
- 25:1 pali-left-in and 25:2 clause-missing (Pāsādika §16, a pair): the reflection on alms food (ඉති පුරාණඤ්ච වෙදනං
  පටිහඞ්ඛාමි … ඵාසුවිහාරො චාති) stands in Pāli at the end of 25:1; in BJT it is the first sentence of the next Pāli
  entry, 25:2, whose Sinhala does not have it. Removed from 25:1 and added, translated, at the head of 25:2, in the
  words text-apz has for the same formula elsewhere; the closing “’යි කියායි” is newly written.
- 41:5 pali-left-in (Lakkhaṇa §6, the seven convex places): three Pāli sentences stand in the middle of the entry
  (තතො චුතො … සත්තස්ස උස්සදා හොන්ති:). Replaced with text-apz's own wording from the same sutta.

Unsure (Pāli that stands beside its own translation, as dn-2-7 61:5 in run 6):
- 79:2 (Āṭānāṭiya, verse 10): the first verse line stands in Pāli before the translation of the whole verse.
- 82:4 (Āṭānāṭiya §15): the opening Pāli words stand with their translation after them in brackets.

Left alone: in 22:2 (Pāsādika §13) the Sinhala explains ඉදමෙව with the “complete holy life” of the next entry
(de Zoysa's explanation, the next entry has it in its place); 66:3 භයස්ස කිච්චං කරොති is given as “(තමාගේ) කටයුතු
කරගනී” where BJT's Sinhala reads “does his friend's work only when he himself is in danger” (a bracketed gloss, the
Pāli allows both); 71:1 follows BJT's Pāli ඡහි ඨානෙහි in the closing sentence; 87:6 උපට්ඨිතං not rendered and
මහාරාජස්ස යසස්සිනො given twice; 91:4 හිරිනෙත්ති as two names; “සදිශාවෝ” for the six directions (spelling).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,410 of 5,250 entries (DN: 73 of 913; next and last DN file `dn-3-10`, 73 entries: the DN batch for
the owner is due when it is read).

## 2026-11-13 (autopilot run 9)

Commit e4db85e (unchanged upstream). Step 1, one file finished: `dn-3-10` (73 entries: the Saṅgīti and Dasuttara
suttas, mostly the short list entries of the threes to the sixes), each read in full against its Pāli. Batches
`batches/dn-3-10_e4db85e.tsv` (1 row) and `dn-3-10_e4db85e_unsure.tsv` (0 rows); nothing refused.

Finding, sure:
- 9:3 wrong-word (Saṅgīti, the three intoxications): the third, ජීවිතමදො (intoxication with life), is given as
  “ජාති (උසස් ජාතියකය යන) මදය” (pride of high birth). Replaced with “ජීවිත මදය”, which text-apz has for the same
  three in `an-3` and `an-5-2`; BJT's Sinhala reads ජීවිත මදය.

Left alone: 62:2 (Dasuttara, the fours' summary) writes out nine of the ten heads where the Pāli abbreviates with
-පෙ- (අභිඤ්ඤෙය්යා is not among them; an expansion of an abbreviation, the Pāli entry itself does not have it);
71:2 gives උපෙක්ඛා චෙතොවිමුත්ති as “උපෙක්ෂා සමාධිය” (word choice); 27:1 gives සුවිමුත්තං as “බැසගන්නාලදී”, as it
gives විමුච්චති throughout the passage; 8:2 “චිත්තාමය” for චින්තාමය with the right gloss (spelling); the bold Pāli
heads kept before each list, as everywhere in these two suttas; the jhānas and the heavens written out where the
Pāli abbreviates (11:2, 45:2, 31:5).

**The Dīgha Nikāya is finished in step 1** (913 entries read over runs 1–9, all at e4db85e). The batch for the owner
to post: `batches/dn-step1_e4db85e.tsv` (43 rows: 12 pali-left-in, 9 clause-missing, 9 clause-added, 6 wrong-number,
4 wrong-word, 2 negation, 1 wrong-script) and `batches/dn-step1_e4db85e_unsure.tsv` (11 rows), with the issue text
`batches/dn-step1_ISSUE.md`. Built afresh from all eleven verdict files against the current text: nothing refused,
so no entry reported has changed upstream since it was read. This run's kind was first written “wrong-item” and
renamed “wrong-word”, the kind already used for a wrong person or thing.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,337 of 5,250 entries (MN 1,089, SN 1,630, AN 1,618; next file `mn-1`, 75 entries).

## 2026-11-13 (autopilot run 10)

Commit 96aedf5 (upstream has moved on from e4db85e; its last commit is “Word alignments for AN 1-11”). The comparison
was rebuilt; the step lists have the same counts as before. **The Dīgha batch still holds at the new commit:**
`work.py batch dn-step1 …` run against 96aedf5 gave the same 43 rows and 11 unsure, nothing refused, byte for byte the
file of run 9 (so `batches/dn-step1_e4db85e.tsv` can be posted as it is; the copy named for 96aedf5 was not kept).

Step 1, the Majjhima begun: `mn-1` finished (75 entries: the Mūlapariyāya, Sabbāsava, Dhammadāyāda, Bhayabherava,
Anaṅgaṇa, Ākaṅkheyya, Sallekha, Sammādiṭṭhi and Satipaṭṭhāna suttas and the vagga's closing verses) and the first 26
entries of `mn-1-2` (the Cūḷasīhanāda sutta and the opening of the Mahāsīhanāda), 101 entries, each read in full
against its Pāli. Batches `batches/mn-1_96aedf5.tsv` (8 rows) and `mn-1_96aedf5_unsure.tsv` (1 row); nothing refused.

Findings, sure (all in `mn-1`):
- 7:2 wrong-word (Mūlapariyāya §36, the arahant free of delusion): the Pāli abbreviates the series and ends with
  Nibbāna known as Nibbāna; the entry writes the whole series out as one list and says that all of these (water, fire,
  the gods … and Nibbāna) are taken “as Nibbāna”. Replaced with the abbreviated form that page 6 entries 2 and 6 have.
- 57:5, 58:3, 59:1, 59:6 pali-left-in (Sammādiṭṭhi, the closing of the sections on ageing and death, birth, existence
  and clinging): the closing sentences එත්තාවතාපි ඛො ආවුසො … ආගතො ඉමං සද්ධම්මන්ති stand in Pāli. Replaced with
  text-apz's own wording of them, copied by script from page 59 entry 4 (a full stop it lacks there added).
- 58:2, 59:0, 59:5 pali-left-in (the same sutta): the two sentences “from the arising of X the arising of Y, from the
  cessation of X the cessation of Y” stand in Pāli (භවසමුදයා ජාතිසමුදයො. භවනිරොධා ජාතිනිරොධො. and the like).
  Translated with each entry's own terms (“භවසමුදයෙන් ජාතිසමුදය වේ. භවනිරොධයෙන් ජාතිනිරොධය වේ.”): this wording
  is newly written, on the pattern of page 60 entry 2.

Unsure:
- 76:4 wrong-number (the fourth closing verse of the vagga, a compressed verse): “five hundred suttas, another hundred
  and fifty, two expositions and two others” where the Pāli has පඤ්ඤස, fifty: the first fifty and another hundred, a
  hundred and fifty, and two others (BJT's Sinhala reads it so). The proposed wording is newly written.

Left alone: `mn-1` 6:1 and the like give සම්මදඤ්ඤා විමුත්තො as “සසරින් මිදුනාවූ” and අභිජානාති as “හඟියි” (word
choice); 11:2 “මුවණින්” (spelling); 28:1 කංසපාති as “රන් තලියක්”; 20:3–22:1 leave out අකුසලං in “භයභෙරවං
අව්හයන්ති”; 76:5 gives the suttas' names where the verse has key words. `mn-1-2` 0:4 gives the wanderers' quotation
twice, the second time in Pāli with its translation in brackets after it (a quoted formula beside its translation;
nothing is missing).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,236 of 5,250 entries (MN 988 of 1,089; next file `mn-1-2`, 205 of its 231 entries still to read).

## 2026-11-13 (autopilot run 11)

Commit 96aedf5 (unchanged since run 10). The comparison was rebuilt; the step lists have the same counts.

Step 1, the Majjhima: the next 108 entries of `mn-1-2` (pages 6–34: the rest of the Mahāsīhanāda sutta, the
Mahādukkhakkhandha sutta from §7, and the Cūḷadukkhakkhandha sutta to §18), each read in full against its Pāli. The
file is not finished (97 of its 231 entries left), so no batch file was written; the seven findings were test-built
with `work.py batch` (6 rows, 1 unsure, nothing refused) and the test files removed.

Findings, sure (all in `mn-1-2`):
- 8:5 and 9:0 wrong-person (Mahāsīhanāda §16, the recollection of past lives): the quotation is in the first person
  (අමුත්රාසිං … සො තතො චුතො අමුත්ර උදපාදිං; තත්රාපාසිං … ඉධූපපන්නො) and the entries end it “හෙතෙම එතැනින් චුතව …
  උපන්නේය” (he … was born). Changed to “ඒ මම … උපන්නෙමි”; text-apz has the first person in this formula in its 40
  other places.
- 18:3 wrong-word (§47, the great-filth eating): පට්ඨිතගාවො, the pens the cattle have gone out of, is given as the pens
  “where the cattle are” (ගවයන් සිටින). Changed to “ගවයන් පිටත්ව ගිය”.
- 19:3 and 20:2 clause-missing (§50 and §53, the emaciated body): two of the six similes are left out, the gleam of
  water sunk deep in a deep well (the eyes) and the bitter gourd cut unripe and shrivelled by wind and sun (the scalp);
  only what they are said of is given. The two similes are newly written, after text-apz's own rendering of the same
  passage in `mn-2-4` page 46 entry 1.
- 20:1 clause-missing (§52, the rice grain): the sentences “you may think the rice grain was large then; it should not
  be seen so” are left out. Added in the wording page 19 entry 3 has for the jujube (with that entry's straight quotes).

Unsure:
- 17:3 clause-missing (§43, the garments): no item for තිරීටානි (bark garments). The entry has shroud-cloth instead,
  which this Pāli entry lacks but BJT's Sinhala has; it may be meant for තිරීටානි. The item added is newly written
  after BJT's reading.

Left alone: 9:0 opens with a paragraph number “17.” that its Pāli entry (the continuation of §16) does not have (the
kind `number` is skipped); 13:1 and the like give තසිතො as “තැතිගත්” beside “පිපාසිත” (word choice); 22:1 gives the
statement once where the Pāli has it twice; 20:1 writes out the mung-bean and sesame cases the Pāli abbreviates; 34:0
(Cūḷadukkhakkhandha §16) has the three tortures එණෙය්‍යක, බළිසමංසික, කහාපණක that this Pāli entry lacks and BJT's
Sinhala has; 32:2 softens ඛුප්පිපාසාය මීයමානො to “suffering from hunger and thirst”; 33:3 and 26:1 give පක්කට්ඨි
and අභිවග්ග otherwise than BJT (word choice).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,128 of 5,250 entries (MN 880 of 1,089; next file `mn-1-2`, 97 of its 231 entries still to read).

## 2026-11-13 (autopilot run 12)

Commit 96aedf5 (unchanged since run 10). The comparison was rebuilt; the step lists have the same counts.

Step 1, the Majjhima: the last 97 entries of `mn-1-2` (pages 35–77: the end of the Cūḷadukkhakkhandha sutta from §18,
the Anumāna, Cetokhila, Vanapattha, Madhupiṇḍika, Dvedhāvitakka and Vitakkasaṇṭhāna suttas, and the vagga's summary
verse), each read in full against its Pāli. The file is finished in step 1: `batches/mn-1-2_96aedf5.tsv` (8 rows) and
`_unsure.tsv` (1 row), nothing refused.

Findings, sure (both in `mn-1-2`):
- 35:1 wrong-person (Cūḷadukkhakkhandha §19): the summing-up “so, friends Nigaṇṭhas, you do not know …” (ඉති කිර තුම්හෙ
  ආවුසො නිගණ්ඨා න ජානාථ) is still spoken to the Nigaṇṭhas; the entry addresses it to Mahānāma (“මහානාමය, … ඔබලා …
  නොදන්නහුය”). The address is changed to “ඇවැත්නි නිගණ්ඨයෙනි” and the quotation mark the speech needs is opened (the
  entry already closes it).
- 72:0 pali-left-in (Dvedhāvitakka §14, the herd of deer): the first sentence, එවං හි සො භික්ඛවෙ මහාමිගසඞ්ඝො අපරෙන
  සමයෙන අනයව්යසනං තනුත්තං ආපජ්ජෙය්ය, stands in Pāli. Translated on the pattern of the entry's own last sentence; the
  words for අනයව්යසනං තනුත්තං (“විපතටද විනාශයටද අඩුවීමටද”) are newly written.

Unsure: none.

Left alone: 36:3 has “පෑ දවල් පහක්” for “රෑ දවල් පහක්” (a misprint, not a meaning error; the owner may want to
mention it); 40:3 “ලද්ේ” (misprint); 35:1 and 62:0, 65:2, 66:0 shorten a repetition the Pāli writes out (62:0 and
66:0 without “by his wise companions in the holy life”, විඤ්ඤූනං සබ්රහ්මචාරීනං), with or without an abbreviation
mark; 35:1 has no word for මනුස්සෙසු පච්චාජාතා; 35:2 and the like give අධිගච්ඡෙය්ය as “ලබාගත යුතුය”; 60:3 and
60:4 have no word for සදෙවමනුස්සාය; 74:0 gives the three verbs අට්ටීයෙය්ය හරායෙය්ය ජිගුච්ඡෙය්ය as one, and 76:4
two of three; 77:1 gives the suttas' names where the verse has key words.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 4,031 of 5,250 entries (MN 783 of 1,089; next file `mn-1-3`, 39 entries).

## 2026-11-13 (autopilot run 13)

Commit 96aedf5 (unchanged since run 10). The comparison was rebuilt; the step lists have the same counts.

Step 1, the Majjhima: all 39 entries of `mn-1-3` (the Alagaddūpama, Vammika, Rathavinīta, Nivāpa, Ariyapariyesana,
Cūḷahatthipadopama, Mahāhatthipadopama, Mahāsāropama and Cūḷasāropama suttas), all 38 of `mn-1-4` (the two Gosiṅga
suttas, the two Gopālaka suttas, the two Saccaka suttas, the two Taṇhāsaṅkhaya suttas, the two Assapura suttas) and
the first 36 of `mn-1-5` (pages 1–15: the Sāleyyaka and Verañjaka suttas and the Mahāvedalla to §20): 113 entries,
each read in full against its Pāli. `mn-1-3` and `mn-1-4` are finished in step 1: `batches/mn-1-3_96aedf5.tsv`
(8 rows, no unsure) and `batches/mn-1-4_96aedf5.tsv` (no rows), nothing refused.

Findings, sure (all in `mn-1-3`):
- 9:3 pali-left-in (Alagaddūpama §8): the first Pāli sentence of the entry stands before its translation; removed.
- 25:5 clause-missing (Vammika, “blazing by day”): කායෙන වාචාය මනසා is given as body and speech only; “සිතින් හෝ” added.
- 31:1 pali-left-in (Rathavinīta §15): the Pāli word තමෙනං stands at the head of the sentence that translates it; removed.
- 36:0 pali-left-in (Nivāpa, the third herd): two Pāli sentences stand before their translations (“යෙපි තෙ තතියා
  මිගජාතා එවං සමචින්තෙසුං:” and “යන්නූන මයං අමුං නිවාපං … ආසයං කප්පෙය්‍යාම.”); both removed.
- 51:5 clause-missing (Ariyapariyesana §28): of the pair ස්වාකාරෙ ද්වාකාරෙ only the first is translated;
  “අයහපත් ආකාර ඇත්තාවූද” added (the wording of dn-2 27:4). The bracketed [දුවිඤ්ඤාපයෙ] is also not in the
  entry; left as it is, since the Pāli brackets it.
- 52:2 and 52:3 wrong-word (Ariyapariyesana §30–31): මහාජානියො (“has had a great loss”; BJT “මහත් පිරිහීමෙක”) is
  given as “මහා ප්‍රඥාවන්තයෙකි” (a man of great wisdom), of Āḷāra and of Uddaka. Replaced with text-apz's own
  wording of the same sentences in mn-2-4 50:3–4 (“මහාපරිහානියකට පත්විය”). 52:2 is not on the step-1 list (it is
  de Zoysa's text, above 90%); it was read because it is the twin of 52:3 and has the same word.
- 53:0 pali-left-in (Ariyapariyesana, the group of five): the entry opens with “බහුකාරා ඛො මෙ පඤ්චවග්ගියා භික්ඛූ...”
  and the translated thought ends in the Pāli “’න්ති”; the Pāli words removed, the ending written “’යි”.

Unsure: none.

Left alone: `mn-1-3` 25:1 calls the deity (දෙවතා) “බ්‍රහ්මයා”, as de Zoysa does throughout the sutta (24:1, after
the commentary); 26:5 gives කොධූපායාස as “ක්‍රෝධය”; 36:0 does not repeat, inside the second herd's thought, the
recap of the first herd that the Pāli writes out (no abbreviation mark); 52:3 gives two of the three words පණ්ඩිතො
බ්‍යත්තො මෙධාවී; 92:1 and the like are plain. `mn-1-4` 22:0 gives උත්තරං තීරං as “එතෙරවූ”; 41:0 has four of the
five words කාමච්ඡන්දො … කාමපරිළාහො (no කාමපිපාසා) and 82:1 no word for විපුලෙන in the karuṇā and muditā
passages; 80:1 gives මිත්තාමච්චා as “මිත්‍රරාජ්‍යමාත්‍යයෝ” and එහි ත්වං භද්‍රමුඛ in the plural (word choice);
83:5 gives the suttas' names where the verse has key words. `mn-1-5`: nothing to note in the 36 entries read.

The add_repo tool was again not available; the repository was already cloned with push access. GitHub answered 503
(“authorization temporarily unavailable”) for the first minutes of the run, then worked.

Left in step 1: 3,918 of 5,250 entries (MN 670 of 1,089; next file `mn-1-5`, 78 of its 114 entries still to read).

## 2026-11-13 (with the owner: the maintainer's answer to the sample)

The owner sent three sample rows of `dn-1`. The maintainer accepted the sample (39:4 and 64:5; 63:5 left as a
restatement) and added: no restatements, redundancy or loose wording; a row only when something in the Pāli is missing,
wrong or reversed, or Pāli is left in the text; a sure error goes in the main file even if the sense can be pieced
together from nearby text; keep to e4db85e (he holds his other edits to text-apz); post each collection as it
finishes (DN, MN, SN, AN, then the Khuddaka books). `CLAUDE.md` (“Added 2026-11-13”), `AUTOPILOT.md` and
`tools/setup.sh` say so now.

**The commit is pinned** (`data/pin_commit.txt`, read by `tools/setup.sh`): runs 10–13 had followed upstream to
96aedf5. All batches were rebuilt at e4db85e with nothing refused, so the Majjhima entries read at 96aedf5 are the
same text at e4db85e; the batch files are named for e4db85e again.

**The findings of runs 1–13 and what those runs left alone were gone over by the new instruction:**
- Moved from unsure to the main file: dn-1 64:5; dn-2 47:2 (a Pāli heading, the number twice); dn-2-7 50:3 (two list
  members missing); dn-2-7 61:5, dn-3-5 79:2 and 82:4 (Pāli beside its own translation); dn-3 36:4 (a compound
  missing); dn-3 59:0 (“...” where the Pāli writes out; භාතු පි භාතරි added to its list too).
- Dropped: dn-1 63:5 (a restatement).
- New rows from what was left alone: dn-2 17:0 (a stray Pāli “ඛො”), 51:8 and 53:1 (Pāli before its bracketed
  translation); dn-2 6:0 also gets එවංගොත්තා in its first list; dn-3 47:2 (“එවං මෙ සුතං:” before its translation);
  dn-3 62:0, 62:1, 62:2, 63:0, 63:1 (“ප්‍රාණඝාතයෙන්...” where the Pāli writes the abstentions out; filled from 61:2,
  62:2 and 63:0 by script); mn-1-2 0:4 (the wanderers' quotation in Pāli before its bracketed translation); mn-1-2
  62:0 and 66:0 (විඤ්ඤූනං සබ්රහ්මචාරීනං left out, so the esteem is given to the Teacher; wording of 63:0).
- Moved to unsure, to match dn-1-6 0:3: dn-1-3 36:4. Both are de Zoysa's stock rendering of සො ධම්මං දෙසෙති …
  බ්රහ්මචරියං පකාසෙති as one clause, found in many entries: one question for the maintainer, asked in the DN issue
  text, not a row per entry.
- Still unsure (the reading is in doubt): dn-2 46:0, mn-1 76:4, mn-1-2 17:3.
- Still left alone: single dropped words and one of several near-synonyms (mn-1-4 41:0); quoted formulas; glosses;
  loose or shortened renderings with an abbreviation mark (mn-1-2 35:1, 65:2; mn-1-3 36:0); misprints.

**The Dīgha batch, rebuilt:** `batches/dn-step1_e4db85e.tsv`, **59 rows** (20 pali-left-in, 17 clause-missing,
9 clause-added, 6 wrong-number, 4 wrong-word, 2 negation, 1 wrong-script), `dn-step1_e4db85e_unsure.tsv`, 3 rows, and
a new `dn-step1_ISSUE.md`. It replaces the batch of run 9 (43 rows, 11 unsure); post this one.

The maintainer asked that Claude post the issues. Claude has no access to pathnirvana/tipitaka.lk: the owner posts
each collection. The Khuddaka is asked for after AN; `tools/work.py` has no step for it yet.

Left in step 1: 3,918 of 5,250 entries (MN 670 of 1,089; next file `mn-1-5`, 78 of its 114 entries still to read).

## 2026-11-13 (run 14)

Commit e4db85e (pinned). Step 1: the last 78 entries of `mn-1-5` (the Mahāvedalla from §20, the end of the
Cūḷavedalla, the Mahādhammasamādāna, Vīmaṃsaka, Kosambiya, Brahmanimantanika and Māratajjanīya suttas) and all 24 of
`mn-2` (Aṭṭhakanāgara, Sekha, Potaliya, Jīvaka, Kukkuravatika, Abhayarājakumāra, Bahuvedanīya, Apaṇṇaka): 102 entries,
each read in full against its Pāli. Both files are finished: `batches/mn-1-5_e4db85e.tsv` (1 row, none unsure) and
`batches/mn-2_e4db85e.tsv` (no rows), nothing refused.

Confirmed (main file):
- `mn-1-5` 48:0 pali-left-in (Kosambiya §6, the eight ways a mind is overcome): the Pāli verb හොති stands in the
  Sinhala sixteen times (“මැඩුණේ හොති, මැඩුණු සිත් ඇත්තේම හොති”, “යෙදුනේ හොති”). Written “වේ නම්” after ඉදින්
  and “වෙයි” at the end of each sentence, by script; nothing else changed. The form is found in no other entry of
  mn-1 … mn-1-5.

Unsure: none.

Left alone: `mn-1-5` 43:1 opens “4. 4.” (the paragraph number twice; a number, not a meaning error); 43:2 gives
සඞ්කිලිට්ඨා once as “ලාමක” and once as “කෙලෙස් සහිත” (word choice); 46:5 gives අප්පටිවිභත්තභොගී as
“නොබෙදා නොවළඳන්නේ” (a defensible reading); 16:3 puts the body as the subject of ජහන්ති (loose, the answer in 16:4
is the same); 63:10 names the monk of the verse (භික්ඛු) as Mahāmoggallāna. `mn-2`: the entries that write out what
the Pāli abbreviates with -පෙ- (10:2–11:2, 16:1–17:0, 24:1) were read through their expansions; nothing to note.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,816 of 5,250 entries (MN 568 of 1,089; next file `mn-2-2`, 21 entries, then `mn-2-3`, 42).

## 2026-11-13 (run 15)

Commit e4db85e (pinned). Step 1: all 21 entries of `mn-2-2` (Mahārāhulovāda, Cūḷamāluṅkya, Mahāmāluṅkya, Bhaddāli,
Laṭukikopama, Naḷakapāna, Gulissāni, Kīṭāgiri), all 42 of `mn-2-3` (Aggivacchagotta, Mahāvacchagotta, Māgandiya,
Sandaka, Mahāsakuludāyi, Samaṇamaṇḍikā, Cūḷasakuludāyi, Vekhanassa) and the first 40 of `mn-2-4` (Raṭṭhapāla,
Makhādeva, Madhura, Bodhirājakumāra to the meeting with the five monks, 51:8): 103 entries, each read in full against
its Pāli. `mn-2-2` and `mn-2-3` are finished: `batches/mn-2-2_e4db85e.tsv` (2 rows) and `batches/mn-2-3_e4db85e.tsv`
(4 rows), none unsure, nothing refused. `mn-2-4` is not finished, so no batch yet (its three findings were test-built:
nothing refused).

Confirmed (main file):
- `mn-2-2` 32:2 and 33:0 wrong-word (Laṭukikopama): අප්පොස්සුක්කා is given as “උදාසීන නොවී” (“without becoming
  indifferent”), the reverse of the word. Written “උත්සාහ රහිතව”, text-apz's own rendering elsewhere (mn-2-4 48:4,
  mn-3-3 40:4).
- `mn-2-3` 34:2 wrong-number (Sandaka): චත්තාරො අබ්රහ්මචරියවාසා without the four; “වාස සතර” as in 34:1.
- `mn-2-3` 49:5, 50:1, 50:2 pali-left-in (Mahāsakuludāyi, the fifth, seventh and eighth bases of mastery): the sentence
  තානි අභිභුය්ය ජානාමි පස්සාමීති එවංසඤ්ඤී හොති stands in Pāli, and the rest is Pāli with Sinhala endings
  (“බහිද්ධාරූපයන්”, “යම්සේ වා පන”, “ලෝහිතකවූ”, “ඕදාතවූ”). The neighbour 50:0 (the sixth base, the same Pāli with
  yellow) is sound, so the three are proposed whole on its pattern, by script (colour, simile and number changed;
  50:2 keeps its last sentence). These are whole-entry proposals, not small edits: the owner may want to look at them.
- `mn-2-4` 49:4 and 50:0 clause-added (Bodhirājakumāra): the list of beings has “අයහපත් ආකාර ඇත්තාවූද” (ද්වාකාරෙ),
  which BJT's Pāli does not have in these two entries (it has ස්වාකාරෙ සුවිඤ්ඤාපයෙ only; BJT's Sinhala likewise).
  The item is taken out.
- `mn-2-4` 50:3 wrong-word: සත්තාහකාලකතො is “කළුරිය කොට සතක් විය” in both places; written “සතියක් විය”.

Unsure: none.

Left alone: `mn-2-2` 27:3 and 28:0 cut the passage on the one-eyed man at another place than the Pāli entries do
(the simile stands in 28:0; nothing lost, as dn-1-3 61:0); 33:1 leaves out න පරමරූපං throughout (an epithet).
`mn-2-3` 23:3 has no word for සුභාසිතං; 71:2 “උදාන් ඇසුවේය” (a misprint for ඇනුවේය); 75:4, the uddāna, names nine
suttas and says ten (uddāna key words are outside the brief). `mn-2-4` 49:4 also has a bracketed “(විරුද්ධ වූ)”
before පරලොව (a gloss, left); 50:5 ends “රාජකුමාරය, මා දකින ලද්දේය.” where the Pāli sentence runs on into 51:0.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,713 of 5,250 entries (MN 465 of 1,089; next file `mn-2-4`, 73 of its 113 entries still to read).

## 2026-11-13 (run 16)

Commit e4db85e (pinned). Step 1: the last 73 entries of `mn-2-4` (Bodhirājakumāra from the five monks' reply, 52:0;
Aṅgulimāla, Piyajātika, Dhammacetiya, Kaṇṇakatthala and the vagga's uddāna) and all 41 of `mn-2-5` (Brahmāyu, Sela,
Assalāyana, Ghoṭamukha, Caṅkī, Esukārī, Dhanañjāni, Vāseṭṭha, Subha, Saṅgārava): 114 entries, each read in full
against its Pāli. Both files are finished: `batches/mn-2-4_e4db85e.tsv` (13 rows, with the three of run 15) and
`batches/mn-2-5_e4db85e.tsv` (1 row), none unsure, nothing refused.

Confirmed (main file):
- `mn-2-4` 79:2, 79:3, 79:4, 80:0, 80:1 moved (Kaṇṇakatthala, the opening): the Sinhala stands one entry late against
  the Pāli. The Pāli of 79:2 also holds the man's going to the Blessed One and his message, which the Sinhala gives in
  79:3; so the sisters' request (Pāli 79:3) stands in 79:4, the king's visit (Pāli 79:4) in 80:0, and the king's
  account (Pāli 80:0) in 80:1 before that entry's own one sentence (සුඛිනියො හොන්තු …). Proposed by script, no word
  changed: 79:2 = 79:2 + 79:3; 79:3 = 79:4; 79:4 = 80:0; 80:0 = 80:1 without its last sentence; 80:1 = that sentence.
  79:3 is not on the step 1 list (0.94 de Zoysa); it was read in full for this. **The five rows belong together: the
  owner may want to say so in the issue.**
- `mn-2-4` 52:1 wrong-number (Bodhirājakumāra): the Pāli has two monks taught while three go for alms, then three
  taught while two go; the entry has the two cases the other way round (mn-1-3, the same passage, has the Pāli's
  order). The numbers are exchanged; “නොබෝ කලකින්ම” added for න චිරස්සෙව, which the last sentence leaves out.
- `mn-2-4` 65:1 and 65:3 pali-left-in (Piyajātika): “සා” (she) and “ඛිත්තචිත්තව” stand in the Sinhala; written
  “ඕ තොමෝ” and “පෙරළුණු සිත් ඇතිව”, the wording of 65:2 and 65:4. 65:3 is not on the step 1 list (0.96 de Zoysa);
  read in full because it has the same word.
- `mn-2-4` 81:2 clause-missing (Kaṇṇakatthala): after “භගවා ආහ” the Pāli repeats the statement (නත්ථි සො සමණො වා
  බ්රාහ්මණො වා … නෙතං ඨානං විජ්ජතී); the Sinhala leaves it out with no mark. Added in the words of 81:1.
- `mn-2-4` 83:1 wrong-person (Kaṇṇakatthala, Viḍūḍabha's question): the bracket “(ඒ අනාගාමී දෙවියන් විසින්)” makes
  the gods who do not return the ones who remove; in the Pāli the gods with affliction (තෙ දෙවා) would remove those
  without (තෙ දෙවෙ), as the entry's own 84:2 has it. The bracket is written “(ඒ ව්‍යාපාද සහිත දෙවියන් විසින්)”.
- `mn-2-5` 6:1 pali-left-in (Brahmāyu's message): the clause “තිණ්ණං වෙදානං පාරගූ … අනවයො” stands in Pāli.
  Translated in the words of 0:3 (the same clause about the same brahmin), put in the sentence's form; “ලොකායන” and
  “ලක්ෂන” of 0:3 written ලොකායත, ලක්ෂණ.

Unsure: none.

Left alone:
- `mn-2-4` 66:0, 66:4, 66:5, 66:9, 66:14, 67:0, 67:1, 67:4, 67:5, 67:9, 67:10, 67:11 (Piyajātika): the stock list
  සොකපරිදෙවදුක්ඛදොමනස්සුපායාසා is given with four members, no උපායාස (the other entries of the sutta have five).
  One of several near-synonyms in a stock list, left alone as mn-1-4 41:0 was. **A doubt for the owner:** twelve
  entries in a row; if the maintainer wants list members restored, these are a one-word edit each.
- `mn-2-4` 52:0 gives the monks' second and third speeches and the second answer as “එසේම කීවාහ / කීමි” where the
  Pāli writes them out (a shortened repetition); 63:4 has “ඒ එසේමය” twice; 83:3 glosses චාවෙතුං as “(මරවීමට)”;
  65:2 (not on the list) has its words out of order (“දෙයින් උපදනාහුය, ප්‍රිය යන”), a misprint.
- `mn-2-5` 3:1–3:3 (and the other marks of the page) add “මෙයද … මහා පුරුෂ ලක්ෂණයෙකි” after each mark, which the
  Pāli of the Brahmāyu sutta does not have (true of each mark, nothing said wrongly). 18:3, 18:6, 19:2, 20:3, 20:6
  (Assalāyana) give කිඤ්චාපි භවං ගොතමො එවමාහ as a question, “කිසියම් කරුණක් නිසා … කීසේක්ද?”, followed by
  “එසේ වී නමුදු”; 19:6 has it right (“මෙසේ කියන සේක් නමුදු”). A wrong construal of කිඤ්චාපි that leaves the
  sense of the reply standing; not sent. **The owner may want to ask the maintainer whether he wants these five.**
  49:4 gives “...” where the Pāli has a few words and then -පෙ- (both abbreviate); 56:0 and 56:2 have no word for
  සහෙතුකා; 28:2 is hard to follow but has every clause.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,599 of 5,250 entries (MN 351 of 1,089; next file `mn-3`, 48 entries, then `mn-3-2`, 113).

## 2026-11-13 (run 17)

Commit e4db85e (pinned). Step 1: all 48 entries of `mn-3` (Devadaha, Pañcattaya, Sāmagāma, Sunakkhatta,
Gaṇakamoggallāna, Gopakamoggallāna, Mahāpuṇṇama and the vagga's uddāna) and the first 48 of `mn-3-2` (Chabbisodhana,
Sappurisa, Sevitabbāsevitabba to 28:4): 96 entries, each read in full against its Pāli. `mn-3` is finished:
`batches/mn-3_e4db85e.tsv` (3 rows), none unsure, nothing refused. `mn-3-2` is not finished, so no batch yet (its four
findings were test-built: nothing refused).

Confirmed (main file):
- `mn-3` 15:0 clause-missing (Pañcattaya): the first case (රූපිං … සඤ්ඤිං අත්තානං පඤ්ඤාපෙන්ති) breaks off after
  “මරණින් මතු නිත්‍යවූ,” and runs into the second. The missing words “සංඥාවෙන් යුක්තවූ ආත්මය හෝ පණවත්. ඒ” are
  added, in the entry's own words for the next case.
- `mn-3` 58:2 clause-missing (Mahāpuṇṇama, the aggregates): the Pāli writes the definition out for feeling,
  perception and formations; the Sinhala gives “...” for අජ්ඣත්තං වා … සන්තිකෙ වා in all three. Filled by script
  with the entry's own words for form and consciousness.
- `mn-3` 59:1 clause-missing (Mahāpuṇṇama, no identity view): the Pāli writes the four ways out for feeling,
  perception and formations; the Sinhala gives the first way and “...”. Filled by script on the pattern of the
  entry's own sentence for consciousness. (58:2 and 59:1 follow the rule of `CLAUDE.md` and dn-3 59:0, 62:0: “...”
  where the Pāli has no -පෙ-. **They are fill-ins of a repetition, not new sense: the owner may want to look.**)
- `mn-3-2` 6:0 wrong-person (Chabbisodhana): the Blessed One's words to the monks (තස්ස භික්ඛවෙ) open with
  “ඇවැත්නි”; written “මහණෙනි”, as 4:5 has it. The same word opens 5:1 and 6:1, which are not on the step 1 list
  (de Zoysa's own text); a row is given for each with the one-word edit, their openings read against the Pāli, the
  rest of those two entries not read.
- `mn-3-2` 23:4 clause-missing (Sevitabbāsevitabba, the arising of mind): the unwholesome list has greed and ill will
  but no විහෙසා; the wholesome half of the entry has all three. “විහෙසා සහිත වූ” added.

Unsure: none.

Left alone: `mn-3` 10:2 has no word for අබ්යාසෙක (an epithet); 15:0 gives පරිත්තසඤ්ඤිං as “හීන සංඥා”; 60:1 has no
word for අවිද්වා and gives ඨානං … විජ්ජති යං … මඤ්ඤෙය්ය as a plain statement; 59:3, 59:5, 60:13 abbreviate where
the Pāli does. `mn-3-2` 6:0 has the paragraph number “101.” in the middle of the entry and writes out the ear's
section, which the Pāli abbreviates; 18:1 writes out the witness's four answers where BJT's Pāli has two; 28:1 has
“වදාරණ ලදී” in the Blessed One's own mouth (style).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,503 of 5,250 entries (MN 255 of 1,089; next file `mn-3-2`, 65 of its 113 entries still to read,
then `mn-3-3`, 64).

## 2026-11-13 (run 18)

Commit e4db85e (pinned). Step 1: the last 65 entries of `mn-3-2` (Anupada's end, Mahācattārīsaka, Ānāpānasati,
Kāyagatāsati, Saṅkhārupapatti) and the first 40 of `mn-3-3` (Mahāsuññata 9:1, Acchariyabbhuta, Bakkula, Dantabhūmi,
Bhūmija, Anuruddha, Upakkilesa to 42:9): 105 entries, each read in full against its Pāli. `mn-3-2` is finished:
`batches/mn-3-2_e4db85e.tsv` (7 rows, with the four of run 17), none unsure, nothing refused. `mn-3-3` is not
finished, so no batch yet (its two findings were test-built: nothing refused).

Confirmed (main file):
- `mn-3-2` 51:0, 51:1, 51:2 clause-added (Ānāpānasati, the tranquillity, concentration and equanimity factors): each
  entry holds its text three times where the Pāli entry has the passage once (the entry before them, 50:3, abbreviates
  feelings, mind and mental objects with -පෙ-, as the Pāli does; the three copies look like de Zoysa's written-out
  repetitions gathered into one entry). One copy is kept, cut out by script. In 51:0 and 51:2 none of the three copies
  has the clause යස්මිං සමයෙ භික්ඛවෙ … (“මහණෙනි, යම් කලක … ද”), which the neighbouring entries have; it is added
  in the entry's own words. 51:1 is its first copy unchanged. **A new kind of row (a tripled entry): the owner may
  want to look.**
- `mn-3-3` 23:1 pali-left-in, with 24:0 clause-missing (Dantabhūmi, the elephant's training; a pair): the sentence
  තමෙනං හත්ථිදමකො උත්තරිං කාරණං කාරෙති stands in Pāli at its first occurrence; written as the entry itself has it
  two lines on. And the entry ends with the head, ears, tusks, tail and trunk the elephant does not move, which in
  BJT open the next Pāli entry (24:0, across the page break), whose Sinhala lacks them; moved word for word. 24:0 is
  not on the step 1 list (it was read in full for this).

Unsure: none.

Left alone:
- `mn-3-3` 23:1 and 24:0 call the elephant “රජුගේ හස්තියා / රජුගේ ඇතා” four times where BJT's Pāli has ආරඤ්ඤකො
  නාගො (BJT's footnote gives the other reading, රඤ්ඤො නාගො; BJT's Sinhala has ආරණ්‍යකනාග). A recorded variant
  reading, de Zoysa's; not sent. **A doubt for the owner: by "the BJT Pāli decides" these could be rows.**
- `mn-3-2` 51:1 has no word for සුඛිනො; 42:5 gives සෙඛො as “සේඛ ප්‍රතිපදාව” (the footnote's reading); 63:3 keeps
  the -පෙ- before “දීර්ඝායුෂ” as the Pāli has it; 64:3 and 64:4 write out what the Pāli abbreviates.
- `mn-3-3` 31:1 gives යොනි හෙසා as “නුවණින් කරන උත්සාහයක්” (loose); 26:2 and 26:3 write out what the Pāli
  abbreviates; 42:3 addresses the one park keeper as “ඇවැත්නි”.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,398 of 5,250 entries (MN 150 of 1,089; next file `mn-3-3`, 24 of its 64 entries still to read,
then `mn-3-4`, 42, and `mn-3-5`, 84).

## 2026-11-13 (run 19) — the Majjhima's step 1 is finished

Commit e4db85e (pinned). Step 1: the last 24 entries of `mn-3-3` (Upakkilesa's end, Bālapaṇḍita, Devadūta), all 42 of
`mn-3-4` (Bhaddekaratta to Dakkhiṇāvibhaṅga) and all 84 of `mn-3-5` (Anāthapiṇḍikovāda to Indriyabhāvanā): 150
entries, each read in full against its Pāli (more than the usual 100: the entries of `mn-3-5` are short, and
finishing the file finished the Nikāya). The three files' batches are built, nothing refused.

**The Majjhima's batch is ready to post:** `batches/mn-step1_e4db85e.tsv` (69 rows), `mn-step1_e4db85e_unsure.tsv`
(3 rows), issue text `batches/mn-step1_ISSUE.md`. 1,089 entries read in fifteen files.

Confirmed (main file):
- `mn-3-3` 61:0 clause-missing (Devadūta, the first messenger): the infant is described in the Pāli as lying on its
  back in its own urine and excrement (මන්දං උත්තානසෙය්යකං සකෙ මුත්තකරීසෙ පලිපන්නං සෙමානං); the Sinhala has only
  “ළදරුවෙකු” (de Zoysa's archived text abbreviates here). Added in the words text-apz uses for the same Pāli
  elsewhere (mn-2 47:0, an-10-2 99:3); the last three words (“ගැලී වැතිර සිටින”) are newly written. In the same
  row: තථා කරිස්සන්ති (they will do) stands as Yama's “කරන්නෙමි”; written “කරන්නාහුය”, as 61:1 has it.
- `mn-3-4` 64:0 pali-left-in (Dakkhiṇāvibhaṅga): the last sentence, ඉමා ඛො ආනන්ද, චතස්සො දක්ඛිණා විසුද්ධියොති,
  stands in Pāli; written in the words of 63:3.
- `mn-3-5` 24:10 clause-missing (Cūḷarāhulovāda): “එය මාගේය” (එතං මම) is missing from the three; added as 24:4 and
  24:16 have it.
- `mn-3-5` 30:3, 30:4, 31:0 clause-missing (Chachakka): the Pāli writes “… සමනුපස්සති” out for each item; the
  Sinhala names the items with “...” between them and gives the sentence once. Filled by script with the entry's own
  sentence. (The same kind as mn-3 58:2, 59:1 of run 17: **fill-ins of a repetition, not new sense; the issue text
  says he may skip them. The owner may want to look.**)
- `mn-3-5` 31:1, 31:3, 32:0 pali-left-in (Chachakka): “දිට්ඨෙව ධම්මෙ (මේ ආත්මයෙහි ම)”; the Pāli taken out, the
  translation kept, as 31:2 has the same sentence.

Unsure:
- `mn-3-3` 60:6 clause-missing (Devadūta): of the five failings the Sinhala has four; for අසාමඤ්ඤො අබ්රහ්මඤ්ඤො it
  has the one phrase “උතුමන් නොහඳුනන්නෙක” (de Zoysa's), which names neither ascetics nor brahmins. A proposal on the
  pattern of the entry's own words for mother and father. Unsure because the one phrase may be meant to cover both.

Left alone:
- `mn-3-3` 43:8 and 44:0 give the Bodhisatta's “I perceived” with the plural verb of the monks' sentence before it
  (“මම ද … හඳුනා ගනිමු”, “(දකිමු)”); the subject මම is stated, so grammar, not sense. 57:4 opens with a sentence
  the BJT Pāli entry does not have (“ඍද්ධි සතරකින්ද යුක්තවූයේ වෙයි”) and has the paragraph number “259.” in the
  middle; 52:2 has no word for පුබ්බෙ.
- `mn-3-4` 5:0 gives ධම්මියා කථාය as “භද්දෙකරත්ත ධර්ම කථාවක්” (loose); 3:11 writes out what the Pāli abbreviates.
- `mn-3-5` 27:3 is the stock rendering already asked about in the DN issue (ධම්මං … දෙසිස්සාමි … බ්රහ්මචරියං
  පකාසිස්සාමි as “බ්‍රහ්මචර්යාව දේශනා කරන්නෙමි. ප්‍රකාශ කරන්නෙමි”, no “Dhamma” of its own); not multiplied.
  1:6 writes out what the Pāli abbreviates; 31:1–32:0 give අනුසෙති as “වැඩෙයි”.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,248 of 5,250 entries (DN and MN finished; next the Saṃyutta, 1,625 entries, first file `sn-1`, 33).

## 2026-11-13 (run 20) — the Saṃyutta begun

Commit e4db85e (pinned). Step 1: all 33 entries of `sn-1` (Devatā and Devaputta saṃyuttas) and the first 70 of
`sn-1-3` (Kosala saṃyutta to the Māra saṃyutta's daughters, up to 49:4): 103 entries, each read in full against its
Pāli. `sn-1`'s batch is built (`batches/sn-1_e4db85e.tsv`, 3 rows), nothing refused; the four findings of `sn-1-3`
were tried through the batch script (nothing refused) and its batch waits for the file's end.

Confirmed (main file):
- `sn-1` 47:8 pali-left-in (Suriya): “ගාථාහි අජ්ඣභාසි” stands in Pāli at the sentence's end; written “ගාථාවලින්
  වදාළහ”, as the twin sentence of the Candima sutta has it.
- `sn-1` 50:17 clause-missing (Kakudha): මං එකමාසීනං (me, sitting alone) is only “මා”; added in the words of the
  question at 50:15 (“හුදෙකලාව ඉන්නා”).
- `sn-1` 53:8 clause-missing (Siva): the first of the verse's two opening clauses, සබ්භිරෙව සමාසෙථ, is missing;
  the sutta's five other verses have both. Added in their words.
- `sn-1-3` 14:11 wrong-word (Dhītu): සස්සුදෙවා (she who holds her mother-in-law as a deity) is turned round,
  “නැන්දම්මාට දේවතාවියක වැනි වූ”; written “නැන්දම්මා දෙවියක සේ සලකන” (newly written words).
- `sn-1-3` 16:2 pali-left-in (Kalyāṇamitta): the particle ඛො in “මෙසේ ඛො භික්ෂුව”; taken out.
- `sn-1-3` 19:5 wrong-number (Dutiya-aputtaka): සතං සතසහස්සානං, a hundred hundred-thousands, stands as
  “ලක්ෂයකි”; written “සිය ලක්ෂයකි” on the pattern of 18:0 (“අසූ ලක්ෂයකි”).
- `sn-1-3` 49:1 wrong-number (Māradhītu): the hundred of සකිං විජාතවණ්ණසතං is missing; added as 49:3 and 49:5
  have it (“වෙස් සියය බැගින්”).

Unsure: none.

Left alone:
- `sn-1-3` 14:11, the same verse: සෙය්යා පොස is given as “පිරිමියාටත් වඩා උතුම්” (better than a man), the other
  recorded reading (posā); BJT's Sinhala takes පොස as “nourish (her)”. Not sent, as the elephant of `mn-3-3` in
  run 18. **The same doubt for the owner: by "the BJT Pāli decides" this could be a row.**
- `sn-1-3` 49:0 has “...පෙ...” for එකසතං එකසතං (a hundred each), two words the Pāli writes out here and
  abbreviates in the entries after it; the hundred itself is there. 15:3 has no word for the first එකමන්තං නිසීදි.
  18:0 and 19:5 give බිලඞ්ගදුතියං as “මිරිස් හොදි සමග” (BJT: කාඩි) and අතිහරිත්වා ආගච්ඡාමි as “ගෙන එමි” (loose).
- `sn-1` 4:2, `sn-1-3` 26:1, 38:5, 41:0, 44:4 write out what the Pāli abbreviates.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,145 of 5,250 entries (SN 1,522 of 1,625; next file `sn-1-3`, 66 of its 136 entries still to read,
then `sn-1-7`, 41).

## 2026-11-13 (run 21) — `sn-1-3` and `sn-1-7` finished

Commit e4db85e (pinned). Step 1: the last 66 entries of `sn-1-3` (Māra's daughters' end, the Bhikkhunī and Brahma
saṃyuttas, 49:5 to 77:13) and all 41 of `sn-1-7` (Brāhmaṇa, Vaṅgīsa, Vana, Yakkha and Sakka saṃyuttas): 107 entries,
each read in full against its Pāli. Both files' batches are built (`batches/sn-1-3_e4db85e.tsv`, 7 rows;
`batches/sn-1-7_e4db85e.tsv`, no rows), nothing refused.

Confirmed (main file):
- `sn-1-3` 55:16 pali-left-in (Cālā): the verse's last quarter stands in Pāli, “යො මං සච්චෙ නිවෙසයි”, with its
  translation in brackets after it; the Pāli taken out, the translation kept.
- `sn-1-3` 68:9 wrong-word (Pamāda): තයා ච … මයා ච, “than you and than me”, has මයා as an agent (“තොපටත් වඩා මා
  විසින් ද”); written “තොපටත් මටත් වඩා”.
- `sn-1-3` 71:4 clause-missing (Kokālika): of the eight sizes of the boils the jujube fruit (කොලමත්තියො) is missing
  between the jujube stone and the myrobalan; added in the words of the same passage in `an-10-2` (“ඩෙබර ගෙඩි පමණ”).

Unsure: none.

Left alone:
- `sn-1-3` 65:11 ends with a sentence the Pāli does not have, “(එහි) මෙලොව උපදින (සත්වයෝ) නැතැයි කියායි”, after the
  brahmā's view is given in full; read as a restatement of the view (no one comes to this world), so no row. **The
  owner may want to look: if it is read as a second, different view, it is an added clause.**
- `sn-1-3` 72:0 and 72:1 address the one monk (භික්ඛු) as “මහණෙනි”, twelve times in all; number of address only, as
  the park keeper of `mn-3-4` 42:3. 67:3 lacks a closing quotation mark.
- `sn-1-7` 18:0 gives විසූකං as “විශූක දර්ශනයකි” and 18:9 makes the Buddha “ලෝකාධිපතියා” in a garbled clause
  (de Zoysa's wording in both; the verses' other clauses are there); 20:5 reads විස්සං as “මුළු” (all), the other
  recorded reading (BJT: foul); 18:5 has the Pāli word “(කට්ඨහාරකා)” in brackets after its own translation, a gloss,
  not text left untranslated.
- The uddāna verses (51:4, 58:13, 72:8, 77:13; `sn-1-7` 10:5, 22:4, 33:1, 40:7, 49:3, 60:4, 67:14, 71:1, 71:3) are
  key words and stay as they are. `sn-1-3` 49:5, 49:7, 71:2, 71:3 write out what the Pāli abbreviates.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 3,038 of 5,250 entries (SN: `tools/work.py list 1 sn` gives 1,630 entries, 1,420 to read; next file
`sn-2`, 46).

## 2026-11-13 (run 22) — `sn-2`, `sn-2-1-5` and `sn-2-2` finished

Commit e4db85e (pinned). Step 1: all 46 entries of `sn-2` (Nidāna saṃyutta, Buddha and Āhāra vaggas to the
Dasabala vagga and the ñāṇavatthu suttas), all 30 of `sn-2-1-5` (Gahapati vagga to the Abhisamaya saṃyutta) and all
32 of `sn-2-2` (Dhātu, Anamatagga and Kassapa saṃyuttas): 108 entries, each read in full against its Pāli. The three
files' batches are built (`batches/sn-2_e4db85e.tsv`, 3 rows; `batches/sn-2-1-5_e4db85e.tsv`, no rows;
`batches/sn-2-2_e4db85e.tsv`, 2 rows), nothing refused.

Confirmed (main file):
- `sn-2` 15:9 wrong-word (Acela Kassapa): Kassapa's four questions on suffering (සයංකතං දුක්ඛං …) stand as
  “සැප දුක්” (pleasure and pain, the next sutta's wording); entries 3–6 of the page and the rest of the entry have
  “දුක”. Changed in the four places.
- `sn-2` 19:7 pali-left-in (Paccaya): the links from භවපච්චයා ජාති to සඞ්ඛාරපච්චයා විඤ්ඤාණං stand in Pāli
  (“භවය පච්චයා ජාති … සඞ්ඛාර පච්චයා විඤ්ඤාණං”) with no translation; written in the words of 13:6 of the same file.
  The last link, translated in the sentence that follows, is not repeated; the quoted formula with its gloss at the
  end is kept (as in 19:6, where the formula is translated first and then quoted).
- `sn-2` 20:0 clause-missing (Paccaya): the Pāli writes the sentence out for birth and for existence; the Sinhala
  has “ජාතිය අනිත්‍යය... භවය අනිත්‍යය...”. Filled with the entry's own words for ageing-and-death.
- `sn-2-2` 52:0 wrong-person (Jhānābhiññā): Kassapa's half ends “දැනගනිමි” (I know) for පජානාති; “දැනගනියි”.
- `sn-2-2` 56:7 pali-left-in (Cīvara): Kassapa's words “ඉධ භන්තෙ, භගවා නිසීදතු, යං මමස්ස දීඝරත්තං හිතාය
  සුඛායා”ති stand untranslated; translated (newly written words).

Unsure: none.

Left alone:
- `sn-2` 18:5 opens with the sutta's setting (“එක්කලෙක … වදාළ සේක”), which the Pāli gives in the entry before it
  as සාවත්ථියං only; an opening written out, no row. 13:6 ends with a closing quotation mark and “කියායි” without
  an opening mark.
- `sn-2` 19:1 keeps “අධිප්පායක්, නානාකරණයක්” as Sinhala-ised terms in a clumsy sentence (model-written); every
  clause of the Pāli is there. 16:0 and 17:6 quote the Pāli formula and gloss it in brackets.
- `sn-2-1-5` 57:5: සත්ත මුග්ගමත්තියො පාසාණසක්ඛරා (seven pebbles the size of mung beans) is “මුංඇට හතක් පමණවූ
  ගල්කැට” (pebbles the size of seven mung beans); the seven is there, wording only.
- `sn-2-2` 3:7: BJT's Pāli has “නො ධම්මපරිළාහං පටිච්ච උප්පජ්ජති ධම්මපරියෙසනා” where the series needs the
  positive sentence (a slip in the Pāli entry); the Sinhala has the positive, as the sense requires. No row.
- Many entries of these three files write out what the Pāli abbreviates (the twelve links, the seven days and nights,
  the Dhātu saṃyutta's triads in three times): not errors.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,930 of 5,250 entries (SN: 1,312 of 1,630 to read; next file `sn-2-5`, 67).

## 2026-11-13 (run 23) — `sn-2-5` and `sn-3` finished

Commit e4db85e (pinned). Step 1: all 67 entries of `sn-2-5` (Lābhasakkāra, Rāhula, Lakkhaṇa, Opamma and Bhikkhu
saṃyuttas) and all 45 of `sn-3` (Khandha saṃyutta, Nakulapitu vagga to the Bhāra vagga's neighbours, pages 4–45):
112 entries, each read in full against its Pāli. The long Rāhula entries (16:13–21:9), which write out six or five
repetitions of one frame, were read sentence by sentence with the repeated sentences counted by script (each frame
complete, each item named once). The two files' batches are built (`batches/sn-2-5_e4db85e.tsv`, 5 rows;
`batches/sn-3_e4db85e.tsv`, 7 rows), nothing refused.

Confirmed (main file):
- `sn-2-5` 0:10 clause-missing (Dāruṇa): කටුකො ඵරුසො stands as “දරුණුය...”; filled with the file's own words
  (“දරුණුය, කටුකය, ඵරුෂය”, 33 times in the file). In the same entry එවං සික්ඛිතබ්බං stands as “නික්මිය යුතු”
  (should leave); “හික්මිය යුතු”, as the entry's last sentence has it.
- `sn-2-5` 6:4 pali-left-in: “න චායමායස්මා - (මේ ආයුෂ්මත්තෙම -)”; the Pāli taken out, the translation kept.
- `sn-2-5` 42:5 clause-missing (Nava): the two descriptions of the four jhānas, ආභිචෙතසිකානං
  දිට්ඨධම්මසුඛවිහාරානං, are not translated; added (newly written words, on the pattern of an-11 and an-5-4).
- `sn-2-5` 43:3 pali-left-in (Sujāta): “දූරතොව (දුරදීම) ආගච්ඡන්තං (එනු)”; the Pāli taken out.
- `sn-2-5` 43:5 pali-left-in (Sujāta, verse): “විප්පමුත්තො (…), විසඤ්ඤුත්තො (…)”; the Pāli taken out.
- `sn-3` 8:1 negation-reversed (Hāliddikāni): ගිහීහි අසංසට්ඨො is “ගිහියන් හා මිශ්‍රව” (mixed with householders);
  “මිශ්‍ර නොවී”.
- `sn-3` 11:3, 11:4, 11:5 pali-left-in (Samādhi): the Pāli pronoun සා stands in “… වේද, සා නිරුද්ධ වෙයි”;
  “එය”, as 13:0 has the same sentence. (A fourth, 11:6, on consciousness, is outside step 1: 92.5% of its words are
  de Zoysa's, above the 90% line; the owner may want to add it by hand.)
- `sn-3` 13:6 pali-left-in (Upādāparitassanā): the verb හොති stands in the Sinhala sentence; taken out.
- `sn-3` 15:2 negation-reversed (Upādāparitassanā): අනුපාදා අපරිතස්සනා හොති is “අනුපාදා අපරිතස්සනාව (… භය
  ඇතිවීමක්) නොවෙයි” (does not come to be); put as the question in 14:3 has it.
- `sn-3` 26:2 wrong-word (Assāda): the written-out sentence on perception ends “සත්වයන් සංස්කාරයන්හි ඇලෙත්”
  (cling to formations); “සත්වයෝ සංඥාවෙහි ඇලෙත්”.

Unsure: none.

Left alone:
- `sn-2-5` 41:4 gives ආකඞ්ඛමානො as “ආකංඛමාන වන්නේ නම්”, and 43:4 keeps “අභිරූපද, දස්සනීයද, පාසාදිකද” and 42:5
  “උජ්ඣායනය (නුගුණ කියන්නට)”: Sinhala-ised terms (de Zoysa's), not Pāli sentences left in; as the terms of `sn-2`
  19:1 in run 22. **A doubt about the rules:** if the maintainer counts such Sinhala-ised words as Pāli left in,
  these are three more rows.
- `sn-2-5` 6:5 writes out in brackets what the Pāli abbreviates; 29:9 gives the Buddha's sentences in another
  order, all there; 19:10 gives the plural රූපා … ධම්මා in the singular.
- `sn-3` 9:8 gives චෙතසො අධිට්ඨානාභිනිවෙසානුසයා loosely (“අකුසල් සිතට ස්ථානවූ අනුසයයෝ”); 26:3 writes the
  sentence out for feeling, perception and formations where BJT's Pāli entry has consciousness only (the fuller
  text, no row); 43:8–43:13 give one answer three times for the three aggregates of the question.
- The uddāna verses (`sn-2-5` 6:16, 48:4) stay as they are.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,818 of 5,250 entries (SN: 1,200 of 1,630 to read; next file `sn-3-1-2`, 55).

## 2026-11-13 (run 24) — `sn-3-1-2` and `sn-3-1-3` finished

Commit e4db85e (pinned). Step 1: all 55 entries of `sn-3-1-2` (Khandha saṃyutta, Upaya vagga to the Puppha vagga,
pages 4–83) and all 35 of `sn-3-1-3` (Anta vagga to the Diṭṭhi vagga, pages 2–32): 90 entries, each read in full
against its Pāli. The two files' batches are built (`batches/sn-3-1-2_e4db85e.tsv`, 2 rows;
`batches/sn-3-1-3_e4db85e.tsv`, no rows), nothing refused. The run stopped at the file's end: the next file,
`sn-3-2`, has 106 entries.

Confirmed (main file):
- `sn-3-1-2` 7:6 pali-left-in (Sattaṭṭhāna): two clauses stand in Pāli in the Sinhala sentence, “රූපස්ස අස්සාදං
  පජානාති, රූපස්ස ආදීනවං පජානාති”; put as the same sutta has them for feeling (“… ආස්වාදය දනී, … ආදීනව දනී”).
- `sn-3-1-2` 49:6 clause-missing (Yamaka; a list item): in the sentence on consciousness, which the Pāli writes
  out, හීනං වා is missing (“සියුම්වූ හෝ උතුම්වූ හෝ”); the entry's sentences on form, feeling and formations have
  “හීනවූ හෝ”. Added.

Unsure: none.

Left alone:
- `sn-3-1-2` 25:8 glosses the seven good qualities as “සද්ධා, හිරි, ඔතප්ප, බාහුසච්ච විරිය, සති, සඤ්ඤා” (the last
  should be paññā, and there is no comma after බාහුසච්ච): a gloss in brackets that the Pāli entry does not have
  (de Zoysa's), so no row; the owner may want to mention it.
- `sn-3-1-2` 27:5 has no word for විප්පමුත්තස්ස and 83:3 none for භික්ඛුනා (single words; the sentences stand);
  83:3's first sentence is clumsy (“නොමදකිමි”), every clause there. 68:4 leaves ලොකෙ out of the second of the
  two twin sentences. 41:7 and 41:8 add a bracketed remark that the answer is the same for the other aggregates.
- `sn-3-1-2` 45:6: BJT's Pāli entry has no විගතඡන්දස්ස (a slip; the twin entries have it); the Sinhala has it.
- `sn-3-1-3` 2:4 gives සක්කායනිරොධගාමිනී පටිපදා as “තමා නැති කිරීමේ මාර්ගය” (de Zoysa's wording for sakkāya):
  loose, no row.
- Most entries of both files write out for the four other aggregates what the Pāli abbreviates (the questions on
  permanence, 16 entries of `sn-3-1-3` alone): not errors; each was counted (four aggregates, each once).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,728 of 5,250 entries (SN: 1,110 of 1,630 to read; next file `sn-3-2`, 106).

## 2026-11-13 (run 25) — `sn-3-2` finished

Commit e4db85e (pinned). Step 1: all 106 entries of `sn-3-2` (the Rādha, Diṭṭhi, Okkanti, Uppāda and Kilesa
saṃyuttas, pages 2–62), each read in full against its Pāli. The file's batch is built
(`batches/sn-3-2_e4db85e.tsv`, 14 rows; no unsure rows), nothing refused. The run stopped at the file's end: the
next file, `sn-3-7`, has 210 entries.

Confirmed (main file):
- `sn-3-2` 10:6 pali-left-in (Rādha, Māra): the closing sentence ends in Pāli, “… ඡන්දය පහාතබ්බො, රාගො
  පහාතබ්බො, ඡන්දරාගො පහාතබ්බො”; put in the entry's own words for the same clause.
- `sn-3-2` 25:2 wrong-word (Diṭṭhi): the Pāli entry is the answer අනිච්චං භන්තෙ; the first of the entry's four
  answers reads “ස්වාමීනි දුකය”. Put like the other three (“ස්වාමීනි, අනිත්‍යය”).
- `sn-3-2` 29:4 pali-left-in (Mahādiṭṭhi): twice “… සුඛදුක්ඛං පලෙන්තී’ති එවං දිට්ඨි උප්පජ්ජති”; put in the
  words of 29:2 (“සුවදුක් කෙළවර කරති’ යන මේ දෘෂ්ටිය උපදියි”).
- `sn-3-2` 31:4 pali-left-in: the last sentence, අයං වුච්චති භික්ඛවෙ, අරියසාවකො සොතාපන්නො … සම්බොධිපරායනොති,
  stands in Pāli; put in the words the same file has for it at the end of other suttas of the saṃyutta.
- `sn-3-2` 39:5 clause-missing (Vāta): the Pāli writes out the last clause of the monks' answer, භගවතො සුත්වා
  භික්ඛූ ධාරෙස්සන්ති; the Sinhala stops before it. Added in text-apz's own words for it.
- `sn-3-2` 43:11 pali-left-in: “විඤ්ඤාණය නිත්‍ය වා අනිත්‍ය වා”; put as 43:8 has the question for form.
- `sn-3-2` 39:4, 39:6, 39:11, 39:13, 39:15, 39:17, 45:0, 45:5 pali-left-in: the Pāli quotation particle ති after
  the closing quotation mark (“… සිටියේය”ති”, “… ආත්මය වෙයි”ති”); written “යි”, as 40:3 and 42:23 end the same
  kind of sentence. (A stray particle, as the “ඛො” of `dn-2` 17:0 and `sn-1-3` 16:2 and the “’න්ති” of run 12;
  eight small rows of one kind, which the owner may want to say in a line when he posts SN.)

Unsure: none.

Left alone:
- `sn-3-2` 16:4 (and the entries like it) writes out the opening “මා විසින් මෙසේ අසනලදී … ජේතවනාරාමයෙහි” where
  the Pāli has only සාවත්ථියං in the entry before: the abbreviated opening written out, no row.
- The entries of the Diṭṭhi saṃyutta that give one question or answer four or five times with “...” between
  (20:0, 21:8, 22:10, 23:15, 23:17, 25:3–25:6, 27:2, 27:4, 28:8): de Zoysa's writing-out for the five aggregates of
  what the Pāli gives once; restatements, no row (25:2 is a row only because its first answer is the wrong word).
  28:5 carries de Zoysa's paragraph numbers “[9] … [13]” inside the text.
- 23:17 and 40:14 give නො චස්සං නො ච මෙ සියා … loosely (“අතීතයෙහි නුවූයෙම්නම් දැන් නොවෙමි …”); 43:5–44:7 give
  රූපී / අරූපී as “අරමුණ” / “ධ්‍යානය” with the Pāli word in brackets (de Zoysa's reading); 10:11 and 16:10 read
  මාරධම්මො as “මාර ධර්මය” where BJT's Sinhala reads “මරණධර්ම”; 59:11–62:4 give නෙක්ඛම්මනින්නං as “ලොකොත්තර
  ධර්මයට නැඹුරු”: word choices, no row. 45:3 has the form “සංස්කාරා”.
- 39:15: BJT's Pāli entry reads තං උපාදාය (the twin entries අනුපාදාය); the Sinhala follows the entry (“එය නිසා”).
- 43:19 writes the passage out where the Pāli entry is only the instruction to expand; 41:7 and 40:23 add a little
  of the abbreviated passage. Three of the file's closing sentences on the stream-enterer (outside this step's
  list, seen while looking for wording) have no word for නියතො: a single word, left.
- The uddāna verses (45:8–45:11) stay as they are.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,622 of 5,250 entries (SN: 1,004 of 1,630 to read; next file `sn-3-7`, 210).

## 2026-11-13 (run 26) — `sn-3-7`, first 137 of 210

Commit e4db85e (pinned). Step 1: the first 137 entries of `sn-3-7` (the Sāriputta, Nāga, Supaṇṇa, Gandhabbakāya,
Valāhaka and Vacchagotta saṃyuttas, and the Jhāna saṃyutta as far as the Abhinīhāra sutta; pages 1–39, to 39:10),
each read in full against its Pāli. Most are short (the abbreviated peyyāla suttas), so the run went past 100. The
file is not finished (73 left, from 39:11), so no batch is built yet; the one finding was tried through
`work.py batch` (nothing refused) and the trial files removed.

Confirmed (main file):
- `sn-3-7` 36:16 wrong-word (Jhāna saṃyutta, Ṭhiti sutta): the Pāli pairs සමාධිකුසලො with ඨිතිකුසලො in four
  sentences. The first gives සමාධිකුසලො as “ධ්‍යානාංග දැනීමෙහි සමත්”; the other three give it as “සමාධියට
  සමවැදීමෙහි”, the file's wording for සමාපත්තිකුසලො in the sutta before (36:6–36:10), which this entry's Pāli does
  not have. Put as the first sentence has it (the second already has it in brackets).

Unsure: none.

Left alone:
- 21:9 and 24:8 give the line සාවත්ථියං as “(මේ සූත්‍ර ද පෙර සූත්‍ර මෙන් ජේතවනාරාමයේදී දේශනා කරන ලදී.)”: loose,
  nothing wrong against the Pāli, no row.
- 36:11–39:2 give the simile ගවා ඛීරං, ඛීරම්හා දධි … partly as “දෙනට වඩා කිරිද, කිරට වඩා දීද …” (“than”, where
  36:11 has “දෙනගෙන් කිරිද …”): de Zoysa's loose wording, the point of the simile stands; no row. The owner may
  want to mention it.
- 28:0, 28:5, 28:10, 29:4 give the closing sentence අයං ඛො වච්ඡ, හෙතු … with “ඊට” for the list of views the Pāli
  repeats; 1:3 and 3:3 have no word for ආගච්ඡන්තං, 3:2 none for දිවාවිහාරං, 7:15 none for එකච්චෙ, 28:0 none for
  ලොකෙ (single words). 27:11 and the entries like it give තථාගතො as “සත්ත්වතෙමේ” (BJT's Sinhala reads the same).
- 24:10: BJT's Pāli entry ends with සීතවලාහකානං (a slip for වස්සවලාහකානං); the Sinhala has වස්සවලාහක.
  35:0: the Pāli entry reads න හොති ච න ච හොති for the third of the four; the Sinhala gives the usual “is and is
  not”.
- The terms of the Jhāna saṃyutta (කල්ලිතකුසලො “සිත ශක්තිමත් කිරීමෙහි”, ආරම්මණකුසලො “කසිණාරම්මණයන්හි”,
  ගොචරකුසලො “සුදුසු කමටහන්හි හා යෝග්‍ය පිණ්ඩපාතයෙහි”, අභිනීහාරකුසලො “කර්මස්ථානය පැමිණවීමෙහි”) follow the
  commentary: word choices, no row.
- The uddāna verses (13:1, 22:5, 26:13) stay as they are.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,485 of 5,250 entries (SN: 867 of 1,630 to read; next `sn-3-7` from 39:11, 73 left).

## 2026-11-14 (run 27) — `sn-3-7` finished; `sn-4`, first 24 of 118

Commit e4db85e (pinned). Step 1: the last 73 entries of `sn-3-7` (the Jhāna saṃyutta from 39:11 to its end, with the
closing uddāna verses of the Khandhavagga, pages 39–53) and the first 24 of `sn-4` (the Saḷāyatana saṃyutta, pages
8–23, to 23:2), 97 entries, each read in full against its Pāli. `sn-3-7` is finished: its batch is built
(`batches/sn-3-7_e4db85e.tsv`, 1 row, the 36:16 of run 26; no unsure rows), nothing refused. `sn-4` is not finished
(94 left, from 23:3), so no batch for it yet.

Confirmed (main file): none in this run.

Unsure: none.

Left alone:
- `sn-3-7` 44:4: BJT's Pāli entry reads නෙව සමාධිස්මිං සප්පායකාරී හොති, න සමාධිස්මිං සමාපත්තිකුසලො where the
  sutta's second person should be “සප්පායකාරී හොති, න … සමාපත්තිකුසලො” (BJT's own Sinhala reads it so; a slip in
  the Pāli entry). The text-apz entry follows the Pāli entry as it stands (“neither”), so it says the same as 44:5.
  Right against the Pāli entry, so no row; the owner may want to mention it to the maintainer as a point in BJT's
  Pāli.
- `sn-3-7` 42:19 gives the two negated skills in the other order; 42:3, 42:12 and 43:1 write out the list
  අග්ගො ච … පවරො ච and add the abbreviated simile where the Pāli has -පෙ-: nothing wrong, no row.
- The model-written entries from 43:5 on keep the Jhāna saṃyutta's terms as terms (“සප්පායකාරී”, “ඨිති කුසල”,
  “වුට්ඨාන කුසල”, “කල්ලිත කුසල”, “සාතච්චකාරී”), as BJT's Sinhala does: technical terms, not Pāli left in.
- The uddāna verses (53:4–53:11) stay as they are; 53:8–53:10 call the vaggas “සූත්‍ර”, 53:11 keeps BJT's Pāli
  “ගන්ධ” (for Rādha): uddāna key words, no row.
- `sn-4` 17:2 gives ඉදං ඛො භික්ඛවෙ, සබ්බං අභිජානං … භබ්බො දුක්ඛක්ඛයාය loosely (“this is the dhamma fit for
  ending suffering, having known the all …”): loose wording, no row.
- `sn-4` 16:1, 16:2, 17:0 write out for flavours, tongue-consciousness and tongue-contact (and for mind) what the
  Pāli abbreviates; 20:5–20:7 read අන්ධභූතං / අද්ධභූතං as “මඩනා ලද්දේ”, as BJT's Sinhala does; 22:2 gives
  න පරිතස්සති as “ආශා නොකරන්නේය” (BJT's Sinhala: craving): not errors.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,388 of 5,250 entries (SN: 770 of 1,630 to read; next `sn-4` from 23:3, 94 left).

## 2026-11-14 (run 28) — `sn-4` finished

Commit e4db85e (pinned). Step 1: the last 94 entries of `sn-4` (the Saḷāyatana saṃyutta from the Jātidhamma vagga to
the Yogakkhemi vagga, pages 25–94), each read in full against its Pāli. `sn-4` is finished: its batch is built
(`batches/sn-4_e4db85e.tsv`, 1 row; no unsure rows), nothing refused.

Confirmed (main file):
- `sn-4` 74:3 pali-left-in (Dutiyadvaya sutta, its last paragraph): the entry opens with the whole Pāli entry left
  in (“යොපි හෙතු යොපි පච්චයො මනොසම්ඵස්සස්ස උප්පාදාය … ද්වයං පටිච්ච විඤ්ඤාණං සම්භොතීති.”) and then gives its
  translation. The Pāli is taken out, nothing else changed.

Unsure: none.

Left alone:
- Most of the file's entries write out for ear, nose, tongue, body and mind what the Pāli abbreviates with -පෙ-
  (30:4, 31:19, 37:4, 42:3–44:0, 58:0, 60:0, 61:1, 66:0, 66:2, 69:2, 89:7, 90:2, 94:10), and 58:4–58:5 shorten
  three of the six questions with “…” where the Pāli has -පෙ-: abbreviation on both sides, no row.
- 68:3 gives පටිවෙදෙසි as “ධර්මාවබෝධය කරවීය”, as BJT's Sinhala does; 45:5–46:2 give -පටිසංවෙදී as
  “දැනගන්නේ”; 56:3 adds de Zoysa's glosses in brackets: word choices, no row.
- 74:3's translation gives ඵුට්ඨො වෙදෙති, සඤ්ජානාති, චෙතෙති in the order feels, intends, perceives (all three
  there); 82:5: BJT's Pāli entry reads ඝානින්ද්රියා සංවුතස්ස, කායින්ද්රියා සංවුතස්ස, මනින්ද්රියා සංවුතස්ස (slips
  for අසංවුතස්ස in the Pāli entry); the Sinhala has “unrestrained” throughout, as the sutta requires. No row.
- The uddāna verses (32:5, 32:8, 38:9) stay as they are.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,294 of 5,250 entries (SN: 676 of 1,630 to read; next file `sn-4-1-12`, 101).

## 2026-11-14 (run 29) — `sn-4-1-12` finished

Commit e4db85e (pinned). Step 1: all 101 entries of `sn-4-1-12` (the Saḷāyatana saṃyutta from the Lokakāmaguṇa vagga
to the Āsīvisa vagga, pages 0–90), each read in full against its Pāli. `sn-4-1-12` is finished: its batch is built
(`batches/sn-4-1-12_e4db85e.tsv`, 0 rows; no unsure rows), nothing refused.

Confirmed (main file): none in this run.

Unsure: none.

Left alone:
- Most of the file's entries write out for ear, nose, tongue, body and mind (and, in the peyyāla vaggas, for each
  of the six bases or the whole closing formula) what the Pāli abbreviates with -පෙ- or “(විත්ථාරෙතබ්බං)”
  (0:6, 10:1, 16:5, 16:7, 17:2, 17:5, 18:4, 20:1, 20:3, 25:3, 25:5, 29:6, 34:10–35:7, 39:1–41:1, 49:1, 49:7,
  51:13–54:14, 60:7–61:2, 78:0, 80:3, 80:4, 90:4): abbreviation on one side only, no row.
- 56:3, 56:11, 57:3, 57:7: the entry gives the closing paragraph (“එවං පස්සං … නාපරං ඉත්ථත්තායාති පජානාති”)
  three times over, once for each of the three suttas the Pāli gives as one (207-209, 213-215, 216-218, 219-221);
  the neighbouring 56:7 gives it once. A restatement, nothing wrong against the Pāli: no row. (These four are
  likely to come up again in step 2 as `length-long`.)
- BJT's Pāli entries have slips the Sinhala does not follow, rightly: 20:1 ends “යෙන මිධෙකච්චෙ සත්තා දිට්ඨෙව ධම්මෙ
  පරිනිබ්බායන්තීති” (for නො පරිනිබ්බායන්ති), 20:3 has “තන්නිස්සිතං විඤ්ඤාණං හොති” without න, 67:1 has
  “තං ධම්මා මනස්ස සඤ්ඤොජනං” for න ධම්මා. BJT's own Sinhala reads as the sutta requires, and so does text-apz.
  No row; the owner may want to mention them to the maintainer as points in BJT's Pāli.
- 56:3 and the like give නාපරං ඉත්ථත්තාය as “මෙයින් අන්‍යවූ ආත්මයක් නැතැයි” (de Zoysa's stock wording, “no
  other existence after this”); 61:5–63:2 gloss පරිත්තා / අධිමත්තා as (අනිෂ්ට) / (ඉෂ්ට), as BJT's Sinhala does;
  60:1 gives ගුළාගුණ්ඨිකජාතා with both of the commentary's readings: word choices, no row.
- The uddāna verses (15:10, 35:11, 43:9, 43:11, 50:8) stay as they are.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,193 of 5,250 entries (SN: 575 of 1,630 to read; next file `sn-4-2`, 44).

## 2026-11-14 (run 30) — `sn-4-2` and `sn-4-8` finished

Commit e4db85e (pinned). Step 1: all 44 entries of `sn-4-2` (the Vedanā, Mātugāma, Jambukhādaka, Sāmaṇḍaka,
Moggallāna and Citta saṃyuttas) and all 95 entries of `sn-4-8` (the Gāmaṇi, Asaṅkhata and Abyākata saṃyuttas; most
of them one-line peyyāla entries), 139 in all, each read in full against its Pāli. Both files are finished: their
batches are built (`batches/sn-4-2_e4db85e.tsv`, 0 rows; `batches/sn-4-8_e4db85e.tsv`, 7 rows; no unsure rows),
nothing refused.

Confirmed (main file):
- `sn-4-8` 16:4 pali-left-in (Maṇicūḷaka sutta): the last three sentences are left in Pāli (“ඉක්බිති මණිචූළක ගාමණි
  යෙන භගවා තෙනුපසඞ්කමි. … භගවන්තං එතදවොච:”); translated in the wording the file has for the same formula
  (4:8, 19:4). In the same entry නික්ඛිත්තමණිසුවණ්ණා is missing beside අපෙතජාතරූපරජතා; added in the words of
  16:5 and 17:0 (“ශ්‍රමණ ශාක්‍ය පුත්‍රයෝ බහා තබන ලද රන් රුවන් ඇත්තාහ.”).
- `sn-4-8` 42:7 pali-left-in: ඉදං වුච්චති භික්ඛවෙ අසඞ්ඛතං stands in Pāli in the middle of the entry; written
  “මහණෙනි, මේ අසංඛතයයි කියනු ලැබේ.”, as in 39:8 and 50:2.
- `sn-4-8` 50:3 pali-left-in: the entry opens with “ඉති ඛො භික්ඛවෙ දෙසිතං වො මයා අසඞ්ඛතං...” and gives the whole
  translation in brackets; the Pāli and the brackets are taken out.
- `sn-4-8` 70:3, 70:4, 71:1, 71:2 negation (Khandha / Vacchagotta sutta, the questions to the Buddha and to
  Moggallāna): the fourth alternative නෙව හොති න න හොති stands, twice in each entry, as “නොවන්නේත් නොවේ
  නොවන්නේත් නොවේ” (න න හොති for both halves). Written “නොවෙයි, නොවන්නේත් නොවේ”, text-apz's own form for it
  elsewhere. (These eight are the only places in text-apz with the doubled form. BJT's own Sinhala has the same
  slip in 70:4, “නො ම නො වේ, නො ම නො වේ”, and reads rightly in 70:3.)

Unsure: none.

Left alone:
- `sn-4-8` 70:3 opens with a setting the Pāli entry does not have (“මා විසින් මෙසේ අසන ලදී. … ජේතවනාරාමයෙහි වාසය
  කරන සේක.”; the Pāli begins අථ ඛො වච්ඡගොත්තො). De Zoysa's opening, written out as in `sn-2` 18:5 (run of
  that file): no row, as there. If the maintainer wants such added openings taken out, it is one edit in the row
  that is already in the batch for 70:3.
- Entries that write out what the Pāli abbreviates with -පෙ- (`sn-4-2` 14:0–16:2 the nine cessations, 21:5, 25:7,
  26:9–27:5, 43:3, 56:3; `sn-4-8` 41:2) and the Sinhala's “...පෙ...” where the Pāli has -පෙ-: no row.
- `sn-4-2` 21:6, 22:0 give එතං පරමං සන්තං සුඛං as “මේ අතිශයින් ශාන්ත වූ සැපය” (සන්තං taken as “peaceful”);
  60:2, 62:3 say “හුන්” (seated) once for ඨිතං beside “සිටියේය” in the same sentence; 61:0, 61:2, 63:1 shorten
  the quoted Buddha formula to “ශාස්තෲවරය”; `sn-4-8` 41:2 has one phrase for හිතෙසිනා අනුකම්පකෙන අනුකම්පං
  උපාදාය; 53:2 reads අබ්භූත as “without arising”; 72:0 and its like give තථාගතො as “සත්වතෙමේ”: word choices or
  quoted formulas, no row.
- The uddāna verses (`sn-4-2` 22:4, 29:6, 64:19, 82:4; `sn-4-8` 41:5, 76:3, 76:6) stay as they are; 41:5 gives
  කායසමථ as “කායගතාසති, සමථ” and 76:6 gives සඞ්ඛතං as “අසංඛත” (the saṃyuttas' names).

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 2,054 of 5,250 entries (SN: 436 of 1,630 to read; next file `sn-5`, 84).

## 2026-11-14 (run 31) — `sn-5` finished

Commit e4db85e (pinned). Step 1: all 84 entries of `sn-5` (the Magga saṃyutta, from the Bhadda sutta to the
Uddhambhāgiya suttas; most of them peyyāla entries of one frame), each read in full against its Pāli. The file is
finished: its batch is built (`batches/sn-5_e4db85e.tsv`, 3 rows; no unsure rows), nothing refused.

Confirmed (main file):
- `sn-5` 51:5 pali-left-in (175-178, the Kāsi cloth): the Pāli sentence “ඉධ භික්ඛවෙ, භික්ඛු සම්මාදිට්ඨිං භාවෙති
  -පෙ- … වොස්සග්ගපරිණාමිං.” stands in the middle of the entry, before its translation; taken out.
- `sn-5` 58:1 wrong-word (Āgantuka sutta): පඤ්චුපාදානක්ඛන්ධා is given as “පඤ්ඤා උපාදානස්කන්ධයෝ” (පඤ්ඤා for
  පඤ්ච; the only place in text-apz); written “පඤ්ච උපාදානස්කන්ධයෝ”.
- `sn-5` 59:0 clause-missing (Nadī sutta): භොගෙහි අභිහට්ඨුං පවාරෙය්යුං is given only as “කියන්නාහු නම්”;
  written “භෝග සම්පත් ගෙනවුත් පවරන්නාහු නම්” (text-apz has “පවරන්නාහු” for the same passage in `sn-4-1-12` 86:4
  and `sn-5-7` 36:0).

Unsure: none.

Left alone:
- `sn-5` 58:1 gives විජ්ජා ච විමුත්ති ච as “මාර්ගඵල නිර්වාණ යන මොහුය” (de Zoysa's gloss; `mn-3-5` 35:2 has
  “අර්හත් මාර්ගඥාන විද්‍යාවද ඵලවිමුක්තියද” for the same words). A gloss in the commentary's direction with
  “නිර්වාණ” beside it, not a plain mistranslation: left out of the row (which changes only පඤ්ඤා). The owner may
  want to mention it to the maintainer.
- 22:3 gives අද්ධානපරිඤ්ඤත්ථං as “සංසාර ගමන නැති කිරීම පිණිස”; 55:2 gives නො පච්චාවමති as “නොරඳයි”; 54:2's
  last sentence has “වැඩීමට නැගීමට මහත් බවට” for මහන්තත්තං වෙපුල්ලත්තං; 37:8 and the like give
  වොස්සග්ගපරිණාමිං as “නිවනට නැමුනු”, as BJT's Sinhala does; 59:0 has “අසල්වැස්සෝ” for අමච්චා: word choices,
  no row.
- Entries that write out what the Pāli abbreviates with -පෙ- (17:3, 18:4, 18:12, 48:5, 65:3, 65:7, 66:2 the eight
  factors; 22:3–23:2 the second question) and the glosses in brackets on the ogha, yoga and gantha (65:3–66:2; BJT's
  Sinhala has them for the ogha): no row.
- The uddāna verses (23:9, 31:5, 35:5, 64:12) stay as they are.

The add_repo tool was again not available; the repository was already cloned with push access.

Left in step 1: 1,970 of 5,250 entries (SN: 352 of 1,630 to read; next file `sn-5-2`, 61).
