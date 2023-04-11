import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        input = """
            bar: function integer(inherit a: auto)
            {
                
            }
            foo: function boolean(x: auto) inherit bar
            {
                super(2);
                if (a==2)
                {
                    return true;
                }
                else
                {
                    return false;
                }

            }
            main: function void() {
                r, s: integer;
                r = 2;
                a, b: array [5] of integer;
                a[0] = bar(2);
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))