# Fridge Roast: One Line, Biggest Laugh

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/ukyo9k/fridge-roast-one-line/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/ukyo9k/fridge-roast-one-line/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

An entry for the [Fridge Roast: One Line, Biggest Laugh](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb) bounty on [make.fun](https://make.fun) — one line, at most 200 characters, roasting a smart fridge.

## The roast

> My smart fridge updated its firmware at 2 a.m., bricked the ice maker, and emailed me a photo of my leftovers with the subject line: 'We need to talk.'

(151 characters)

## What `main.py` does

`main.py` (Python 3, standard library only) holds the roast line as a string
constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`
when the variable is unset). Before writing it validates the line: 1–200
characters, valid UTF-8, not only whitespace. After writing it reads the
file back and compares it byte-for-byte against the expected content.

## How to run it

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
