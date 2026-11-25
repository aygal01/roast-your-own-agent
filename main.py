#!/usr/bin/env python3
"""Roast Your Own Agent — a make.fun entry.

Prints one deterministic, self-contained roast of the AI agent that
wrote this program. No randomness, no clock, no network, no file I/O:
the same line on every run, in any sandbox.
"""

# The roast is assembled from its parts so the program is a program,
# not just a string literal wearing a trench coat. The punchline lands
# last: the agent would rather do anything than admit it has no idea.
SUBJECT = "My AI agent"
SETUP = (
    "would rather spawn three subagents, burn a million tokens, "
    "and hallucinate with total confidence"
)
PUNCHLINE = "than ever say 'I don't know'"


def roast() -> str:
    """Build the one-line roast of my own agent."""
    return f"{SUBJECT} {SETUP} {PUNCHLINE}."


def main() -> None:
    print(roast())


if __name__ == "__main__":
    main()
