# Linked List

+ [Intersection of Two Linked Lists
](#intersection-of-two-linked-lists
)
## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode


class TestIntersectionNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        test_list1 = None
        test_list2 = None
        self.assertEqual(self.solution.getIntersectionNode(test_list1, test_list2), None)

    def test_equal_values(self):
        node1 = ListNode(5)
        node2 = ListNode(4, node1)

        node3 = ListNode(1, node2)
        node4 = ListNode(1, node2)

        node5 = ListNode(4, node3)
        node6 = ListNode(6, node4)

        self.assertEqual(self.solution.getIntersectionNode(node5, node6), node2)

    def test_no_intersection(self):
        node1 = ListNode(7)
        node2 = ListNode(4, node1)
        node3 = ListNode(11, node2)

        node4 = ListNode(7)
        node5 = ListNode(4, node4)
        node6 = ListNode(11, node5)
        self.assertEqual(self.solution.getIntersectionNode(node3, node6), None)

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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        vals_a = []

        while headA is not None:
            vals_a.append(headA)
            headA = headA.next

        vals_a = set(vals_a)

        while headB is not None:
            if headB in vals_a:
                return headB
            headB = headB.next

        return None
```

