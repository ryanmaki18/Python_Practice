from longestCommonPrefix import Solution
import unittest

class TestLongestCommonPrefix(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower","flow","flight"]), "fl")
        
    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["preheat", "prefix", "preapprove"]), "pre")
                         
    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["dog","racecar","car"]), "")
    
    def test_empty_strings(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["", "abc", "def"]), "")
    
    def test_empty_input(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix([""]), "")
        
    def test_single_string(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["apple"]), "apple")

if __name__ == '__main__':
    unittest.main()
    