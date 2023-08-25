from mySqrt import Solution
import unittest

class MySqrt(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        num = 4
        output = 2
        self.assertEqual(solution.mySqrt(num), output)
    
    def test_example_2(self):
        solution = Solution()
        num = 9
        output = 3
        self.assertEqual(solution.mySqrt(num), output)
    
    def test_example_3(self):
        solution = Solution()
        num = 9
        output = 3
        self.assertEqual(solution.mySqrt(num), output)
    
    def test_example_4(self):
        solution = Solution()
        num = 25
        output = 5
        self.assertEqual(solution.mySqrt(num), output)
        
    def test_example_5(self):
        solution = Solution()
        num = 144
        output = 12
        self.assertEqual(solution.mySqrt(num), output)
        
    def test_example_6(self):
        solution = Solution()
        num = 150
        output = 12
        self.assertEqual(solution.mySqrt(num), output)
    
if __name__ == '__main__':
    unittest.main()
    