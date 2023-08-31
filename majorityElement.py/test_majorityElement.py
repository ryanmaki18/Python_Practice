from majorityElement import Solution
import unittest

class MajorityElement(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [3,2,3]
        output = 3
        self.assertEqual(solution.majorityElement(nums), output)
        
    def test_example_2(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        output = 2
        self.assertEqual(solution.majorityElement(nums), output)
   
        
if __name__ == '__main__':
    unittest.main()
    