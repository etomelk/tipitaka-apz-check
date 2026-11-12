#!/bin/bash
# Fetch the sources into ../apz-sources (or $APZ_SRC): tipitaka.lk (text-apz, BJT text, the translation guidelines)
# and the archived de Zoysa. Always moves to the latest upstream commit, and prints it.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${APZ_SRC:-$ROOT/../apz-sources}"
mkdir -p "$SRC"
if [ ! -d "$SRC/tipitaka.lk/.git" ]; then
  git clone -q --depth 1 --filter=blob:none --sparse https://github.com/pathnirvana/tipitaka.lk "$SRC/tipitaka.lk"
fi
git -C "$SRC/tipitaka.lk" sparse-checkout set --no-cone '/public/static/text-apz/' '/public/static/text/dn-*' \
  '/public/static/text/mn-*' '/public/static/text/sn-*' '/public/static/text/an-*' '/public/static/text/kn-*' \
  '/dev/apz-trans/prompt-v2.md' '/dev/apz-trans/glossary.tsv' >/dev/null
git -C "$SRC/tipitaka.lk" fetch -q --depth 1 origin master
git -C "$SRC/tipitaka.lk" reset -q --hard FETCH_HEAD
if [ ! -d "$SRC/pitaka.lk-archive/.git" ]; then
  git clone -q --depth 1 --filter=blob:none --sparse https://github.com/pathnirvana/pitaka.lk-archive "$SRC/pitaka.lk-archive"
  git -C "$SRC/pitaka.lk-archive" sparse-checkout set main/text/sinh-aps >/dev/null
fi
echo "APZ_SRC=$SRC"
echo "COMMIT=$(git -C "$SRC/tipitaka.lk" rev-parse --short HEAD)"
