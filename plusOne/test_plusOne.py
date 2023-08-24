from plusOne import Solution
import unittest

class PlusOne(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        digits = [1,2,3]
        output = [1,2,4]
        self.assertEqual(solution.plusOne(digits), output)

    def test_example_2(self):
        solution = Solution()
        digits = [4,3,2,1]
        output = [4,3,2,2]
        self.assertEqual(solution.plusOne(digits), output)
    
    def test_example_3(self):
        solution = Solution()
        digits = [9]
        output = [1,0]
        self.assertEqual(solution.plusOne(digits), output)

if __name__ == '__main__':
    unittest.main()
    