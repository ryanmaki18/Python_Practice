from isPalindrome import Solution
import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_1(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome("A man, a plan, a canal: Panama"))
        
    def test_palindrome_2(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome("racecar"))
        
    def test_palindrome_3(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome(" "))

    def test_palindrome_4(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome("race a car"))
        
    def test_palindrome_5(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome("Hello World"))
        
 
 
if __name__ == '__main__':
    unittest.main()
    