
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return f'{self.value}'

class LinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def add_to_tail(self, value):
    new_node = Node(value)
    self.length += 1
    # if self.head is None:
    #   self.head = new_node

    # while head.next != None:
    #   head = head.next
    #   print(head)
    # head.next = new_node
    if self.tail:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node

  def delete(self, node):
    self.length -= 1
    if not self.head:
      print('List is empty')
      return

    if self.head == self.tail:
      self.head = None
      self.tail = None
  
    if node == self.head:
      self.head = node.next
      self.head.prev = None

    if node == self.tail:
      self.tail = node.prev
      self.tail.next = None  

  
  def printList(self):
    head = self.head
    while head.next != None:
      print(head.value)
      head = head.next

  def contains(self, value):
    # curr_value = self.head.value
    head = self.head
    while head:
      if head.value == value:
        return True
      head = head.next
    
    return False

  def remove_head(self):
    # value = self.head.value
    if self.head.next:
      self.head = self.head.next
    else: 
      self.head = None

    return self.head.value

  def get_max(self):
    current = self.head
    if current is None:
      return None

    curr_value = self.head.value
    while current:
        if curr_value < current.value:
            curr_value = current.value
        current = current.next
    return curr_value

node = Node(6)
ll = LinkedList(node)
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(7)
ll.printList()
ll.remove_head()
print(ll.contains(7))
print(ll.get_max(),'max')
ll.printList()


