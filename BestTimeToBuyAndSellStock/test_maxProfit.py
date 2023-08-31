from maxProfit import Solution
import unittest

class BestTimeToBuyAndSellStock(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        prices = [7,1,5,3,6,4]
        output = 5
        self.assertEqual(solution.maxProfit(prices), output)
        
    def test_example_2(self):
        solution = Solution()
        prices = [7,6,4,3,1]
        output = 0
        self.assertEqual(solution.maxProfit(prices), output)
        
    
        
if __name__ == '__main__':
    unittest.main()
    