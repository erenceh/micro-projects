package pool

import "sync"

type Job struct {
	Number int
}

type Result struct {
	Number  int
	IsPrime bool
}

func Worker(jobs chan Job, results chan Result, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		isPrime := isPrime(job.Number)
		results <- Result{Number: job.Number, IsPrime: isPrime}
	}
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
