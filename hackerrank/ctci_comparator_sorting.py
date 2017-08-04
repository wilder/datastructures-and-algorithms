'''
Given an array of  Player objects, write a comparator that sorts them in order of decreasing score; if or more players have the same score, sort those players alphabetically by name
'''
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __repr__(self):
        return repr((self.name, self.score))
    
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif b.score < a.score:
            return 1
        elif a.score == b.score:
            if b.name < a.name:
                return 1
            elif b.name > a.name:
                return -1
            else:
                return 0
        else:
            return 0
                
