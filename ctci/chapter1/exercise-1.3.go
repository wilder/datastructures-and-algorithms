/*
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer. NOTE: One or two additional variables are fine.
An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
*/
package chapter1

import (
	"bytes"
)

/*
    Solution 1 - using an auxiliar structure:

    For each character in the string
    if the current character is not in the map
    append it to the variable that will contain the final string
    add it to the map
    otherwise, don't add it to the string.

	Time Complexity: O(n)
    Space Complexity: O(n)

*/
func RemoveDuplicates(str string) string {
	var m = make(map[int32]int)
	var buffer bytes.Buffer
	for _, char := range str {
		//if the char wasn't seen yet
		if m[char] == 0 {
			//convert char to string and append it to the finalString
			buffer.WriteString(string(char))
			m[char] += 1
		}
	}
	return buffer.String()
}
