# Linked List

+ [Merge Two Sorted Lists
](#merge-two-sorted-lists
)
## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode


class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result

    def create_linked_list(self, values):
        values.reverse()
        if not values:
            return None
        prev_node = ListNode(values[0])
        for i in range(1, len(values)):
            next_node = ListNode(values[i], prev_node)
            prev_node = next_node
        return prev_node

    def test_merge(self):
        list1 = self.create_linked_list([1, 2, 4, 7, 8])
        list2 = self.create_linked_list([1, 5, 8])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.get_linked_list_values(result), [1, 1, 2, 4, 5, 7, 8, 8])

    def test_empty_list(self):
        self.assertEqual(self.get_linked_list_values(self.solution.mergeTwoLists(None, None)), [])

    def test_one_value(self):
        list1 = self.create_linked_list([1])
        list2 = self.create_linked_list([])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(self.get_linked_list_values(result), [1])


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = ListNode()
        head = result

        while list1 is not None and list2 is not None:
            result.next = ListNode()
            result = result.next
            if list1.val < list2.val:
                result.val = list1.val
                list1 = list1.next
            else:
                result.val = list2.val
                list2 = list2.next

        while list1 is not None:
            result.next = ListNode()
            result = result.next
            result.val = list1.val
            list1 = list1.next

        while list2 is not None:
            result.next = ListNode()
            result = result.next
            result.val = list2.val
            list2 = list2.next

        return head.next
```

