import unittest
from solution import Solution
from solution import ListNode


class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        result = self.solution.reverseList(ListNode())
        expected = ListNode()
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_one_value(self):
        result = self.solution.reverseList(ListNode(1))
        expected = ListNode(1)
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(expected))

    def test_two_values(self):
        two = ListNode(2)
        one = ListNode(1, two)
        two_res = ListNode(1)
        one_res = ListNode(2, two_res)
        result = self.solution.reverseList(one)
        self.assertEqual(self.solution.get_linked_list_values(result), self.solution.get_linked_list_values(one_res))


if __name__ == "__main__":
    unittest.main()