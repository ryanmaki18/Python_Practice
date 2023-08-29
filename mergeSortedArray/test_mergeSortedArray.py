from mergeSortedArray import Solution
import unittest

class MergeSortedList(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        s = "Hello World"
        output = 5
        self.assertEqual(solution.merge(s), output)         ## FIXME: Not updated testcase

        
if __name__ == '__main__':
    unittest.main()
    