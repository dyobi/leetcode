"203. Remove Linked List Elements"

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Input: head = [1,2,6,3,4,5,6], val = 6 / Output: [1,2,3,4,5]
# Input: head = [7,7,7,7], val = 7 / Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None : return head
        else :
            temp = head
            
            while (temp) :
                if temp.val == val :
                    head = temp.next
                    temp = temp.next
                elif temp.next and temp.next.val == val :
                    temp.next = temp.next.next
                else :
                    temp = temp.next
                    
            return head