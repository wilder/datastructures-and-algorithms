'''
summary: iterate the string and while iterating, keep track of the
         already seen characters. when going to the next position,
         add to the 'solution' string the last seen characters + the
         current character and update the last seen.
         
time complexity: O(n)         
'''


def string_splosion(string):
  
  seen = ''
  solution = ''
  
  for i in string:
    solution += seen + i
    seen += i
    
  return solution

