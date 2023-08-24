from firstOccurence import Solution
import unittest

class FirstOccurenceInString(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        haystack = "sadbutsad"
        needle = "sad"
        output = 0
        self.assertEqual(solution.removeElement(haystack, needle), output)
        
    def test_example_2(self):
        solution = Solution()
        haystack = "dndhdhjdhRYAN"
        needle = "RYAN"
        output = 9              # Check if correct index later
        self.assertEqual(solution.removeElement(haystack, needle), output)
        
    def test_example_3(self):
        solution = Solution()
        haystack = "leetcode"
        needle = "leeto"
        output = -1
        self.assertEqual(solution.removeElement(haystack, needle), output)
    
    def test_example_4(self):
        solution = Solution()
        haystack = "randomstring"
        needle = "qqq"
        output = -1
        self.assertEqual(solution.removeElement(haystack, needle), output)
        

if __name__ == '__main__':
    unittest.main()
    