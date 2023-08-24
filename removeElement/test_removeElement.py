from removeElement import Solution
import unittest

class ValidParentheses(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        given_input = [1,1,2]
        output = 2
        self.assertEqual(solution.removeElement(given_input), output)
        


if __name__ == '__main__':
    unittest.main()
    