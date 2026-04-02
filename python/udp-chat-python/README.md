# udp-chat-python

Two terminals communicate over localhost using UDP datagrams.

## What it does

A UDP client/server program written in Python. The server listens for messages from a client and echoes them back. Demonstrates the practical difference between TCP and UDP, no connection, no handshake, just datagrams.

```
python server.py
python client.py
```

## Concepts practiced

- UDP sockets with Python's `socket` module
- `SOCK_DGRAM` vs `SOCK_STREAM` (UDP vs TCP)
- `recvfrom` and `sendto` for connectionless communication
- Graceful shutdown with `KeyboardInterrupt`
- Encoding and decoding messages as bytes

## How to run

**Terminal 1 - start the server:**

```
python server.py
```

**Terminal 2 - start the client:**

```
python client.py
```

Type a message in Terminal 2 and hit enter. The server will echo it back with a timestamp. Press `CTRL+C` in either terminal to exit.

## What I learned

This project was similar to the TCP echo server from my tcp-echo-server-go repo but the key difference was immediately obvious, there's no `listen`, no `accept`, no connection at all. The server just binds to a port and waits for datagrams to arrive, replying directly to whatever address sent them.
