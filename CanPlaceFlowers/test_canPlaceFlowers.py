from canPlaceFlowers import Solution
import unittest

class CanPlaceFlowers(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        flowerbed = [1,0,0,0,1]
        n = 1
        self.assertTrue(solution.canPlaceFlowers(flowerbed, n))
        
    def test_example_2(self):
        solution = Solution()
        flowerbed = [1,0,0,0,1]
        n = 2
        self.assertFalse(solution.canPlaceFlowers(flowerbed, n))
        
if __name__ == '__main__':
    unittest.main()
    