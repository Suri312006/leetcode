class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        
        self.stack2=[]

        i = len(self.stack1)-1
        while i >= 0:
            val = self.stack1[i]
            self.stack2.append(val)
            
            i-=1

        

    def pop(self) -> int:
        val = self.stack2.pop()

        self.stack1=[]

        #update stack1
        i = len(self.stack2)-1
        while i >= 0:
            temp = self.stack2[i]
            self.stack1.append(temp)
            i-=1

        return val

    def peek(self) -> int:
        return self.stack2[-1]

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True

        return False


    def p_stack1(self):
        return f's1: {self.stack1}'
    
    def p_stack2(self):
        return f's2: {self.stack2}'
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)

print(myQueue.peek()) # return 1

#problem with the pop function?
print(myQueue.pop()) # return 1, queue is [2]

print(myQueue.empty()) # return false


"""
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
"""