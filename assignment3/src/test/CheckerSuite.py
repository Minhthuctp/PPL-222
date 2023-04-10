import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        input = """
            foo: function boolean(x: integer)
        {
            r, s: integer;
            r = 2;
            a, b: array [5] of integer;
            a[0] = s;
        }
        main: function void() {
            r, s: integer;
            r = 2;
            a, b: array [5] of integer;
            a[0] = s;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))