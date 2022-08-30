


from typing import Set


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None and llist_2.head is None:
        return "Empty lists"
    elif llist_1.head is None:
        return llist_2
    elif not llist_2.head:
        return llist_1

    unionll = LinkedList()
    current1 = llist_1.head
    current2 = llist_2.head
    while current2 is not None:
        if current1 is None:
            unionll.append(current2)
            current2 = current2.next
        else:
            unionll.append(current1)
            current1 = current1.next
    return unionll

def intersection(llist_1, llist_2):
    if llist_1.head is None and llist_2.head is None:
        return "Empty intersection"
    elif llist_1.head is None or llist_2.head is None:
        return "No intersection"
    intersected = LinkedList()
    tracker  = {}
    current1 = llist_1.head
    current2 = llist_2.head
    while current1 is not None:
        if current1.value not in tracker:
            tracker[current1.value] = 1
            current1 = current1.next
        elif current1.value in tracker:
            tracker[current1.value] += 1
            current1 = current1.next

    while current2 is not None:
        if current2.value in tracker:
            intersected.append(current2)
            tracker.pop(current2.value)
            current2 = current2.next
        current2 = current2.next
    if intersected.head is not None:
        return intersected
    return "No intersection found"
        
    
            

            
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

empty_llist = LinkedList()

# print (union(linked_list_3,linked_list_4))
print(union(empty_llist, empty_llist))
print (intersection(linked_list_3,linked_list_4))