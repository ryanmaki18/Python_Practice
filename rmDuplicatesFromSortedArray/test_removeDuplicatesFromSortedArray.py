from removeDuplicatesFromSortedArray import Solution
import unittest
 
class RemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        given_input = [1,1,2]
        output = 2
        self.assertEqual(solution.removeDuplicates(given_input), output)
        
    def test_example_2(self):
        solution = Solution()
        given_input = [0,0,1,1,1,2,2,3,3,4]
        output = 5
        self.assertEqual(solution.removeDuplicates(given_input), output)
        
    def test_example_all_same(self):
        solution = Solution()
        given_input = [0,0,0,0,0,0,0]
        output = 1
        self.assertEqual(solution.removeDuplicates(given_input), output)
        
    def test_example_all_diff(self):
        solution = Solution()
        given_input = [0,1,2,3,4,5,6,7,8,9]
        output = 10
        self.assertEqual(solution.removeDuplicates(given_input), output)

if __name__ == '__main__':
    unittest.main()
    