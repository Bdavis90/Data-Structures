# """
# A stack is a data structure whose primary purpose is to store and
# return elements in Last In First Out order. 

# 1. Implement the Stack class using an array as the underlying storage structure.
#    Make sure the Stack tests pass.
# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.
# 3. What is the difference between using an array vs. a linked list when 
#    implementing a Stack?
# """

import sys
print(sys.path.append('hello'))
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# # class Stack:
# #     def __init__(self):
# #         self.size = 0
# #         self.storage = []

# #     def __len__(self):
# #         return self.size

# #     def push(self, value):
# #         self.size += 1
# #         self.storage.append(value)

# #     def pop(self):
# #         if self.size == 0:
# #             return None
# #         else:
# #             self.size -= 1
# #             return self.storage.pop()

# #     def __str__(self):
# #         return f'{self.storage}'

# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev

#     def get_value(self):
#         return self.value
    
#     def get_next(self):
#         return self.next

#     def __str__(self):
#         return f'value: {self.value}'
    

class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.size = len(self.storage)
        

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
           
        popped_value = self.storage.remove_from_tail()

        return popped_value 

    def __str__(self):
        return f'{self.storage}' 


s = Stack()
s.push(1)
s.push(2)
s.push(18)
s.pop()
print(s)