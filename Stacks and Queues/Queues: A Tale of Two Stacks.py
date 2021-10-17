class MyQueue(object):
    #     def __init__(self):
    #         self.inward = []
    #         self.outward = []
        
    
    #     def peek(self):
    #         if not self.outward:
    #             self.outward = list(reversed(self.inward))
    #             self.inward = []
    #         return self.outward[-1] 


    #     def pop(self):
    #         head = self.peek()
    #         del self.outward[-1]
    #         return head


    #     def put(self, value):
    #         self.inward.append(value)
    
    def __init__(self):
        self.queue = []

    def peek(self):
        return self.queue[-1]
        
    def pop(self):
        del self.queue[-1]
        
    def put(self, value):
        self.queue.insert(0, value)
    
    
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
