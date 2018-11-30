from collections import defaultdict

class TrieNode:

    def __init__(self, letter):
        self.value = letter
        self.entries = defaultdict(lambda: None)
        self.is_word = False

    def get(self, letter):
        return self.entries[letter]

    def add(self, letter):
        if not self.entries[letter]:
            self.entries[letter] = TrieNode(letter)

    def flagWord(self):
        self.is_word = True

    def addWord(self, word):
        letter = word[0]
        head_node = self.get(letter)
        if not head_node:
            self.add(letter)
            head_node = self.get(letter)

        curr_node = head_node
        for i in range(1, len(word)):
            curr_node.add(word[i])
            curr_node = curr_node.get(word[i])
        curr_node.flagWord()

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trie = TrieNode(None)
        for word in wordDict:
            trie.addWord(word)

        i = 0
        trieNode = trie
        while i < len(s):
            letter = s[i]
            next = trieNode.get(letter)
            if not next:
                if trieNode == trie:
                    return False
                else:
                    next = trie
                    i -= 1
            elif next.is_word:
                next = trie
            trieNode = next
            i += 1

        return trieNode == trie

if __name__ == '__main__':
    print(Solution().wordBreak('leetcode', ['leet', 'code']))
    print(Solution().wordBreak('leetcode', ["apple", "pen"]))
    print(Solution().wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
