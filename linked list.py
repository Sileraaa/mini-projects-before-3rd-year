"""
This is the first time I implemented a SINGLY Linked List, this was very confusing, especially the iteration of each nodes and those frickin edge cases.
I will update another version of this soon. For now.. I will leave the linkedlist implementation through Hard-code.

Valuable lesson learned:
I started to realize how data is stored in a memory and how a pointer store the address of data somewhere in the computer memory. 

For example:
a=5
b=a

- This means that b and a has the same address pointing at the intger '5'

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"The content: {self.data}"


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def append(self, data):
        new_node = Node(data)
        #You want the address of the new_node to be stored 
        self.tail.next = new_node 
        #You just updated the address of the node 
        self.tail = new_node

    def traverse(self):
        print("This is the chain of your linked list!!!")
        current = self.head
        #While the current pointer is still existing, direct the current to the next current address
        while current != None:
            #Prints the state of the current (node object) before moving on

            print(current)
            current = current.next
    
    def delete(self, target):
    #Ai helped me implement the edge cases from this method
        current = self.head
        previous = None
        # Case 1: The list is empty
        if current is None:
            print("List is empty!")
            return
        # Case 2: Deleting the Head
        if current.data == target:
            self.head = current.next
            # If the list only had one item, update the tail too
            if self.head is None:
                self.tail = None
            return
        # Case 3: Searching for the target
        while current is not None and current.data != target:
            previous = current
            current = current.next
        # Case 4: Target not found
        if current is None:
            print(f"Could not find {target} in the list.")
            return
        # Case 5: Standard Deletion (unlinking the node)
        # We create a 'bridge' over the 'current' node
        previous.next = current.next
        # Update tail if we just deleted the last node
        if current == self.tail:
            self.tail = previous

    def reverse(self):
        #Initialize our pointers. Assume that head is at the leftmost and tail is at the rightmost initially
        prev = None
        current = self.head #of course this is our temporary reference
        self.tail = self.head  # update tail to current head before reversing, this means you just position the tail at the left most already

        while current is not None:
            next_node = current.next #store the address of the next node
            current.next = prev #the address of the "next" node is pointing at our previous node 
            prev = current # we want to update previous with the LITERAL CURRENT WE ARE AT before moving to the next node
            current = next_node #we just want the current to have a fresh start from the next node that we stored
        self.head = prev #by this time, 'prev' is already positioned at the rightmost. we just want the head to start at the righmost, BECAUSE YOU JUST REVERSED IT DUHH


            

wow= LinkedList(67)
wow.append(35)
wow.append(23)
wow.traverse()
input(" ")
wow.reverse()
wow.traverse()