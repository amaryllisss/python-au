import unittest
import generator_md as gmd


class TestGeneratorMd(unittest.TestCase):
    def test_get_md_code_block(self):
        data = 'Hello'
        self.assertEqual(gmd.get_md_code_block(data), '\n```python\nHello```\n')


    def test_get_formatted_test_block(self):
        data = 'Hello'
        self.assertEqual(gmd.get_formatted_test_block(data), '<details><summary>Test cases</summary><blockquote>\n\n```python\nHello```\n\n</blockquote></details>\n')


    def test_get_md_link(self):
        data = 'Squares of a Sorted Array'
        self.assertEqual(gmd.get_md_link(data), '+ [Squares of a Sorted Array](#squares-of-a-sorted-array)')


    def test_get_md_data(self):
        solution_file = open('test_source_solution.txt')
        solution = solution_file.readlines()
        solution_file.close()

        tests_file = open('test_source_tests.py')
        tests = tests_file.readlines()
        tests_file.close()

        expected_file = open('test_expected_md.txt')
        expected = expected_file.read()
        expected_file.close()

        self.assertEqual(gmd.get_md_data(solution, tests), expected)


if __name__ == "__main__":
    unittest.main()

