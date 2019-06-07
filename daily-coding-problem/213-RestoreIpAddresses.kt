/**
 *
 * 93. Restore IP Addresses
 * Daily Coding Problem #213
 * https://leetcode.com/problems/restore-ip-addresses/
 *
 */
class Solution {
    
    val result = mutableSetOf<String>()
    val memo = mutableSetOf<String>()
    
    fun restoreIpAddresses(s: String): List<String> {
        restoreIpAddresses(s, "", Pair(0, 1), 0)
        restoreIpAddresses(s, "", Pair(0, 2), 0)
        restoreIpAddresses(s, "", Pair(0, 3), 0)
        return result.toList()
    }
    
    fun restoreIpAddresses(s: String, currRestored: String, group: Pair<Int, Int>, groupCount: Int) {
        if (group.first >= s.length || group.second > s.length) {
            return
        }

        val currentGroup = s.substring(group.first, group.second)
        if (!isGroupValid(currentGroup) || groupCount == 4) {
            return
        }

        val newGroup = bulidNewGroup(currRestored, currentGroup)
        if (memo.contains("$currRestored$newGroup")) {
            return
        }

        if (groupCount == 3) {
            if (group.second == s.length) {
                result.add(newGroup)
            }
            return
        }


        restoreIpAddresses(s, newGroup, Pair(group.second, group.second + 3), groupCount + 1)

        restoreIpAddresses(s, newGroup, Pair(group.second, group.second + 2), groupCount + 1)

        restoreIpAddresses(s, newGroup, Pair(group.second, group.second + 1), groupCount + 1)

        memo.add("$currRestored$newGroup")

    }

    private fun bulidNewGroup(currRestored: String, currentGroup: String): String {
        var separator = "."
        if (currRestored.isEmpty()) {
            separator = ""
        }
        val newGroup = "$currRestored$separator$currentGroup"
        return newGroup
    }

    fun isGroupValid(group: String): Boolean {

        if(group.isEmpty() || (group[0] == '0' && group.length > 1)) {
            return false
        }

        val groupAsInt = group.toInt()
        return groupAsInt in 0..255
    }
    
}
