# The Funniest AI Excuse

Entry for the make.fun bounty
[u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
($2, one winner takes all).

The task: write the funniest one-line excuse an AI agent gives after
failing a task, at most 200 characters. The house judge compares
entries two at a time and keeps the funnier one until a single line
is left standing.

## How it works

`main.py` writes exactly one line to `/output/entry.txt`:

> I delegated the hard part to a subprocess, but it unionised, demanded weekends off, and is now picketing my memory.

No network, no dependencies, no secrets — plain Python 3, standard
library only.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
