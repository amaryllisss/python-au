# Linked List

+ [Sort List
](#sort-list
)
## Sort List

https://leetcode.com/problems/sort-list/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution
from solution import ListNode


class TestSortList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result

    def test_merge_sort(self):
        test_list = [2, 1, 4, 7, 1]
        self.solution.merge_sort(test_list)
        self.assertEqual(test_list, [1, 1, 2, 4, 7])

    def test_empty_list(self):
        self.assertEqual(self.get_linked_list_values(self.solution.sortList(None)), [])

    def test_one_value(self):
        one = ListNode(1)
        self.assertEqual(self.get_linked_list_values(self.solution.sortList(one)), [1])

    def test_sortList(self):
        three = ListNode(2)
        two = ListNode(1, three)
        one = ListNode(3, two)
        self.assertEqual(self.get_linked_list_values(self.solution.sortList(one)), [1, 2, 3])

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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = self.get_linked_list_values(head)
        self.merge_sort(vals)
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

    def merge_sort(self, values):
        if len(values) > 1:
            middle = len(values) // 2
            list1 = values[:middle]
            list2 = values[middle:]
            self.merge_sort(list1)
            self.merge_sort(list2)
            first, second = 0, 0
            i = 0
            while first < len(list1) and second < len(list2):
                if list1[first] < list2[second]:
                    values[i] = list1[first]
                    first += 1
                else:
                    values[i] = list2[second]
                    second += 1
                i += 1
            while first < len(list1):
                values[i] = list1[first]
                first += 1
                i += 1
            while second < len(list2):
                values[i] = list2[second]
                second += 1
                i += 1
```

