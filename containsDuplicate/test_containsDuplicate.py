from containsDuplicate import Solution
import unittest

class ContainsDuplicate(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [1,2,3,1]
        self.assertTrue(solution.containsDuplicate(nums))
        
    def test_example_2(self):
        solution = Solution()
        nums = [1,2,3,4]
        self.assertFalse(solution.containsDuplicate(nums))
        
    def test_example_3(self):
        solution = Solution()
        nums = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(solution.containsDuplicate(nums))

        
if __name__ == '__main__':
    unittest.main()
    