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
