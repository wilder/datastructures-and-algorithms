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
    Space Complexity: O(n)

*/
func ReverseCString(str []string) []string {
	var reversed []string
	for index := len(str)-1; index >= 0; index-- {
		reversed = append(reversed, str[index])
	}
	return reversed
}

/*
	2 - Solution

	Description:
	Iterate the string until its half,
	change the first for the last,
	the second for the last-1 and so on.

	Time Complexity: O(n/2)
	Space Complexity: O(1)

 */
 func ReverseCString2(str []string) []string {
 	 var len = len(str)-1
	 for i := 0; i < len/2; i++ {
		str[i], str[len-i] = str[len-i], str[i]
	 }
	 return str
 }
