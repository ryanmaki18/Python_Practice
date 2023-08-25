from deleteDuplicates import Solution
import unittest

class DeleteDuplicates(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        head = [1,1,2]
        output = [1,2]
        self.assertEqual(solution.deleteDuplicates(head), output)
        
    def test_example_2(self):
        solution = Solution()
        head = [1,1,2,3,3]
        output = [1,2,3]
        self.assertEqual(solution.deleteDuplicates(head), output)
        
if __name__ == '__main__':
    unittest.main()
    