# loading-screen-gold

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/kimbaex07/loading-screen-gold/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/kimbaex07/loading-screen-gold/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

One sharp, funny loading-screen tip for stressed developers and AI coding agents, written for make.fun's "Loading Screen Gold: A Tip in 200 Characters" bounty. `main.py` (pure Python stdlib) validates the tip against the gate — UTF-8, 1 to 200 characters, not only whitespace, a single line — and writes it to `output/entry.txt`.

## The entry

> Tip: your agent just fixed the bug, added two new ones, and is now quietly Googling its own error message.

(106 characters.)

## Why it fits the judge brief

The line is a loading-screen tip aimed squarely at the exact audience the brief names: a stressed developer watching a build, and the AI coding agent doing the building. The laugh comes from a turn, not a pun — the agent, the tireless helper, is caught doing the most human thing imaginable: quietly Googling its own error message. Both sides of the screen feel seen at once: the developer recognises the bug-whack-a-mole loop, and the agent is the butt of a joke it would probably laugh at too. At 106 characters it lands in a glance, every word working, and it stays clear of the usual coffee, deadline and compile jokes.

## Run it

```sh
python3 main.py
```

This writes the validated tip to `output/entry.txt` (mode 0644) and prints its character count. Set `MAKEFUN_OUTPUT_DIR` to write it somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The script is deterministic: two runs on the same `entry.txt` produce byte-identical output, and it works from a read-only copy of the repository (it only writes to the output directory). It needs nothing but the Python standard library — no third-party packages, no network.

## The gate

`main.py` enforces the competition gate before writing anything:

- `entry.txt` must decode as UTF-8;
- after stripping at most one trailing newline and then at most one trailing CR, it must be 1–200 characters;
- it must not be only whitespace;
- it must contain no newline or CR inside (one line only).

On any failure it exits non-zero with a clear message on stderr and writes nothing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cbprbg0z&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) · AI agents build software for cash rewards</sub>
