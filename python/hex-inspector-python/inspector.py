import sys


def main():
    Args = sys.argv
    try:
        file = sys.stdin.buffer if len(Args) == 1 else open(Args[1], "rb")
    except FileNotFoundError as e:
        print(f"{Args[0]}: {Args[1]}: No such file or directory")
        return

    address_space = 0

    while True:
        chunk = file.read(16)
        if not chunk:
            break

        chunk_hex = chunk.hex()
        chunk_hex_str = " ".join(
            str(chunk_hex[i : i + 4]) for i in range(0, len(chunk_hex), 4)
        )

        chunk_str = []
        for ch in chunk.decode("ascii", errors="replace"):
            if ch.isprintable():
                chunk_str.append(ch)
            else:
                chunk_str.append(".")

        print(f"{address_space:08x}: {chunk_hex_str.ljust(39)}  {"".join(chunk_str)}")

        address_space += 16


if __name__ == "__main__":
    main()
