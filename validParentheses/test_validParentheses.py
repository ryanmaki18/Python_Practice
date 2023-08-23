from romanToInt import Solution
import unittest

class TestRomanToInt(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("()"), True)
        
    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("()[]{}"), True)
        
    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("([{}])"), True)
        
    def test_example43(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("(]"), False)

    def test_example_5(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("([{}])]"), False)

if __name__ == '__main__':
    unittest.main()
    