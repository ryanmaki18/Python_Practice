from isPalindrome import Solution
import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_positive_palindromes(self):             # FIXME: All stolen from other isPalindrome
        solution = Solution()
        self.assertTrue(solution.isPalindrome(0))
        self.assertTrue(solution.isPalindrome(121))
        self.assertTrue(solution.isPalindrome(12321))
        self.assertTrue(solution.isPalindrome(1221))

    def test_positive_non_palindromes(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(123))
        self.assertFalse(solution.isPalindrome(12345))

    def test_negative_number(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(-121))

    def test_single_digit_numbers(self):
        solution = Solution()
        for i in range(10):
            self.assertTrue(solution.isPalindrome(i))

if __name__ == '__main__':
    unittest.main()
    