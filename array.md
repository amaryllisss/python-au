# Array

+ [Squares of a Sorted Array
](#squares-of-a-sorted-array
)
## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution

class TestSortedSquares(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.solution.sortedSquares([]), [])

    def test_mixed_nums(self):
        result = self.solution.sortedSquares([-4,-1,0,3,10])
        expected = [0,1,9,16,100]
        self.assertEqual(result, expected)

    def test_positive_nums(self):
        self.assertEqual(self.solution.sortedSquares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative_nums(self):
        self.assertEqual(self.solution.sortedSquares([-10, -5, -2]), [4, 25, 100])

    def test_find_with_positive(self):
        self.assertEqual(self.solution.get_first_non_negative([2, 3, 5]), 0)

    def test_find_with_negative(self):
        self.assertEqual(self.solution.get_first_non_negative([-10, -5, -2]), 3)

    def test_find_with_non_negative(self):
        self.assertEqual(self.solution.get_first_non_negative([0, 1, 2, 3]), 0)

    def test_find_with_mixed(self):
        self.assertEqual(self.solution.get_first_non_negative([-10, -5, 0, 1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
```

</blockquote></details>


```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = self.get_first_non_negative(nums)
        left = right - 1
        result = []

        while left >= 0 and right < len(nums):
            if nums[left] ** 2 < nums[right] ** 2:
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1

        while right < len(nums):
            result.append(nums[right] ** 2)
            right += 1

        return result

    def get_first_non_negative(self, nums):
        for i, val in enumerate(nums):
            if val >= 0:
                return i
        return len(nums)
```

