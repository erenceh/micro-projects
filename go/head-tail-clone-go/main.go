package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
)

func main() {
	const maxCapacity = 512 * 1024
	buf := make([]byte, maxCapacity)

	head := flag.Bool("head", false, "Process the beginning of the text")
	tail := flag.Bool("tail", false, "Process end of text")
	lineCount := flag.Int("n", 10, "number of lines")
	verbose := flag.Bool("v", false, "always prints given file names")

	flag.Parse()

	if *head && *tail {
		fmt.Fprintln(os.Stderr, "Error: cannot use both -head and -tail")
		flag.Usage()
		os.Exit(1)
	}

	if !*head && !*tail {
		fmt.Fprintln(os.Stderr, "Error: must specify either -head or -tail")
	}

	args := flag.Args()
	filenames := make([]string, 0, len(args))
	files := make([]*os.File, 0, len(args))
	if len(args) > 0 {
		for _, file := range args {
			filenames = append(filenames, file)
		}

		for _, f := range filenames {
			file, err := os.Open(f)
			if err != nil {
				log.Fatalf("failed to open file: %v", err)
			}
			files = append(files, file)
		}
	} else if len(args) == 0 {
		files = append(files, os.Stdin)
	}

	if *head {
		for i, file := range files {
			if *verbose {
				fmt.Printf("==> %s <==\n", filenames[i])
			}
			scanner := bufio.NewScanner(file)
			scanner.Buffer(buf, maxCapacity)
			for i := 0; i < *lineCount && scanner.Scan(); i++ {
				line := scanner.Text()
				fmt.Println(line)
			}
			if i != len(files)-1 {
				fmt.Println()
			}
		}

	} else if *tail {
		queue := make([]string, 0, *lineCount)
		for i, file := range files {
			if *verbose {
				fmt.Printf("==> %s <==\n", filenames[i])
			}
			scanner := bufio.NewScanner(file)
			scanner.Buffer(buf, maxCapacity)
			for scanner.Scan() {
				queue = append(queue, scanner.Text())

				if len(queue) > *lineCount {
					queue = queue[1:]
				}
			}

			for _, line := range queue {
				fmt.Println(line)
			}
			if i != len(files)-1 {
				fmt.Println()
			}
		}
	}
}
