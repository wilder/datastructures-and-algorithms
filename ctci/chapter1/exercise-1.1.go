/*
  Implement an algorithm to determine if a string has all unique characters.
  What if you can not use additional data structures?
*/
package chapter1

import "sort"

/*
    1 - Solution using a data structure:

    Description:
    For each character of the string,
    add it to a map[char:counter] where counter is the amout of times the char occurred in the string
    Then, iterate the map values and check if any is greater than 1.

    Time Complexity: O(n)
    Space Complexity: O(n)

*/
func HasAllUniqueCharacters(str string) bool{
    var m = make(map[int32]int)
    for _, char := range str {
        if m[char] != 0 {
            return false
        }
        m[char] = m[char] + 1
    }
    return true
}

/*
    2 - solution without using a data structure

    Description:
    sort the string
    for each char in the string
    if the previous char is equal to the current
    return false
    it it gets to the end of the string, return true

    Time Complexity: O(n log n)
    Space Complexity: O(1)

 */
func HasAllUniqueCharacters2(str []string) bool{
    sort.Strings(str)
    for index := 1; index < len(str); index++ {
        if str[index] == str[index-1] {
            return false
        }
    }
    return true
}

