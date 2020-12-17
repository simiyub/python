import unittest
import cap

class TestCap(unittest.TestCase):
    '''unit tests for Cap'''

    def test__one_word(self):
        '''test one word returns as expected.'''
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        '''test more than one word'''
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')