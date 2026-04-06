from collections import defaultdict
import json
import sys


def main():
    Args = sys.argv
    rows = []

    try:
        if len(Args) == 1:
            file = sys.stdin
            for line in file:
                rows.append(parse(line.strip("\n")))

        elif len(Args) == 2:
            try:
                with open(Args[1], "r") as file:
                    for line in file:
                        rows.append(parse(line.strip("\n")))

            except FileNotFoundError:
                print(f"{Args[0]}: {Args[1]}: No such file or directory")
                return

    except KeyboardInterrupt:
        return

    data = {}
    for i in range(1, len(rows)):
        test = {}
        for j, f in enumerate(rows[i]):
            test[rows[0][j]] = f
        data[f"id {i}"] = test

    print_data(data, rows[0])

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def parse(line: str) -> list:
    current_field = []
    in_quotes = False
    fields = []

    for i, char in enumerate(line):
        if char == '"':
            if i != len(line) - 1 and line[i + 1] == '"' and in_quotes:
                current_field.append(char)
            elif i != len(line) - 1 and line[i + 1] != '"' and in_quotes:
                in_quotes = not in_quotes
            else:
                in_quotes = not in_quotes
        elif char == "," and not in_quotes:
            fields.append("".join(current_field))
            current_field = []
        else:
            current_field.append(char)

    fields.append("".join(current_field))

    return fields


def print_data(data, cols):
    for col in cols:
        if col != cols[0]:
            print("| ", end="")
        print(f"{col:<20}", end="")
    print()
    print("-" * 20 * len(cols))
    for info in data.values():
        for i, v in enumerate(info.values()):
            if i != 0:
                print("| ", end="")
            print(f"{v:<20}", end="")
        print()


if __name__ == "__main__":
    main()
