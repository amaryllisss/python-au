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

    def test_merge(self):
        list1 = [1, 2, 4, 7, 8]
        list2 = [1, 5, 8]
        self.assertEqual(self.solution.merge(list1, list2), [1, 1, 2, 4, 5, 7, 8, 8])

    def test_empty_list(self):
        self.assertEqual(self.solution.get_linked_list_values(self.solution.mergeTwoLists(None, None)), [])

    def test_one_value(self):
        one = ListNode(1)
        self.assertEqual(self.solution.get_linked_list_values(self.solution.mergeTwoLists(one, None)), [1])

    def test_sortList(self):
        three = ListNode(6)
        two = ListNode(5, three)
        one = ListNode(3, two)

        five = ListNode(5)
        four = ListNode(2, five)

        self.assertEqual(self.solution.get_linked_list_values(self.solution.mergeTwoLists(one, four)), [2, 3, 5, 5, 6])

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
        first_list = self.get_linked_list_values(list1)
        second_list = self.get_linked_list_values(list2)
        vals = self.merge(first_list, second_list)
        return self.create_linked_list(vals)


    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result

    def create_linked_list(self, values):
        if values == []:
            return None
        values.reverse()
        prev_node = ListNode(values[0])
        for i in range(1, len(values)):
            next_node = ListNode(values[i], prev_node)
            prev_node = next_node
        return prev_node

    def merge(self, list1, list2):
        first, second = 0, 0
        result = []

        while first < len(list1) and second < len(list2):
            if list1[first] < list2[second]:
                result.append(list1[first])
                first += 1
            else:
                result.append(list2[second])
                second += 1

        while first < len(list1):
            result.append(list1[first])
            first += 1

        while second < len(list2):
            result.append(list2[second])
            second += 1

        return result
```

