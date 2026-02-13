"""
You are given the head of a singly linked-list. The list can be represented as:
L0 -> L1 -> ...->Ln-1 -> Ln
Reorder the list to be on the following form:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
You may not modify the values in the lists nodes. Only nodes themselves may be changed
"""

class reorderlist(object):
    def reorderlist(self, head):
        if not head or not head.next:
            return
        
        #Find middle of list
        slow, fast = head, head
        slow = slow.next
        fast = fast.next.next

        #split and reverse second half
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #merge two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

            