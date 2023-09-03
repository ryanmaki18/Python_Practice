from countingBits import Solution
import unittest

class CountingBits(unittest.TestCase):
    def test_example_1(self):
        '''
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        '''
        solution = Solution()
        n = 2
        output = [0,1,1]
        self.assertEqual(solution.countBits(n), output)
        
    def test_example_2(self):
        '''
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
        '''
        solution = Solution()
        n = 5
        output = [0,1,1,2,1,2]
        self.assertEqual(solution.countBits(n), output)

        
if __name__ == '__main__':
    unittest.main()
    