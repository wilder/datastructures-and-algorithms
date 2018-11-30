'''
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

ab*yc*d

a -> b*
 \  |
  > y ->

'''

class StateNode:
    
    @staticmethod
    def fromString(string):
        head = StateNode(None)
        current = head
        for char_index in range(0, len(string)):
            char = string[char_index]
            added = current.add(char)
            current = added
        current.isEnd = True
        return head


    def __init__(self, value):
        self.value = value
        self.parent = None
        self.isStar = False
        self.next = None # just makes sense for period
        self.children = {} # just makes sense for star parents
        self.isPeriod = False # rename to 'canAcceptPeriod'
        self.isEnd = False

    def add(self, value):

        if value == '*':
            self.isStar = True
            return self

        if value ==  '.':
            self.isPeriod = True
        
        newNode = StateNode(value)

        if self.isStar and self.parent:
            self.parent.children[value] = newNode

        self.children[value] = newNode

        if self.parent and self.parent.isPeriod:
            self.parent.next = newNode

        return newNode

    def read(self, value):
        
        print('reading ', value)
        if '.' in self.children and self.value == None:
            return self.children['.']

        if value in self.children:
            nextState = self.children[value]
            return nextState

        elif self.isStar and (self.value == value or self.value == '.'):
            return self

        elif self.isPeriod:
            return self.children['.']

        else:
            return None
        

def matches(pattern, string):
    stateMachine = StateNode.fromString(pattern)

    currState = stateMachine
    for char in string:
        if not currState:
            return False
        currState = currState.read(char)
    
    return currState != None and currState.isEnd

if __name__ == "__main__":
    print('ra. - ray: ', matches("ra.", "ray"))
    print('ra. - raymond: ', matches("ra.", "raymond"))
    print('.*at - chat: ', matches(".*at", "chat"))
    print('.*at - chats: ', matches(".*at", "chats"))
    assert matches("a*b", "aaaaaaaaaaaaaab") == True
    assert matches("a.c", "abc") == True
