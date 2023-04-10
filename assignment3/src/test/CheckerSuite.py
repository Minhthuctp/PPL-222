import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        input = """x: array [2,2] of float = {{1.2,1.3},{1.2,1}};
            main: function void(){
                b: array [2] of float = x[0];
            }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))