class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next
            fast = fast.next

            if slow == fast:
                return True
            elif fast.next == None:
                return False

def insert_values(head, values):
    current = head

    for value in values:
        new_node = ListNode(value)
        current.next = new_node
        current = new_node

# Creating a simple linked list 
list_head = ListNode(2)
values_to_insert = [3,4,5]
insert_values(list_head, values_to_insert)

# Making a cycle in the list
temp = list_head
while temp.next != None:
    temp = temp.next

temp.next = list_head.next

# Detecting Cycles 
obj = Solution()
ans = obj.hasCycle(list_head)
print(ans)



        