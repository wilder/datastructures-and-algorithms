class Solution:
    def lengthOfLongestSubstring(self, s):
        longestSubstringLength = 0
        seen = {}
        noDuplicateStartIndex = 0
        for letter in s:
            if letter not in seen:
                seen[letter] = True
            else:
                longestSubstringLength = max(longestSubstringLength, len(seen))
                while(s[noDuplicateStartIndex] != letter):
                    del seen[s[noDuplicateStartIndex]]
                    noDuplicateStartIndex += 1
                noDuplicateStartIndex += 1
        return max(longestSubstringLength, len(seen))
        
