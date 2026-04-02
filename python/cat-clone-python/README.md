# cat-clone-python

Read from stdin or a file and write to stdout, supporting Unix-style piping.

## What it does

A Python implementation of the Unix `cat` command. Reads from one or more files or stdin and writes the contents to stdout, supporting Unix-style piping.

```
python cat.py text.txt
echo "hello world" | python cat.py
python cat.py text.txt text2.txt
```

## Concepts practiced

- stdin/stdout piping with `sys.stdin`
- File I/O with Python's built-in `open()`
- Streaming output line by line rather than loading into memory
- CLI argument parsing wiht `sys.argv`
- Error handling with `FileNotFoundError`

## How to run

**With a file:**

```
python cat.py <filename>
```

**With multiple files:**

```
python cat.py <file1> <file2>
```

**With stdin:**

```
echo "hello world" | python cat.py
```

## Reflections

This micro project was a refresher on how programs read file lines and interact with stdin in Python. The key insight was that `sys.stdin` and the result of `open()` are both file objects, the same type, so they can be handled with the same logic.

Streaming output line by line rather than loading everything into memory first is an important habit for CLI tools, especially when dealing with large files. Error handling also needed to match Unix conventions, printing the error and continuing to the next file rather than stopping entirely.
