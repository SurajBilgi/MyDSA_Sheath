""" 
234. Palindrome Linked List.

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next

        return new_list == new_list[::-1]