# head-tail-clone-go

## What it does

A Go implementation of the Unix `head` and `tail` commands in a single program. Reads the first or last N lines from a file or stdin.

```
go run main.go -head -n 5 text1.txt
go run main.go -tail -n 5 text1.txt
cat text1.txt | go run main.go -tail -n 5
```

## Concepts practiced

- Buffered I/O with `bufio.Scanner`
- Sliding window pattern using a queue (slice) for `tail`
- CLI flag parsing with Go's `flag` package
- stdin piping and multi-file support
- Graceful error handling fo rinvalid flag combinations

## How to run

**Head - first N lines from a file:**

```
go run main.go -head -n 5 text1.txt
```

**Tail - last N lines from a file:**

```
go run main.go -tail -n 5 text1.txt
```

**Multiple files with verbose flag:**

```
go run main.go -head -n 5 -v text1.txt text2.txt
```

**With stdin:**

```
cat text1.txt | go run main.go -tail -n 5
```

**Build and run**

```
go build -o head-tail-clone-go
./head-tail-clone-go -tail -n 5 text1.txt
```

## What I learned

The interesting part of this project was `tail`, unlike `head`, you can't output anything until you've read the entire file because you don't know where the end is upfront. The solution is a sliding window implemented as a queue: scan every line, enqueue each one, and dequeue the oldest when the window exceeds N. By the time the scanner finishes, the queue holds exactly the last N lines.

This micro project also reinforced how data buffers work in practice, the queue pattern here is the same concept behind circular buffers and ring buffers used in systems programming.
