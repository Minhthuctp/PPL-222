import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        input = """
            foo: function integer(a:integer,b:integer){}

main: function void(){

	a: array[2,2] of integer;
    b: array[2] of integer = a[1];
    foo(1,2,3);
    }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))

