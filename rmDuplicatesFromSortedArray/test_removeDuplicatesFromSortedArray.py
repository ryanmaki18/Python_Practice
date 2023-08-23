from removeDuplicatesFromSortedArray import Solution
import unittest

class RemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        given_input = [1,1,2]
        output = "2, [1,2,_]"
        self.assertEqual(solution.removeDuplicates(given_input), output)
        
    def test_example_2(self):
        solution = Solution()
        given_input = [0,0,1,1,1,2,2,3,3,4]
        output = "5, [0,1,2,3,4,_,_,_,_,_]"
        self.assertEqual(solution.removeDuplicates(given_input), output)

if __name__ == '__main__':
    unittest.main()
    