For 2 linkedlists of size m, and n respectively:
Two new data structures are created:
a dictionary called tracker, which tracks elements in both LInked LIsts. 
A LinkedList called intersected which stores the intersection of both lists. 

These 2 structures in the worst case are O(n + m). This is because in the worst case, the lists could intersect at every value, and the LinkedList would be full, O(n + m). Because an intersecting item is popped off the tracker dictionary, then in this case it will be empty. 
If there is completely no intersection then the tracker list will be O(n) space complexity.

Time complexity seems to be O(n + m). This is because I go through each Linked List, then also for every step of going through the Linked list, I check the tracker list for an element. 

