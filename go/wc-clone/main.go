package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	Args := os.Args

	var file *os.File
	if len(Args) == 1 {
		file = os.Stdin

	} else if len(Args) == 2 {
		var err error
		file, err = os.Open(Args[1])
		if err != nil {
			fmt.Printf("file does not exist: %v", err)
			return
		}
		defer file.Close()
	}

	res, err := getCounts(file)
	if err != nil {
		fmt.Println(err)
		return
	}

	for _, out := range res {
		fmt.Printf("%*d", 8, out)
	}

	fmt.Println()
}

func getCounts(file *os.File) ([]int, error) {
	scanner := bufio.NewScanner(file)
	var res []int

	numLines := 0
	numWords := 0
	bytes := 0
	for scanner.Scan() {
		line := scanner.Text()
		numLines++

		words := strings.Fields(line)
		numWords += len(words)

		bytes += len(line) + 1
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading input:", err)
	}

	file.Seek(-1, 2)
	buf := make([]byte, 1)
	if n, _ := file.Read(buf); n > 0 && buf[0] != 0x0A {
		numLines--
		bytes--
	}

	res = append(res, numLines)
	res = append(res, numWords)
	res = append(res, bytes)

	return res, nil
}
