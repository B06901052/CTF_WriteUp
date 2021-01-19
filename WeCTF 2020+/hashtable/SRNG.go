package main

import (
	"math/big"
	"math/rand"
	"fmt"
)

func main() {
   rand.Seed(1608443617475458416)
   
   var p1 = big.NewInt(int64(rand.Intn(1 << 32)))
   var p2 = big.NewInt(int64(rand.Intn(1 << 32)))
   
   fmt.Print(p1, p2)
}