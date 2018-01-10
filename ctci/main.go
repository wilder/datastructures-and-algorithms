package main

import "fmt"
import (
	"./chapter1"
	"strings"
)

func main() {
	//exercise1_1()
	exercise1_2()
	//exercise1_3()
	//exercise1_4()
	exercise1_5()
}


func exercise1_1(){
	fmt.Printf("Exercise 1.1 - hasAllUniqueCharacters(\"abcde\"): %t\n", chapter1.HasAllUniqueCharacters("abcde")) //true
	fmt.Printf("Exercise 1.1 - hasAllUniqueCharacters(\"abcdbe\"): %t\n", chapter1.HasAllUniqueCharacters("abcdbe")) //false
	fmt.Printf("Exercise 1.1 - hasAllUniqueCharacters(\"abecde\"): %t\n", chapter1.HasAllUniqueCharacters("abecde")) //false
	fmt.Printf("Exercise 1.1 - hasAllUniqueCharacters(\"aabcde\"): %t\n", chapter1.HasAllUniqueCharacters("aabcde")) //false

	fmt.Printf("Exercise 1.1+ - hasAllUniqueCharacters2(\"abcde\"): %t\n", chapter1.HasAllUniqueCharacters2(strings.Split("abcde", ""))) //true
	fmt.Printf("Exercise 1.1+ - hasAllUniqueCharacters2(\"abcbde\"): %t\n", chapter1.HasAllUniqueCharacters2(strings.Split("abcbde", ""))) //false
	fmt.Printf("Exercise 1.1+ - hasAllUniqueCharacters2(\"abecdee\"): %t\n", chapter1.HasAllUniqueCharacters2(strings.Split("abecdee", ""))) //false
	fmt.Printf("Exercise 1.1+ - hasAllUniqueCharacters2(\"axagbsbcde\"): %t\n", chapter1.HasAllUniqueCharacters2(strings.Split("axagbsbcde", ""))) //false
}

func exercise1_2()  {
	fmt.Printf("Exercise 1.2 - reverseCString([]int32{'h','e', 'l','l','o'}): %s\n", chapter1.ReverseCString([]string{"h","e", "l","l","o"})) //olleh
	fmt.Printf("Exercise 1.2+ - reverseCString2([]int32{'h','e', 'l','l','o'}): %s\n", chapter1.ReverseCString2([]string{"h","e", "l","l","o"})) //olleh
}

func exercise1_3(){
	fmt.Printf("Exercise 1.3 - hasAllUniqueCharacters(\"abcde\"): %s\n", chapter1.RemoveDuplicates("abcde")) //abcde
	fmt.Printf("Exercise 1.3 - hasAllUniqueCharacters(\"abcdbe\"): %s\n", chapter1.RemoveDuplicates("abcdbe")) //abcde
	fmt.Printf("Exercise 1.3 - hasAllUniqueCharacters(\"abecde\"): %s\n", chapter1.RemoveDuplicates("abecde")) //abecd
	fmt.Printf("Exercise 1.3 - hasAllUniqueCharacters(\"aabcde\"): %s\n", chapter1.RemoveDuplicates("aabcdeab")) //abcde
}

func exercise1_4(){
	fmt.Printf("Exercise 1.4 - isAnagram(\"aaaaaa\"): %t\n", chapter1.IsAnagram("aaaaa")) //true
	fmt.Printf("Exercise 1.4 - isAnagram(\"abba\"): %t\n", chapter1.IsAnagram("abba")) //true
	fmt.Printf("Exercise 1.4 - isAnagram(\"abbacbba\"): %t\n", chapter1.IsAnagram("abbabba")) //true
	fmt.Printf("Exercise 1.4 - isAnagram(\"aabbd\"): %t\n", chapter1.IsAnagram("aabbd")) //false

	fmt.Printf("Exercise 1.4+ - isAnagram2(\"aaaaaa\"): %t\n", chapter1.IsAnagram2("aaaaa")) //true
	fmt.Printf("Exercise 1.4+ - isAnagram2(\"abba\"): %t\n", chapter1.IsAnagram2("abba")) //true
	fmt.Printf("Exercise 1.4+ - isAnagram2(\"abbacbba\"): %t\n", chapter1.IsAnagram2("abbabba")) //true
	fmt.Printf("Exercise 1.4+ - isAnagram2(\"aabbd\"): %t\n", chapter1.IsAnagram2("aabbd")) //false
}

func exercise1_5(){
	fmt.Printf("Exercise 1.5 - urlEncode(\"hello\"): %s\n", chapter1.UrlEncode("hello")) //hello
	fmt.Printf("Exercise 1.5 - urlEncode(\"hello world\"): %s\n", chapter1.UrlEncode("hello world ")) //hello%20world%20)
	fmt.Printf("Exercise 1.5+ - urlEncode2(\"hello\"): %s\n", chapter1.UrlEncode2(strings.Split("hello", ""))) //hello
	fmt.Printf("Exercise 1.5+ - urlEncode2(\"hello world\"): %s\n", chapter1.UrlEncode2(strings.Split("hello world ", ""))) //hello%20world%20)
}