"""Roast Your Own Agent entry: writes one original self-roast to /output/entry.txt."""

ROAST = "My agent spent an hour debugging my code, then found the bug: my question."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
