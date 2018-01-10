/*
	Write a method to decide if two strings are anagrams or not.
*/
package chapter1

/*
    Solution 1

    Tranverse the string from the beginning
	and from the end at the same time i = 0,
	j = len(str). Increment i and decrement
	j until i == j. if str[i] != str[j],
	it is not an anagram.

	Time Complexity: O(n/2)
    Space Complexity: O(1)

*/
func IsAnagram(str string) bool {

	var strLen = len(str)-1

	for i, j := 0, strLen; i < j; i, j = i+1, j-1 {
		if str[i] != str[j] {
			return false
		}
	}

	return true

}

/*
	Solution 2
	Reverse the string and compare to the original
	Time Complexity: O(n)
	Space Complexity: O(n)

 */
func IsAnagram2(str string) bool {
	return reverse(str) == str
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}