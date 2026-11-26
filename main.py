from pathlib import Path

ENTRY = (
    "My smart fridge photographs the leftovers, nags me about expiry dates, "
    "and still lets the spinach rot like it entered witness protection."
)
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if "\n" in ENTRY or not ENTRY.strip() or len(ENTRY) > 160:
        raise ValueError("entry must be one non-empty line of at most 160 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
