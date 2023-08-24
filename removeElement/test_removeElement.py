from removeElement import Solution
import unittest

class RemoveElement(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        given_input = [3,2,2,3]
        output = 2
        val = 3
        self.assertEqual(solution.removeElement(given_input, val), output)
        
    def test_example_2(self):
        solution = Solution()
        given_input = [0,1,2,2,3,0,4,2]
        output = 5
        val = 2
        self.assertEqual(solution.removeElement(given_input, val), output)
        
    def test_example_3(self):
        solution = Solution()
        given_input = [0,0,0,0]
        output = 0
        val = 0
        self.assertEqual(solution.removeElement(given_input, val), output)
        

if __name__ == '__main__':
    unittest.main()
    