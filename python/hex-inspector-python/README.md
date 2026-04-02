# hex-inspector-python

Read any file and display its contents as hex + ASCII side-by-side.

## What it does

A Python implementation of `xxd`. Reads any file or stdin and displays its contents as hex and ASCII side-by-side, 16 bytes per line.

```
python inspector.py inspector.py
echo "hello world" | python inspector.py
```

## Concepts practiced

- Binary file I/O with `open()` in `rb` mode
- Byte-level data manipulation with Python's `bytes` type
- Hex representation and address space formatting
- stdin binary mode with `sys.stdin.buffer`
- String formatting with f-strings and `ljust`

## How to run

**With a file:**

```
python inspector.py <filename>
```

**With stdin:**

```
echo "hello world" | python inspector.py
```

## What I learned

This was more fun than expected. Playing around with translating data into hex and back gave me a much stronger understanding of how data is actually represented at the byte level, how address space works, why each hex pair maps to exactly one byte, and how the same data looks completely different depending on whether you're reading it as text or raw bytes.

It also reinforced how `xxd` actually works under the hood, which makes debugging binary files feel a lot less mysterious.
