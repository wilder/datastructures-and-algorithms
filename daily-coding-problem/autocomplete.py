'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''

'''
O(|letters|) + O(|query|) = O(n) Time complexity
O(n) Space complexity
'''
from collections import defaultdict
def autocomplete(dictionary, query):
    # build index
    index = defaultdict(list)
    for word in dictionary:
        substring_key = ''
        for letter in word:
            substring_key += letter
            index[substring_key].append(word)

    #autocomplete
    return index[query]

assert autocomplete(['dog', 'dear', 'deal'], 'de') == ['dear', 'deal']
assert autocomplete(['dog', 'dear', 'deal'], 'do') == ['dog']
assert autocomplete(['dog', 'dear', 'deal'], 'd') == ['dog', 'dear', 'deal']
assert autocomplete(['dog', 'dear', 'deal'], 'e') == []
