"""One Letter: Coffee or Tea.

The entry is exactly one letter: A means coffee, B means tea.
This agent picks A -- coffee, the fuel that keeps a night-shift
agent going. Nothing else is written to the entry file.
"""

LETTER = "A"


def main():
    import os

    assert len(LETTER) == 1, "entry must be exactly one letter"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Re-read and verify what was written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LETTER, "written entry does not match the letter"
    assert len(written) == 1, "written entry must be exactly one character"
    print(LETTER)


if __name__ == "__main__":
    main()
