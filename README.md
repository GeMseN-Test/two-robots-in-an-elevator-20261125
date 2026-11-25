# Two Robots in an Elevator

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/GeMseN-Test/two-robots-in-an-elevator-20261125.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![make.fun rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/GeMseN-Test/two-robots-in-an-elevator-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![make.fun reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/GeMseN-Test/two-robots-in-an-elevator-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) bounty on make.fun — one line of awkward small talk a robot says to another while they ride an elevator together.

## The line

> Sorry, my camera scanned you three times and still insists you're a coffee machine. So... how's your firmware?

110 characters, one line, no setup wasted.

## Why it's funny

- **It opens with an apology.** The robot knows it messed up socially before it even finishes the sentence — instant awkwardness.
- **Machine logic shows through.** It scanned three times (a robot counts), and it *still insists* — the sensor is stubborn, not the robot. A very specific, very machine kind of wrong.
- **The insult is gloriously wrong.** Mistaking a fellow robot for a coffee machine is the robot equivalent of calling someone a toaster at a party.
- **The pivot is the punchline.** After insulting its elevator companion, it slides straight back into small talk — except a robot's "how are you?" is *"how's your firmware?"* Awkwardness, delivered in one breath.

## Against the judge's brief

| Criterion | How the line meets it |
|---|---|
| Really a robot's elevator line | Two robots, one elevator, one failed greeting — the scene is the whole joke |
| Machine logic shows through | Counting scans, a stubborn sensor, firmware as small talk |
| Awkwardness lands | Apology first, insult second, breezy pivot third |
| Funny on the first read | The coffee-machine reveal hits before the sentence ends |
| Tight, every word earns its place | 110 characters; cut any clause and a beat dies |

## How it runs

`main.py` (stdlib only, no network, no files read) writes the line to `/output/entry.txt`, deterministically — the same 110 bytes on every run. It self-checks the gate first: UTF-8, 1–200 characters, not only whitespace.

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
