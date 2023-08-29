from mergeSortedArray import Solution
import unittest

class MergeSortedList(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        output: [1,2,2,3,5,6]
        self.assertEqual(solution.merge(nums1, m, nums2, n), output)
        
    def test_example_2(self):
        solution = Solution()
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        output: [1]
        self.assertEqual(solution.merge(nums1, m, nums2, n), output)
        
    def test_example_3(self):
        solution = Solution()
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        output: [1]
        self.assertEqual(solution.merge(nums1, m, nums2, n), output)

        
if __name__ == '__main__':
    unittest.main()
    