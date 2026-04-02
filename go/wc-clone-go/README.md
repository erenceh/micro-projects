# wc-clone-go

Implement Unix `wc` - count words, lines, and bytes from a file or stdin.

## What it does

A Go implementation of the Unix `wc` command. Counts the number of lines, words, and bytes from a file or stdin.

```
go run main.go text.txt
echo "hello world" | go run main.go
```

## Concepts practiced

- File I/O with `os.Open` and `os.Stdin`
- Reading from stdin vs a file using `bufio.Scanner`
- Byte-level string handling with `len()` and `scanner.Bytes()`
- CLI argument parsing with `os.Args`
- Unix-style stdin piping

## How to run

**With a file:**

```
go run main.go <filename>
```

**With stdin:**

```
echo "hello world" | go run main.go
```

**Build and run:**

```
go build -o wc-clone-go
./wc-clone-go <filename>
```

## Reflections

This micro project helped me understand how programs read from files and standard input in Go. The key insight was the `os.Stdin` and the result of `os.Open` are both `*os.File` so they can be handled with the same function.

Working at the byte level was trickier than expected. `bufio.Scanner` strips newline characters before the program reads them, which means counting bytes accurately requires accounting for that manually. Files without a trailing newline on the last line are an edge case that needed special handling.
