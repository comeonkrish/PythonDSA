class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

def insert_values(head, values):
    current = head
    for value in values:
        new_node = ListNode(value)
        if current is None:
            head = new_node
        else:
            current.next = new_node
        current = new_node
    return head

# Creating a simple linked list 
list_head = ListNode(2)
values_to_insert = [3,4,5]
list_head = insert_values(list_head, values_to_insert)

# Making a cycle in the list
temp = list_head
while temp.next is not None:
    temp = temp.next

# Connect the last node to the second node to create a cycle
temp.next = list_head.next

# Detecting Cycles 
obj = Solution()
ans = obj.hasCycle(list_head)
print(ans)
