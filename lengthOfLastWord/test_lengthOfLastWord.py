from lengthOfLastWord import Solution
import unittest

class LengthOfLastWord(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        s = "Hello World"
        output = 5
        self.assertEqual(solution.lengthOfLastWord(s), output)
        
    def test_example_2(self):
        solution = Solution()
        s = "   fly me   to   the moon  "
        output = 4
        self.assertEqual(solution.lengthOfLastWord(s), output)
        
    def test_example_3(self):
        solution = Solution()
        s = "luffy is still joyboy"
        output = 6
        self.assertEqual(solution.lengthOfLastWord(s), output)
        
    def test_single_word(self):
        solution = Solution()
        s = " Hi "
        output = 2
        self.assertEqual(solution.lengthOfLastWord(s), output)
    
    def test_long_word(self):
        solution = Solution()
        s = "Input is supercalifragilisticexpialidocious"
        output = 34                                           ## TODO: Check if correct later
        self.assertEqual(solution.lengthOfLastWord(s), output)
    
        
if __name__ == '__main__':
    unittest.main()
    