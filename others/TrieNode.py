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
