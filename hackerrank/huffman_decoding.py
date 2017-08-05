"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    track_head = root
    result = ''
    i= 0
    while i < len(s):
        if s[i] == '1':
            if root.right == None:
                result+=root.data
            root = root.right
        else:
            if root.left == None:
                result+=root.data
            root = root.left
        
        if root == None:
            root = track_head
        else:
            i+=1
            
    result+= root.data
    print result
