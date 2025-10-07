package main

import "fmt"

func main() {
	// Tipe data dasar
	var integer int = 10
	var floatingPoint float64 = 3.14
	var boolean bool = true
	var text string = "Hello, Go!"

	fmt.Println("Integer:", integer)
	fmt.Println("Floating Point:", floatingPoint)
	fmt.Println("Boolean:", boolean)
	fmt.Println("Text:", text)

	// Tipe data komposit
	var array [3]int = [3]int{1, 2, 3}
	var slice []int = []int{4, 5, 6}
	var mapping map[string]int = map[string]int{"satu": 1, "dua": 2}

	fmt.Println("Array:", array)
	fmt.Println("Slice:", slice)
	fmt.Println("Map:", mapping)

	// Tipe data khusus
	var runeValue rune = 'A' // Representasi Unicode code point
	fmt.Println("Rune:", runeValue)
}