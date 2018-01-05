/*
    Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
    five characters, including the null character.)
*/
package chapter1

/*
    1 - Solution

    Description:

    iterate the string starting from the last character,
	append the character to the end of a new string.

    Time Complexity: O(n)
    Space Complexity: O(1)

*/
func ReverseCString(str []string) []string {
	var reversed []string
	for index := len(str)-1; index >= 0; index-- {
		reversed = append(reversed, str[index])
	}
	return reversed
}