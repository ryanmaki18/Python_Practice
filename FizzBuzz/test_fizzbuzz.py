from fizzbuzz import Solution
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        n = 3
        expected_output = ["1", "2", "Fizz"]
        self.assertEqual(solution.fizzBuzz(n), expected_output)

    def test_case_2(self):
        solution = Solution()
        n = 5
        expected_output = ["1", "2", "Fizz", "4", "Buzz"]
        self.assertEqual(solution.fizzBuzz(n), expected_output)

    def test_case_3(self):
        solution = Solution()
        n = 15
        expected_output = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(solution.fizzBuzz(n), expected_output)

if __name__ == '__main__':
    unittest.main()





