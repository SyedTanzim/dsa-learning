# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        listLength = 0
        curr = head

        while curr:
            listLength += 1
            curr = curr.next

        j = 0    
        curr = head
        mid = listLength//2
        res = 0

        while curr:
            if j == mid:
                res = curr
                break
            else:
                curr = curr.next
                j += 1

        return res