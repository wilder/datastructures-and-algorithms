/*
	Write a method to replace all spaces in a string with ‘%20’.
*/
package chapter1

/*
    Solution 1

	For each character in the string, if the
	character is not a space, add it to the
	final string, if it is, add %20 to the
	final string.

	Time Complexity: O(n)
    Space Complexity: O(n)

*/
func UrlEncode(str string) string {

	var finalStr = ""

	for _, char := range str {
		if char == ' ' {
			finalStr += "%20"
		} else {
			finalStr += string(char)
		}
	}

	return finalStr

}

/*
    Solution 1

	For each character in the string, if the
	character is a space, replace it by %20.

	Time Complexity: O(n)
    Space Complexity: O(1)

*/
func UrlEncode2(str []string) []string {

	for i := 0; i < len(str); i++ {
		if str[i] == " "  {
			str[i] = "%20"
		}
	}

	return str

}