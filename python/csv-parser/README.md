# csv-parser

## What it does

Parses CSV files from scratch without using Python's built-in `csv` module. Handles real-world edge cases including quoted fields, commas inside quotes, and escaped quote characters (`""`). Outputs a formatted table to stdout and exports pardes data to a `data.json` file.

```
python parser.py sample.csv
cat sample.csv | python parser.py
```

## Concepts practiced

- Character-level parsing with state tracking
- Quoted fields handling and escape sequence detection
- Lookahead pattern for detecting `""` inside quoted fields
- stdin piping and file argument handling with `sys.argv`
- JSON export with `json.dump`

## How to run

**With a file:**

```
python parser.py sample.csv
```

**With stdin:**

```
cat sample.csv | python parser.py
```

## Reflections

This project was a good refresher on fundamental string parsing problems. Splitting on commas seems like the obvious approach until you hit quoted fields, a comma inside `"Smith, John"` would split into two fields incorrectly. The solution is an `in_quotes` flag that toggles on at an opening quote and off at the closing quote, treating commas as literal characters while inside a quoted field.

The escaped quote case (`""`) required a lookahead, peeking at the next character to decide whether a `"` is closing the field or representing a literal quote character. This is the same pattern that shows up in lexers and tokenizers for programming languages, where a single character can mean different things depending on context.
