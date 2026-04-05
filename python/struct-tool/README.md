# struct-tool-python

## What it does

Serializes and deserializes a custom binary header using Python's `struct` module. Packs a `PacketHeader` object into raw bytes using big-endian format and writes it to a `.bin` file, then reads it back and unpacks it into a reconstructed object, verifying the round-trip.

```
python struct_tool.py
```

## Concepts practiced

- Binary serialization with Python's `struct` module
- Big-endian byte order and why it matters for network protocols
- Designing a custom binary format with a format string
- `struct.pack` and `struct.unpack` for encoding and decoding raw bytes
- Class methods from constructing objects from binary data

## How to run

```
python struct_tool.py
```

This will create a `packed.bin` file in the same directory. You can inspect the raw bytes with a hex inspector:

```
python hex-inspector/inspector.py packed.bin
```

### Reflections

This project made the connection between in-memory data and raw bytes concrete. A `PacketHeader` object with five fields - ID, type, length, checksum, and timestamp, packs down to exactly 18 bytes laid out in the predictable order. Seeing those bytes in a hex dump and being able to identify each field by offset is what makes binary protocols feel less mysterious.

Big-endian (network byte order) is the agreed standard for internet protocols precisely because byte order has to be consistent across machines. The `>` in the format string is a contract, it guarantees the same layout regardless of the CPU architecture reading the bytes.
