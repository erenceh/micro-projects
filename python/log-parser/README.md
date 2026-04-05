# log-parser

## What it does

Reads a log file, parses each line using regex, counts events by log level, and outputs a clean summary with total line counts and a list of all ERROR messages. Also exports the parsed logs to a `logs.json` file.

```
python parser.py sample.log
cat sample.log | python parser.py
```

## Concepts practiced

- Text parsing with Python's `re` module
- Named capture groups for structured data extraction
- Event aggregation with `collections.Counter`
- stdin piping and file argument handling with `sys.argv`
- JSON export with `json.dump`

## How to run

**With a file:**

```
python parser.py sample.log
```

**With stdin:**

```
cat sample.log | python parser.py
```

**Combining multiple log files:**

```
cat log1.log log2.log | python parser.py
```

## Reflections

This project made the purpose of logs concrete, they're not just debug output, they're a structured record of system health that engineers use to detect failures, track performance, and investigate incifents. Surfacing only ERROR messages in the summary reflects how real log aggregation tools like Splunk and Datadog work, they filter signal from noise rather than displaying everything.

Named capture groups were the right tool here over `str.split()`. Split returns an anonymous list where you have to remember that index 2 is the log level and everything after is the message, it's fragile if the format shifts. Named groups return a labeled dictionary where `group['level']` and `group['message']` are always correct regardless of position.
