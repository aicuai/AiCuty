# CLAUDE.md

Claude Code はこのファイルを最初に読みます。作業方針の正本は [AGENTS.md](AGENTS.md) です。
ここには書き写さず、読み込むだけにしています（同じことを 2 か所に書くと、片方だけ古くなります）。

@AGENTS.md

## Claude Code 向けの補足

- **設定や口調を答える前に、該当する `<CharacterName>/README.md` を読む。** 記憶や他リポジトリの写しで答えない。
  本リポジトリにない詳細（楽曲・NG ルール・記事の文体）は `aicuty-bots/shared/characters.yaml` にある（AGENTS.md 第 1 節）。
- **作業を始める前に [SKILLS.md](SKILLS.md) で手順と道具を確かめる。** 画像生成・ボイス・記事には、それぞれ決まった手順がある。
- **変更はブランチと PR で出す。** `gh pr merge` は Claude Code の権限層が止めるので、マージは人に 1 行で頼む（AGENTS.md 第 5 節）。
- **画像を置く前に、Read ツールで中身を見る。** ファイル名だけで判断しない。
- **セッションの記憶（`~/.claude/projects/*/memory/`）は他のマシンにも他のセッションにも渡らない。**
  次の人が要る判断材料は、README・`REVIEW.md`・Issue に書く（AGENTS.md 第 7 節）。
- 他のリポジトリのセッションから来た場合、このリポジトリは**読むだけ**で済むことが多い。
  読む場所は AGENTS.md 第 0 節の早見表にある。
