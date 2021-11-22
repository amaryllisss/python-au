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
