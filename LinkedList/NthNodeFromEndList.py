"""Given the head of a linked list, remove the nth node 
from the end of the list and return its head."""

class Solution:
    def removeNthFromEnd(self, head):
        #I have initialized dummy to handle edge cases...
        dummy = ListNode(0,head)
        speed = dummy
        slowe = dummy

        #moving fast pointer two steps ahead
        for _  in range(n+1):
            speed = speed.next

        #moving both speed and slowe pointers until it reaches end
        while speed:
            speed = speed.next
            slowe = slowe.next

        #skip the nth node
        slowe.next = slowe.next.next

        return dummy.next
        

 
