"""
Yeah no explanation on this one. Easy stuff and Light Work.

"""
import pickle # I got lazy for this version
import os #same thing

class Stack:
    def __init__(self, name):
        self._items=[]
        self.name=name

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("There are no items in the stack!")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("There are no items in the stack!")
        return self._items[-1]

    def is_empty(self):
        return len(self._items)==0
    
    def size(self):
        return len(self._items)
    
    def display(self):
        if self.is_empty():
            return ValueError("There are no items in the stack!")
        return self._items

    def clear(self):
        self._items.clear()
        return f"Stack Cleared!"
    

class Queue:
    def __init__(self):
        self._items=[]

    def enqueue(self, item):
        self._items.append(item)

    def is_empty(self):
        return len(self._items)==0
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("There are no items in the queue!")
        return self._items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("There are no items in the queue!")
        return self._items[0]

    def size(self):
        return len(self._items)
    
    def display(self):
        if self.is_empty():
            raise ValueError("There are no items in the Queue!")
        return self._items
    
    def clear(self):
        self._items.clear()
        return f"Queue Cleared!"
    
    
# --- Stack Tests ---
print("=== STACK ===")
s = Stack("mystack")
s.push(1)
s.push(2)
s.push(3)
print("Size:", s.size())        # 3
print("Peek:", s.peek())        # 3
print("Pop:", s.pop())          # 3
print("Display:", s.display())  # [1, 2]
s.clear()
print("After clear:", s.display())  # should raise ValueError

# --- Queue Tests ---
print("\n=== QUEUE ===")
q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print("Size:", q.size())         # 3
print("Peek:", q.peek())         # a
print("Dequeue:", q.dequeue())   # a
print("Display:", q.display())   # ['b', 'c']
q.clear()
print("After clear:", q.display())  # should raise ValueError

    
