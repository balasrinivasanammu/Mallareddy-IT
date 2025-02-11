class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "Queue is empty"
    
    def display(self):
        return self.queue
    
    def is_empty(self):
        return len(self.queue) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.display())  # [2, 3]


from collections import deque

q = deque()
q.append(1)  # Enqueue
q.append(2)
print(q.popleft())  # Dequeue (1)
print(q)  # deque([2])


#----------------------

import queue

q = queue.Queue()
q.put(1)
q.put(2)
print(q.get())  # Dequeue (1)
print(q.queue)  # Remaining items: [2]


#--------------------------

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    def enqueue(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            return "Queue is full"
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "Queue is empty"
    
    def display(self):
        return self.queue


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.enqueue(4))  # "Queue is full"
print(q.display())  # [1, 2, 3]


#------------------------------ q using LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def display(self):
        current = self.front
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.display())  # [2, 3]
