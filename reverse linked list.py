class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev = head ,None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev,curr = curr,temp
        return prev    
