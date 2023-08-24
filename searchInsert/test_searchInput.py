from searchInsert import Solution
import unittest

class SearchInsert(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [1,3,5,6]
        target = 5
        output = 2
        self.assertEqual(solution.searchInsert(nums, target), output)
        
    def test_example_2(self):
        solution = Solution()
        nums = [1,3,5,6]
        target = 2
        output = 1
        self.assertEqual(solution.searchInsert(nums, target), output)
        
    def test_example_3(self):
        solution = Solution()
        nums = [1,3,5,6]
        target = 7
        output = 4
        self.assertEqual(solution.searchInsert(nums, target), output)
        
if __name__ == '__main__':
    unittest.main()
    