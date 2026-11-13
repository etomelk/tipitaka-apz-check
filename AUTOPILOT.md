# Autopilot: standing instruction for one run

Each run is a fresh session. Read `CLAUDE.md` first, all of it: the brief, the format and the reading rules.

1. Check out the branch `autopilot` (create it from `main` if it does not exist). Run `bash tools/setup.sh`, export the
   `APZ_SRC` it prints and note `COMMIT` (it must be e4db85e while `data/pin_commit.txt` is there: the maintainer asked
   on 2026-11-13 for every batch against that commit; if it is anything else, stop and tell the owner). Run `python3 tools/analyse.py dn mn sn an` and
   `python3 tools/findings.py dn mn sn an` (a few minutes). Read `$APZ_SRC/tipitaka.lk/dev/apz-trans/prompt-v2.md`.
2. `python3 tools/work.py status`. Work on the lowest step that has entries to read, and in it the first file with
   entries to read (the order `work.py list` gives: DN, MN, SN, AN).
3. Read entries with `python3 tools/work.py show <step> <file> 0 12`, twelve at a time, each in full against its Pāli
   as `CLAUDE.md` says. After each twelve: add any findings to `verdicts/<file>.json` (edits, not retyped text; mark
   `"unsure": true` only when you doubt the reading; a sure omission, error, reversal or left-in Pāli goes in the main
   file even if the sense can be pieced together from nearby text, and a restatement or loose wording is no finding:
   `CLAUDE.md`, "Added 2026-11-13"), then `python3 tools/work.py done <step> <file> <pi>:<ei> …` for all twelve.
   Read about 100 entries in a run, fewer if they are long; stop at a file's end when near that number.
4. When a file is finished in the step, run `python3 tools/work.py batch <file> <file>`; it must refuse nothing. Fix a
   refused finding by reading the entry again, never by forcing it.
5. When a whole Nikāya is finished in step 1 (DN, then MN, SN, AN), also build its batch for the owner:
   `python3 tools/work.py batch <nik>-step1 <all its files>`, and write `batches/<nik>-step1_ISSUE.md`: a short issue
   text for pathnirvana/tipitaka.lk naming the commit, the number of entries read, the number of rows by kind, and that
   the unsure file is attached separately (the DN issue text also asks the one open question on සො ධම්මං දෙසෙති,
   `CLAUDE.md`). The maintainer wants each collection as soon as it finishes: notify the owner at once. Steps 2–4 are one batch each over the four Nikāyas, built the same way.
6. Add a dated entry to `AUTOPILOT_LOG.md`: the commit, the files and number of entries read, the findings (file,
   page:entry, kind, sure or unsure), and anything the owner should know (an entry that changed upstream after it was
   read, a doubt about the rules). Commit everything with a plain-English message and push the branch `autopilot`.
   Never push to `main`. Never post, comment or open anything on pathnirvana/tipitaka.lk.
7. When step 4 is finished, stop: write "finished" in the log, do nothing more in later runs, and tell the owner. The
   Khuddaka (step 5): the maintainer asked for it after AN (2026-11-13), book by book; `tools/work.py` has no step for
   it yet, so say in the notification that it is next and needs setting up in a conversation with the owner.

The owner is not watching: do not ask questions. Where the rules do not settle a case, leave the entry out of the main
file (unsure, with the doubt said in the reason) and note it in the log. Notify the owner only when a Nikāya's batch is
ready to post, when all four steps are finished, or when a run could not do its work.
