"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        tail.next = list1 if list1 else list2
        return dummy.next
 
