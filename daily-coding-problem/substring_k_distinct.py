'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def longestSubstringWithKDistinct(string, k):
    seen = {}
    
    currentSubstring = ''
    longestSubstring = ''
    
    startIndex = 0

    for index, letter in enumerate(string):
        print("index: {0} - letter: {1}".format(index, letter))
        if letter not in seen:
            if len(seen) + 1 > k:
                
                if len(currentSubstring) > len(longestSubstring):
                    longestSubstring = currentSubstring

                lastLetterIndex = index - 1
                while lastLetterIndex != startIndex and string[lastLetterIndex] == string[index - 1]:
                    lastLetterIndex -= 1

                for l in set(string[startIndex:lastLetterIndex+1]):
                    if string[index - 1] != l:
                        print("removing {0}".format(l))
                        del seen[l]
                startIndex = lastLetterIndex+1
                currentSubstring = string[startIndex:index]

            seen[letter] = True
        currentSubstring += letter
    return longestSubstring


print(longestSubstringWithKDistinct("abcba", 2))
