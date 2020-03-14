# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList


# class Queue:
#     def __str__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()

#     def enqueue(self, value): #should add an item to the back of the queue.
#         return self.storage.add_to_tail(value)

#     def dequeue(self): #should remove and return an item from the front of the queue.  
#         return self.storage.remove_from_head()

#     def len(self): #returns the number of items in the queue.
#         return self.size


# queue = Queue()
# queue.enqueue(9)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(4)
# print(queue)

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return "empty"
        curr_node = self.head
        #" (3) <-> (5) <-> ..."
        output = ''
        output += f'( {curr_node.value} ) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'( {curr_node.value} ) <-> '
        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return  
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
       # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __str__(self):
        if self.size == 0:
            return "empty"
        curr_node = self.storage.head
        output = ''
        output += f'Queue < {curr_node.value} >'
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f', < {curr_node.value} >'
        return output

    def enqueue(self, value): #should add an item to the back of the queue.
        self.storage.add_to_tail(value)
        self.size = self.storage.length

    def dequeue(self): #should remove and return an item from the front of the queue.  
        if self.size > 0:    
            value = self.storage.head.value
            self.storage.remove_from_head()
            self.size = self.storage.length
            return value


    def len(self): #returns the number of items in the queue.
        return self.size


queue = Queue()
queue.enqueue(9)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
print(queue)