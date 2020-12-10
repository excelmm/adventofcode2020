package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func main() {

	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		os.Exit(1)
	}

	scanner := bufio.NewScanner(strings.NewReader(string(input)))
	scanner.Split(bufio.ScanWords)

	var inputs []int

	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			os.Exit(1)
		}
		inputs = append(inputs, x)
	}

	ansa := 0
	ansb := 0

	for i := 0; i < len(inputs)-1; i++ {
		for j := i + 1; j < len(inputs); j++ {
			if inputs[i]+inputs[j] == 2020 {
				ansa = inputs[i] * inputs[j]
				break
			}
			for k := j + 1; k < len(inputs); k++ {
				if inputs[i]+inputs[j]+inputs[k] == 2020 {
					ansb = inputs[i] * inputs[j] * inputs[k]
					break
				}
			}
		}
	}

	fmt.Println(ansa)
	fmt.Println(ansb)

}
