# Definiton of a singly linked list
class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev one step forward
            current = next_node       # Move current one step forward

        return prev              # After the loop, prev is the new head

# insert values into the list:
def insert_values(head, values):
    current = head
    for value in values:
        new_node = listnode(value)
        if current is None:
            head = new_node
        else:
            current.next = new_node
        current = new_node
    
    return head

def print_list(head):
    current = head
    temp_list = []
    while current:
        temp_list.append(current.val)
        current = current.next
    
    print(temp_list)

list1_head = listnode(1)

list1_head = insert_values(list1_head, [2,3,4,5])

# print the created linked list
print_list(list1_head)

# reverse the linked list
rlist1 = Solution()
new_head = rlist1.reverseList(list1_head)

# print the reversed linked list
print_list(new_head)