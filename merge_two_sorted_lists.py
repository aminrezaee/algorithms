"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        result_head = result_current = None
        while list1 is not None and list2 is not None:
            first_item = list1.val
            second_item = list2.val
            if first_item <= second_item:
                chosen_item = first_item
                list1 = list1.next
            else:
                chosen_item = second_item
                list2 = list2.next
            if result_head is None:
                result_head = ListNode(chosen_item)
                result_current = result_head
            else:
                result_current.next = ListNode(chosen_item)
                result_current = result_current.next
        if list1 is not None:
            result_current.next = list1
        elif list2 is not None:
            result_current.next = list2
        return result_head
        
        