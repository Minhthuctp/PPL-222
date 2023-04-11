import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        input = """
                        bar: function integer(inherit a: auto)
            {
                
            }
            foo: function integer(x: auto) inherit bar
            {
                super(2);
                i: integer;
                for (x = 1, i < 10, i+1)
                    a = 1; 

            }
            main: function void() {
                r, s: integer;
                r = 2;
                a, b: array [5] of integer;
                a[0] = foo(1);
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))

