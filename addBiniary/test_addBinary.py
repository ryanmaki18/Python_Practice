from addBinary import Solution
import unittest

class AddBinary(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        a = "11"
        b = "1"
        output = "100"
        self.assertEqual(solution.addBinary(a, b), output)
        
    def test_example_2(self):
        solution = Solution()
        a = "1010"
        b = "1011"
        output = "10101"
        self.assertEqual(solution.addBinary(a, b), output)
    
if __name__ == '__main__':
    unittest.main()
    