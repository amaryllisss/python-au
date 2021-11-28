# Linked List

+ [Palindrome Linked List
](#palindrome-linked-list
)
## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode


class TestisPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_one_value(self):
        one = ListNode(1)
        self.assertEqual(self.solution.isPalindrome(one), True)

    def test_isntPalindrom(self):
        four = ListNode(4)
        three = ListNode(3, four)
        two = ListNode(5, three)
        one = ListNode(3, two)
        self.assertEqual(self.solution.isPalindrome(one), False)

    def test_isPalindrom(self):
        five = ListNode(3)
        four = ListNode(4, five)
        three = ListNode(5, four)
        two = ListNode(4, three)
        one = ListNode(3, two)
        self.assertEqual(self.solution.isPalindrome(one), True)


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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = self.get_linked_list_values(head)
        vals_len = len(vals)
        for i in range(vals_len):
            if vals[i] != vals[vals_len - 1 - i]:
                return False
        return True

    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result
```

