from twoSum import Solution
import unittest

class TwoSum(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        output = [0, 1]
        self.assertEqual(solution.twoSum(nums, target), output)
        
    def test_example_2(self):
        solution = Solution()
        nums = [3, 2, 4]
        target = 6
        output = [1, 2]
        self.assertEqual(solution.twoSum(nums, target), output)
        
    def test_example_3(self):
        solution = Solution()
        nums = [3, 3]
        target = 6
        output = [0, 1]
        self.assertEqual(solution.twoSum(nums, target), output)
        
    def test_example_4(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 8
        output = []
        self.assertEqual(solution.twoSum(nums, target), output)
        
if __name__ == '__main__':
    unittest.main()
    