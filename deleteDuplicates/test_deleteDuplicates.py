from deleteDuplicates import Solution
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DeleteDuplicates(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()

        # Create linked list from a list of values
        values = [1, 1, 2]
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        head = nodes[0]

        # Create the expected linked list
        expected_values = [1, 2]
        expected_nodes = [ListNode(val) for val in expected_values]
        for i in range(len(expected_nodes) - 1):
            expected_nodes[i].next = expected_nodes[i + 1]
        expected_head = expected_nodes[0]

        # Call the deleteDuplicates function
        result_head = solution.deleteDuplicates(head)

        # Compare the result with the expected linked list
        self.assertEqual(result_head.val, expected_head.val)
        current_result = result_head
        current_expected = expected_head
        while current_result and current_expected:
            self.assertEqual(current_result.val, current_expected.val)
            current_result = current_result.next
            current_expected = current_expected.next

    def test_example_2(self):
        solution = Solution()

        # Create linked list from a list of values
        values = [1, 1, 2, 3, 3]
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        head = nodes[0]

        # Create the expected linked list
        expected_values = [1, 2, 3]
        expected_nodes = [ListNode(val) for val in expected_values]
        for i in range(len(expected_nodes) - 1):
            expected_nodes[i].next = expected_nodes[i + 1]
        expected_head = expected_nodes[0]

        # Call the deleteDuplicates function
        result_head = solution.deleteDuplicates(head)

        # Compare the result with the expected linked list
        self.assertEqual(result_head.val, expected_head.val)
        current_result = result_head
        current_expected = expected_head
        while current_result and current_expected:
            self.assertEqual(current_result.val, current_expected.val)
            current_result = current_result.next
            current_expected = current_expected.next
if __name__ == '__main__':
    unittest.main()
    