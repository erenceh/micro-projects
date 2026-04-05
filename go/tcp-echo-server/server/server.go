package server

import (
	"log"
	"net"
)

func Server(network, address string) {
	l, err := net.Listen(network, address)
	if err != nil {
		log.Fatal(err)
	}
	defer l.Close()

	for {

		conn, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}

		go func(c net.Conn) {
			buffer := make([]byte, 1024)
			for {
				n, err := c.Read(buffer)
				if err != nil {
					break
				}
				c.Write(buffer[:n])
			}
			c.Close()
		}(conn)
	}
}
