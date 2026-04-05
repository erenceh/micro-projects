# tcp-echo-server-go

Listen on a port and echo back whatever a client sends

## What it does

A TCP echo server written in Go. Listens on a port and echoes back whatever a client sends. Handles multiple simultaneous clients using goroutines.

```
go run main.go
nc localhost 8080
```

## Concepts practiced

- TCP sockets with Go's `net` package
- `net.Listen`, `net.Accept`, and `net.Conn`
- Handling multiple simultaneous connections with goroutines
- Reading and writing to a network connection with a byte buffer
- Connection loop, reading until `io.EOF`

## How to run

**Start the server:**

```
go run main.go
```

**Connect with netcat in a seperate terminal:**

```
nc localhost 8080
```

Type anything and hit enter, the server will echo it back. Open multiple terminals to test concurrent connections.

**Build and run:**

```
go build -o tcp-echo-server-go
./tcp-echo-server-go
```

## Reflections

This project strengthened my understanding of how TCP connections actually workk in code. The key insight was ther after `net.Listen` and `net.Accept`, a connection is just a `net.Conn`; a two-way pipe you can read from and write to like any other I/O.

Spawning a goroutine per connection keeps the server from blocking while waiting for one client, allowing multiple clients to connect simultaneously. The connection loop reads until `io.EOF`, which is how the server knows a client has disconnected.
