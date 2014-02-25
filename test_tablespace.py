import unittest

import os

from tablespace import TableSpace

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'ibdata55')


class TestTablespace(unittest.TestCase):
    
    def test_openfile(self):
        """docstring for test_openfile"""
        t = TableSpace(TESTDATA_FILENAME)
        f = file
        self.assertEqual(type(t.file), f)


if __name__ == '__main__':
    unittest.main()