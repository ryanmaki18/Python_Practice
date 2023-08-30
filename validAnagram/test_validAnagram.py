from validAnagram import Solution
import unittest

class ValidAnagram(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        s = "anagram"
        t = "nagaram"
        self.assertTrue(solution.isAnagram(s, t))
        
    def test_example_2(self):
        solution = Solution()
        s = "rat"
        t = "car"
        self.assertFalse(solution.isAnagram(s, t))


if __name__ == '__main__':
    unittest.main()
    