class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.data)
            copy.insert_at_end(node)
            current = current.next
        return copy
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
 
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.data
        while current2:
            temp = current2
            current2 = current2.next
            if temp.data == data:
                llist.remove(temp)
        current1 = current1.next
 
 
def find_union(llist1, llist2):
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union
 
    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)
 
    return union
 
 
def find_intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return LinkedList()
 
    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                node = Node(data)
                intersection.insert_at_end(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)
 
    return intersection
 
 
a_llist1 = LinkedList()
a_llist2 = LinkedList()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist2.insert_at_end(node)
 
union = find_union(a_llist1, a_llist2)
intersection = find_intersection(a_llist1, a_llist2)
 
print('Their union: ')
union.display()
print()
print('Their intersection: ')
intersection.display()
print()