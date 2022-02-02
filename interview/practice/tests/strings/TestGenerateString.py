import unittest
from interview.practice.code.strings.GenerateString import generate


class TestGenerateString(unittest.TestCase):
    def test_generate1(self):
        characters = 'v reir vo t piss miss w piss e st f sipp o ai tst es ha te pp mii  isi  '
        string = 'mississippi is a river to the west of mississippi state'
        self.assertTrue(generate(characters, string))  # add

    def test_generate2(self):
        characters = ' time'
        string = 'emit'
        self.assertTrue(generate(characters, string))
            # assertion here


if __name__ == '__main__':
    unittest.main()
