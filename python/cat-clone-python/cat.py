import sys


def main():
    Args = sys.argv

    if len(Args) == 1:
        file = sys.stdin
        for f in file:
            print(f, end="")

    elif len(Args) > 1:
        for i in range(1, len(Args)):
            try:
                with open(file=Args[i], mode="r") as file:
                    for f in file:
                        print(f, end="")
            except FileNotFoundError as e:
                print(f"{Args[0]}: {Args[i]}: No such file or directory")
                return


if __name__ == "__main__":
    main()
