import unittest

from extra import sort


class extraTest(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(sort(5), 'Invalid Input')

    def test_string_input(self):
        self.assertEqual(sort('string'), 'Invalid Input')

    def test_empty_list(self):
        self.assertEqual(sort([]), 'Empty list')

    def test_list_contains_strings(self):
        self.assertEqual(sort(['cat', 'dog']), 'List should contain numbers')

    def test_list_contains_non_numbers(self):
        self.assertEqual(sort(['a','c','@','&']), 'List should contain numbers')

    def test_output_missing_numbers(self):
        self.assertEqual(
            sort([2,7,12]), [0,1,3,4,5,6,8,9,10,11])

    