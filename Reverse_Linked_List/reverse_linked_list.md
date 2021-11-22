# Linked List

+ [Reverse Linked List
](#reverse-linked-list
)
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/


```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        values = self.get_linked_list_values(head)
        values.reverse()
        head1 = self.create_linked_list(values)
        return head1

    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result

    def create_linked_list(self, values):
        values.reverse()
        if values == []:
            return None
        prev_node = ListNode(values[0])
        for i in range(1, len(values)):
            next_node = ListNode(values[i], prev_node)
            prev_node = next_node
        return prev_node
```

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        result = self.solution.reverseList(self.solution.create_linked_list([]))
        expected = self.solution.create_linked_list([])
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_one_value(self):
        result = self.solution.reverseList(self.solution.create_linked_list([1]))
        expected = self.solution.create_linked_list([1])
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_two_values(self):
        result = self.solution.reverseList(self.solution.create_linked_list([1, 2]))
        expected = self.solution.create_linked_list([2, 1])
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_odd_number_of_values(self):
        result = self.solution.reverseList(self.solution.create_linked_list([1, 2, 3, 4, 5]))
        expected = self.solution.create_linked_list([5, 4, 3, 2, 1])
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_even_number_of_values(self):
        result = self.solution.reverseList(self.solution.create_linked_list([1, 2, 3, 4, 5, 6]))
        expected = self.solution.create_linked_list([6, 5, 4, 3, 2, 1])
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>

