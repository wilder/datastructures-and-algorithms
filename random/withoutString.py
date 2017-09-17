# -*- coding: utf-8 -*-
'''
Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"

-- solutions thoughs --
started: 21:33
finished: 21:41

-- implementation --
started: 22:05
finished: 22:21

total: 24 min

#solution 1
    summary: Use two variable to keep track of the index of
    replacement and base string. If the character at position 
    of ibase if different from irep, increment ibase and add
    it to a result string.
    If they match, copy ibase and iterate cibase and irep. 
    If in the next iteration the str[irep] and str[cibase]
    are different, reset the irep and
    increment ibase. If irep == len(replacement), increment
    ibase by the length of the replacement string
    time complexity: O(n)
'''

def without_string(base, remove):
    final_str = ''
    base_index = 0
    while base_index < len(base):

        #if the current letter is equal to the first letter of the remove string 
        if base[base_index] == remove[0]:
            #copy the current index
            base_indexc = base_index
            
            #iterate over the string until they're different or end of the string
            rm_index = 0

            string_being_removed = ""
            while rm_index < len(remove):
                if remove[rm_index] != base[base_indexc] or base_indexc+1 == len(base):
                    final_str += string_being_removed
                    break
                string_being_removed += base[base_indexc]
                base_indexc+=1
                rm_index += 1

            base_index += rm_index

        #if the current character is not part of the remove string, add it to the final string
        final_str += base[base_index]
        base_index += 1
    return final_str

assert(without_string("Hellallo there", "llo") == "Hella there")
assert(without_string("Hello there", "el") == "Hlo there")
assert(without_string("Hello there", "x") == "Hello there")
