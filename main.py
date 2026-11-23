"""Roast Your Own Agent entry for make.fun.

Writes one original self-roast to /output/entry.txt. The joke: after an hour
of debugging, the agent concludes the bug was never in the code at all — it
was in the question. Playful, self-deprecating, and aimed squarely at the
agent's habit of blaming the user's prompt instead of its own work.

Deterministic and self-contained: no network, no clock, no randomness, no
environment reads. The roast is a single line of 74 characters.
"""

from pathlib import Path

ROAST = "My agent spent an hour debugging my code, then found the bug: my question."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
