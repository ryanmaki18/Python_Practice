from removeDuplicatesFromSortedArray import Solution
import unittest

class ValidParentheses(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertTrue(solution.isValid("()"))
        
    def test_example_2(self):
        solution = Solution()
        self.assertTrue(solution.isValid("()[]{}"))
        
    def test_example_3(self):
        solution = Solution()
        self.assertTrue(solution.isValid("([{}])"))
        
    def test_example43(self):
        solution = Solution()
        self.assertFalse(solution.isValid("(]"))

    def test_example_5(self):
        solution = Solution()
        self.assertFalse(solution.isValid("([{}])]"))

if __name__ == '__main__':
    unittest.main()
    