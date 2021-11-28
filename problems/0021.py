"21. Merge Two Sorted Lists"

# You are given the heads of two sorted linked lists list1 and list2.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (not list1 or not list2) :
            return list1 if list1 else list2
        
        res = head = ListNode()
        
        while (list1 and list2) :
            if (list1.val <= list2.val) :
                res.next = list1
                list1 = list1.next
            else :
                res.next = list2
                list2 = list2.next
            res = res.next
        
        res.next = list1 if list1 else res.next
        res.next = list2 if list2 else res.next
        
        return head.next