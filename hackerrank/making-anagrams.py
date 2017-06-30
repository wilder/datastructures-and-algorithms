import collections

def number_needed(a, b):
    alphabet_dict = collections.defaultdict(lambda: 0)
    number = 0
    for s in a:
        alphabet_dict[s] = alphabet_dict[s] + 1
    
    for s in b:
        alphabet_dict[s] = alphabet_dict[s] - 1

    for k, b in alphabet_dict.iteritems():
        number += abs(b)
    
    return number

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
