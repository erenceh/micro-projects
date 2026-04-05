# micro-projects

Small, focused projects I build independently to sharpen my programming fundamentals. Each one targets a specific concept and takes about 1–2 hours. Built using only official documentation and no AI generated code to strengthen indendepent problem solving skills.

---

## Projects

### Done

| Project                                        | Language | Concepts                       |
| ---------------------------------------------- | -------- | ------------------------------ |
| [go/wc-clone](./go/wc-clone)                   | Go       | File I/O, stdin piping         |
| [python/cat-clone](./python/cat-clone)         | Python   | stdin/stdout piping            |
| [go/worker-pool](./go/worker-pool)             | Go       | Goroutines, channels           |
| [python/hex-inspector](./python/hex-inspector) | Python   | Bit manipulation, bytes        |
| [go/tcp-echo-server](./go/tcp-echo-server)     | Go       | TCP sockets                    |
| [python/udp-chat](./python/udp-chat)           | Python   | UDP sockets                    |
| [go/head-tail-clone](./go/head-tail-clone)     | Go       | Buffered I/O, sliding window   |
| [python/struct-tool](./python/struct-tool)     | Python   | Memory layout, `struct` module |
| [python/log-parser](./python/log-parser/)      | Python   | Parsing, stdin piping          |

### Planned

| Project                       | Language   | Concepts                            |
| ----------------------------- | ---------- | ----------------------------------- |
| python/csv-parser             | Python     | File I/O, parsing                   |
| go/http-parser                | Go         | Protocol parsing, byte manipulation |
| go/dns-query                  | Go         | Raw sockets, binary protocol        |
| go/port-scanner               | Go         | Goroutines, TCP, concurrency        |
| python/tls-inspector          | Python     | TLS handshake, `ssl` module         |
| typescript/rate-limiter       | TypeScript | Sliding window, middleware          |
| typescript/binary-search-tree | TypeScript | Data structures, generics           |
| typescript/lru-cache          | TypeScript | HashMap + linked list               |
| typescript/pipeline-processor | TypeScript | Functional composition              |
| go/ping                       | Go         | Raw sockets, ICMP                   |
| go/arp-scanner                | Go         | Raw sockets, ARP, subnet math       |

---

## Structure

```
micro-projects/
├── go/
│   ├── wc/
│   ├── worker-pool/
│   ├── tcp-echo-server/
│   ├── head-tail/
│   └── ...
├── python/
│   ├── cat/
│   ├── hex-inspector/
│   ├── udp-chat/
│   ├── struct-tool/
│   └── ...
├── typescript/
│   └── ...
└── README.md
```

---

_Each project folder has its own README explaining what it does and what I learned._
