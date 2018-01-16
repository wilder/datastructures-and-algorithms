/*
	Write a method to decide if two strings are anagrams or not.
*/
package chapter1

import (
	"sort"
	"strings"
)

/*
    Solution 1

    Tranverse the string and
	count its occurrences using a map.

	Tranverse the other string and remove
	the occurence from the map.

	tranverse the map, if some of the values
	is not 0, it's not an anagram. Otherwise,
	it is an anagram.

	Time Complexity: O(n)
    Space Complexity: O(1)

levar contrato looqbox amanhã
*/
func IsAnagram(str string, str2 string) bool {

	var m = make(map[int32]int)

	for _, char := range str {
		m[char] += 1
	}

	for _, char := range str2 {
		m[char] -= 1
	}

	for _, v := range m {
		if v != 0 {
			return false
		}
	}

	return true

}

/*
	Solution 2
	Sort the strings and compare them
	Time Complexity: O(n log n)
	Space Complexity: O(1)

 */

func sortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}


func IsAnagram2(str string, str2 string) bool {
	return sortString(str) == sortString(str2)
}
