/**
 * 791. Custom Sort String
 * https://leetcode.com/problems/custom-sort-string/
 *
 */
import java.util.*
class Solution {
    
    fun customSortString(S: String, T: String): String {
        
        val charOcurrence = buildCharOcurrenceMap(S)
        var remainingString = ""
        
        T.forEach {
            if (!charOcurrence.contains(it)) {
                remainingString += it
            } else {
                charOcurrence[it] = charOcurrence[it]!! + 1
            }
        }
        
        return filterNonOcurringCharacters(S, charOcurrence) + remainingString
        
    }
    
    fun buildCharOcurrenceMap(s: String): LinkedHashMap<Char, Int> {
        val charMap = LinkedHashMap<Char, Int>()
        s.forEach {
            charMap.put(it, 0)
        }
        return charMap
    }
    
    fun filterNonOcurringCharacters(s: String, ocurrences: Map<Char, Int>): String {
        var filtered = ""
        ocurrences.forEach { key, value -> 
            for (count in 0 until value) {
                filtered += key
            }
        }
        return filtered
    }
    
}
