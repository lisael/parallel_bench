// mostly copied from http://studygolang.com/resources/153

package main

import (
    "fmt"
    "math/rand"
    "time"
)

func MultiPI(samples int) float64 {
    cpus := 8

    threadSamples := samples / cpus
    results := make(chan float64, cpus)

    for j := 0; j < cpus; j++ {
        go func() {
            var inside int
            r := rand.New(rand.NewSource(time.Now().UnixNano()))
            for i := 0; i < threadSamples; i++ {
                x, y := r.Float64(), r.Float64()

                if x*x+y*y <= 1 {
                    inside++
                }
            }
            results <- float64(inside) / float64(threadSamples) * 4
        }()
    }

    var total float64
    for i := 0; i < cpus; i++ {
        total += <-results
    }

    return total / float64(cpus)
}

func main() {
    fmt.Println(MultiPI(100000000))
}
