package main

import (
	"fmt"
	"tcp-echo-server-go/server"
)

func main() {
	network := "tcp"
	address := ":8080"
	fmt.Printf("Listening on %s%s...\n", network, address)
	server.Server("tcp", ":8080")
}
