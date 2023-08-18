from romanToInt import Solution
import unittest

class TestRomanToInt(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("III"), 3)

    def test_example_2(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("LVIII"), 58)

    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("MCMXCIV"), 1994)
        
    def test_example_4(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("VIII"), 8)
        
    def test_example_5(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt("MII"), 1002)

if __name__ == '__main__':
    unittest.main()
    