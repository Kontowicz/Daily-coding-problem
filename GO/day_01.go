// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
package main

import (
	"fmt"
	"sort"
)

func check(arr [] int, k int) bool {
	begin := 0
	end := len(arr) - 1
	sort.Ints(arr)

	for begin < end {
		s := arr[begin] + arr[end]
		if s == k {
			return true
		} else if s > k {
			end -= 1
		} else if s < k {
			begin += 1
		}
	}
	return false
}

func main() {
	table := []int{10, 15, 3, 7}
	fmt.Println(check(table, 17))
}