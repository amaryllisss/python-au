class ListNode(object):
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_len = self.get_linked_list_length(head)
        for i in range(list_len // 2):
            head = head.next
        return head

    def get_linked_list_length(self, head):
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        return length
