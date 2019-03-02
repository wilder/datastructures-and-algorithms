/*
 * Leetcode 49. Group Anagrams
 * https://leetcode.com/problems/group-anagrams/
 *
*/

class Solution {
       
    fun groupAnagrams(strings: Array<String>): List<List<String>> {
    
        val groups = hashMapOf<String, MutableList<String>>()
    
        strings.forEach {s ->
            val sortedLetters = s.toCharArray().sorted()
            val key = sortedLetters.toString()
    
            groups.computeIfAbsent(key) { mutableListOf() }
                .add(s)
    
        }
        
        return groups.values.toList()
    
    }
    
}
