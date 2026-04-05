import json
import re
from collections import Counter
import sys


def main():
    Args = sys.argv
    log_lines = []

    if len(Args) == 1:
        file = sys.stdin
        for f in file:
            log_lines.append(f)

    elif len(Args) == 2:
        try:
            with open(Args[1], "r") as file:
                for line in file:
                    log_lines.append(line)
        except FileNotFoundError as e:
            print(f"{Args[0]}: {Args[1]}: No such file or directory")
            return

    logs, log_counts = get_logs(log_lines)
    print_summary(log_counts, logs)

    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)


def get_logs(log_lines: list) -> tuple[dict, dict]:
    logs = {}
    log_counts = Counter()
    for i, log in enumerate(log_lines):
        m = re.match(
            r"(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}) (?P<level>(?:INFO|DEBUG|ERROR|WARN)) (?P<message>.*)",
            log,
        )
        if m is None:
            continue

        group = m.groupdict()

        log_counts["Total lines"] += 1
        for k, v in group.items():
            if k == "level":
                log_counts[v] += 1

        logs[f"log {i+1}"] = group

    return logs, log_counts


def print_summary(counts: dict, logs: dict) -> None:
    print("Log Summary")
    print("-----------")

    for level, count in counts.items():
        print(f"{level}: {count}")

    print("\nErrors:")
    for info in logs.values():
        if info["level"] == "ERROR":
            print(f"{info['timestamp']} - {info['message']}")


if __name__ == "__main__":
    main()
