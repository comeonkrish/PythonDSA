class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head
        
        # Initialize the `prev` and `current` pointers
        prev = None
        current = head

        # Move `current` to the `left`-th node and `prev` to one node before `left`
        for _ in range(left - 1):
            prev = current
            current = current.next
        
        # `prev` is now the node just before the `left`-th node
        # `current` is the `left`-th node, and we will start reversing from here
        
        # Save the connection before the sublist and the connection after the sublist
        connection_before = prev
        connection_after = current
        
        # Reverse the sublist between left and right
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev  # Reverse the pointer
            prev = current
            current = next_node

        # After the loop, `prev` is the new head of the reversed sublist
        # `connection_before` is the node before the reversed sublist, 
        # and `connection_after` is the node at the start of the reversed sublist

        # Connect the reversed sublist back to the list
        if connection_before:
            connection_before.next = prev
        else:
            head = prev  # If `left` is 1, then update the head to the new reversed sublist's head
        
        connection_after.next = current  # Connect the end of the reversed sublist to the next node

        return head

# Insert values into the list:
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

# Create the linked list
list1_head = listnode(1)
list1_head = insert_values(list1_head, [2, 3, 4, 5])

# Print the original linked list
print_list(list1_head)

# Reverse the sublist between position 2 and 4
rlist1 = Solution()
new_head = rlist1.reverseBetween(list1_head, 1, 2)

# Print the reversed linked list
print_list(new_head)
