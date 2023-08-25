from climbStairs import Solution
import unittest

class ClimbStairs(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        n = 2
        output = 2
        self.assertEqual(solution.climbStairs(n), output)
        
    def test_example_2(self):
        solution = Solution()
        n = 3
        output = 3
        self.assertEqual(solution.climbStairs(n), output)
        
    def test_example_3(self):
        solution = Solution()
        n = 8
        output = 34
        self.assertEqual(solution.climbStairs(n), output)
        
    def test_example_3(self):
        solution = Solution()
        n = 38
        output = 63245986
        self.assertEqual(solution.climbStairs(n), output)
    
if __name__ == '__main__':
    unittest.main()
    