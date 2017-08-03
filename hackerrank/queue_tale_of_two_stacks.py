class MyQueue(object):
    def __init__(self):
        self.queue = []
        self.start_index = 0
    
    def peek(self):
        if self.start_index < len(self.queue):
            print self.queue[self.start_index] 
        
    def put(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        self.start_index += 1
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.dequeue()
    else:
        queue.peek()
