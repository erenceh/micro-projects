# worker-pool-go

Fan-out a set of jobs across N goroutines and collect results via channels.

## What it does

A Go implementation of the worker pool concurrency pattern. Spawns 5 goroutines that concurrently check whether numbers from 1-100 are prime, collecting results via channels. Results intentionally print out of order to demonstrate that goroutines run independently and don't wait for each other.

```
go run main.go
```

## Concepts practiced

- Goroutines and the worker pool pattern
- Buffered and unbuffered channels
- `sync.WaitGroup` for coordinating goroutine completion
- Sending and receiving structs over channels
- Avoiding deadlocks in concurrent programs

## How to run

**Run directly:**

```
go run main.go
```

**Build and run:**

```
go build -o worker-pool-go
./worker-pool-go
```

## Reflections

The concept of concurrency and parallelism made sense going in, but the mechanics of goroutines in Go were trickier than expected.

The most important thing I learned was how goroutines communicate through channels, how sending blocks until a receiver is ready, and how closing a channel signals workers that no more jobs are coming. Deadlocks were also a real lesson: if you send jobs into an unbuffered channel before workers are ready to receive the whole program freezes. Wrapping the send loop in a goroutine was the fix.

The out-of-order results in the output are intentional, they're proof that the workers are running concurrently and not waiting for each other.
