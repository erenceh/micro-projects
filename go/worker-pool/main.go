package main

import (
	"fmt"
	"sync"
	"worker-pool-go/pool"
)

func main() {
	jobs := make(chan pool.Job)
	results := make(chan pool.Result)
	var wg sync.WaitGroup

	for range 5 {
		wg.Add(1)
		go pool.Worker(jobs, results, &wg)
	}

	go func() {
		for i := 1; i < 101; i++ {
			jobs <- pool.Job{Number: i}
		}
		close(jobs)
	}()

	go func() {
		wg.Wait()
		close(results)
	}()

	var res []int
	for result := range results {
		if result.IsPrime {
			res = append(res, result.Number)
		}
	}

	fmt.Println(res)
}
