// Given an array of integers, return a new array such that each element at index i of the new array is the product of all
// the numbers in the original array except the one at i.
// For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
// If our input was [3, 2, 1], the expected output would be [2, 3, 6].
package main

import (
	"fmt"
)
func getArr(input [] int) {
	multi := 1
	arr := [3]int{}
	for item := range input {
		multi = multi * input[item]
	}
	for i:=0; i< len(input); i++ {
		arr[i] = int(multi/input[i])
	}
	fmt.Println(arr)
}

func main() {
	table := []int{3, 2, 1}
	getArr(table)
}