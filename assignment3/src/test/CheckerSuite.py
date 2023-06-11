import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    """Test program"""
    def test_program_1(self):
        input=""""""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_program_2(self):
        input="""foo: function void()
        {
            
        }
        """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_program_3(self):
        input="""a:integer;"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_program_4(self):
        input="""a: float;
                 foo: function void() {}"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_program_5(self):
        input="""a: float;
                 main: function integer() {}"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,405))

    """Test variable declaration"""

    def test_vardecl_1(self):
        input="""
            a: float;
            b: integer;
            a: string;
            """
        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_vardecl_2(self):
        input="""
            c: string;
            d: string;
            a: string = c::d;
            e: boolean = 2;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(e, BooleanType, IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_vardecl_3(self):
        input="""
            a: auto;
            """
        expect="Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_vardecl_4(self):
        input="""
            a: integer = 1.2;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_vardecl_5(self):
        input="""
            a: float = 2;
            b: integer = 2;
            b: string;
            """
        expect="Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_vardecl_6(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = a + b;
            d: integer = c;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_vardecl_7(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {a,b};
            d: array [2] of float = {"a","b"};
            """
        expect="Illegal array literal: ArrayLit([Id(a), Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_vardecl_8(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {a,b,"d"};
            """
        expect="Illegal array literal: ArrayLit([Id(a), Id(b), StringLit(d)])"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_vardecl_9(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {{a,b},{a,b}};
            d: array [2] of integer = c[0];
            """
        expect="Illegal array literal: ArrayLit([ArrayLit([Id(a), Id(b)]), ArrayLit([Id(a), Id(b)])])"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_vardecl_10(self):
        input="""
            a: integer;
            b: array [2,2] of float;
            c: auto = b[2];
            d: integer = c[1];
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, ArrayCell(c, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    """Test function declaration"""
    def test_funcdecl_1(self):
        input="""
            a: function integer(b: integer, c:integer) inherit d {}
            main: function void()
            {
            
            }
            """
        expect="Undeclared Function: d"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_funcdecl_2(self):
        input="""
            a: integer;
            a: function integer(b: integer, c:integer){}
            main: function void()
            {
            
            }
            """
        expect="Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_funcdecl_3(self):
        input="""
            a: integer;
            b: function integer(c: integer, d:integer) inherit a{}
            main: function void()
            {
            
            }
            """
        expect="Undeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_funcdecl_4(self):
        input="""
            bar : function void (out n : integer, a:float) inherit foo{}
            foo : function auto (inherit n: float, n: integer){} 
            """
        expect="Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_funcdecl_5(self):
        input="""
            bar : function void (out n : integer, a:float) inherit foo{} 
            foo : function auto (inherit n: float){} 
            """
        expect="Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,420))


    def test_funcdecl_6(self):
        input="""
            bar : function void (a:float) inherit foo{} 
            foo : function auto (inherit n: float){} 
            """
        expect="Invalid statement in function: bar"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_funcdecl_7(self):
        input="""
            bar : function void (a:float) inherit foo{} 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_funcdecl_8(self):
        input="""
            bar : function void (a:float) inherit foo{
                super();
            } 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_funcdecl_9(self):
        input="""
            bar : function void (a:float) inherit foo{
                super();
            } 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_funcdecl_10(self):
        input="""
            bar : function void (a:float) inherit foo{
                preventDefault();
            } 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_funcdecl_11(self):
        input="""
            bar : function void (a:float) inherit foo{
                preventDefault(a);
            } 
            foo : function auto (){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_funcdecl_12(self):
        input="""
            bar : function void (a:float) inherit foo{
                super(a);
            } 
            foo : function auto (){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_funcdecl_13(self):
        input="""
            bar : function void (a:float) inherit foo{
                super(a,a);
            } 
            foo : function auto (a: float, b: integer){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_funcdecl_14(self):
        input="""
            bar : function void (a:float) inherit foo{
                super(a,a,a);
            } 
            foo : function auto (a: float, b: integer){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_funcdecl_15(self):
        input="""
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                    b = 1 + foo(1,2);
                    foo(1,2);
                }
                b=1.3;
            }

            """
        expect="Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_funcdecl_16(self):
        input="""
            bar: integer;
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                }
            }
            bar: function integer(inherit c: integer)
            {
            
            }
            """
        expect="Redeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_funcdecl_17(self):
        input="""
            bar: integer;
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                }
            }
            """
        expect="Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_funcdecl_18(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                }
            }
            """
        expect="Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_funcdecl_19(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                super();
                if (a==1)
                {
                    b: integer;
                }
            }
            """
        expect="Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_funcdecl_20(self):
        input="""
            bar: function integer(n: integer, n: integer) {}
            foo: function integer (a: integer, b: auto) inherit bar
            {
                super(1,2);
            }
            """
        expect="Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,435))

    """Test statement"""
    def test_stmt_1(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if (b==1)
                {
                
                }
                else
                {
                    if (a<2.0)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_stmt_2(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if (a==1)
                {
                
                }
                else
                {
                    if (a<2.0)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_stmt_3(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if ((a==1) && (b=="a"))
                {
                
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(==, Id(b), StringLit(a))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_stmt_4(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if ((b<2.0) && (b==a))
                {
                
                }
                else
                {
                    if (b==1)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(==, Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_stmt_5(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if ((1!=true) && (b==a))
                {
                
                }
                else
                {
                    if (b<2)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(<, Id(b), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_stmt_6(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                b = 1 + a;
            }
            """
        expect="Type mismatch in expression: BinExpr(+, IntegerLit(1), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_stmt_7(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                b = a;
                a = b + 1;
            }
            """
        expect="Type mismatch in expression: BinExpr(+, Id(b), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_stmt_8(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                b = "1"::a;
            }
            """
        expect="Type mismatch in expression: BinExpr(::, StringLit(1), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_stmt_9(self):
        input="""
            foo: function integer (a: string, b: auto)
            {
                b = a + "1";
            }
            """
        expect="Type mismatch in expression: BinExpr(+, Id(a), StringLit(1))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_stmt_10(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                c: integer = a;
                b = a + 1.0;
                printInteger(a);
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_stmt_11(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                for (b = 1, a, b + 1)
                {
                
                }
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_stmt_12(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                b = a;
                for (b = 1, a, b+1)
                {
                
                }
            }
            """
        expect="Type mismatch in statement: ForStmt(AssignStmt(Id(b), IntegerLit(1)), Id(a), BinExpr(+, Id(b), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_stmt_13(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                for (b = "a", a, 1)
                {
                
                }
            }
            """
        expect="Type mismatch in statement: ForStmt(AssignStmt(Id(b), StringLit(a)), Id(a), IntegerLit(1), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input,expect,448))
        
    def test_stmt_14(self):
        input="""
            foo: function string (a: auto, b: auto)
            {
                for (b = 1, a, b + 1)
                {
                
                }
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_stmt_15(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                for (a = 1,  1 == true, a + b)
                {
                
                }
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_stmt_16(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                while (a == true)
                {
                
                }
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_stmt_17(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                while ((a == true) && (b=="a"))
                {
                
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(==, Id(b), StringLit(a))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_stmt_18(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                while ((a == true) && (bar()))
                {
                
                }
            }
            bar: function auto ()
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_stmt_19(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                do
                {
                
                }
                while ((a == true) && (b=="a"));
            }
            """
        expect="Type mismatch in expression: BinExpr(==, Id(b), StringLit(a))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_stmt_20(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                do
                {
                
                }
                while ((a == true) && (bar()));
            }
            bar: function auto ()
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_stmt_21(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                do
                {
                    break;
                }
                while ((a == true) && (bar()));
            }
            bar: function auto ()
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_stmt_22(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                while (a==1)
                {
                    break;
                }
            }
            bar: function auto ()
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_stmt_23(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                for (a=1,b,a+1)
                {
                    
                }
                break;
            }
            bar: function auto ()
            {
            
            }
            """
        expect="Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_stmt_24(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                for (a=1,b,a+1)
                {
                    c: integer = 2;
                    for (c=2,c<2,c+1)
                    {
                        continue;
                    }   
                }
            }
            bar: function auto ()
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_stmt_25(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                for (a=1,b,a+1)
                {
                    c: integer = 2;
                    for (c=2,c<2,c+1)
                    {
                        continue;
                    }   
                    continue;
                }
            }
            bar: function auto ()
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_stmt_26(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                c: integer = bar();
                d: float = bar();
            }
            bar: function auto ()
            {
                foo(1,2);
                foo(1,1.2);
            }
            """
        expect="Type mismatch in statement: CallStmt(foo, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_stmt_27(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                c: integer = bar();
                d: float = bar();
            }
            bar: function auto ()
            {
                foo(1.1,1.2);
                foo(1,2);
                foo("a","b");
                
            }
            """
        expect="Type mismatch in statement: CallStmt(foo, StringLit(a), StringLit(b))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_stmt_28(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
            
            }
            bar: function auto ()
            {
                foo(1.1,1.2);
                foo(1,2);
                foo(bar(),bar());
                c: integer = bar();
                
            }
            """
        expect="Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FuncCall(bar, []))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_stmt_29(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
            
            }
            bar: function auto ()
            {
                foo(1.1,1);
                foo(1,2);
                foo(bar(),bar());
                c: integer = bar();
                
            }
            """
        expect="Type mismatch in statement: CallStmt(foo, FuncCall(bar, []), FuncCall(bar, []))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_stmt_30(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
            
            }
            bar: function auto ()
            {
                c: integer;
                d: float;
                foo(c,d);
                e: integer = foo(c,d);
                f: float = foo(e,f);
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,465))

    """Test array literal"""
    def test_array_lit_1(self):
        input="""
            a: array [2] of integer = {2,1.0};
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(2), FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_array_lit_2(self):
        input="""
            a: array [2,2] of float = {{1,1},{1.1,1.2}};
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([FloatLit(1.1), FloatLit(1.2)])])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_array_lit_3(self):
        input="""
            a: array [2,2] of float = {{1,1},{1,1.5}};
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([IntegerLit(1), FloatLit(1.5)])])"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_array_lit_4(self):
        input="""
            a: array [2,2] of float = {{1,1},{1,1}};
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_array_lit_5(self):
        input="""
            a: array [2,2] of float = {{1,1},{1,1},{"a","b"}};
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([StringLit(a), StringLit(b)])])"
        self.assertTrue(TestChecker.test(input,expect,470))

    """Test simple program"""
    def test_simple_program_1(self):
        input="""
            foo: function void (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                c = 1;
            }

            bar: function void (inherit c: auto)
            {
                c = 1.3;
            }
            """
        expect="Type mismatch in statement: AssignStmt(Id(c), FloatLit(1.3))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_simple_program_2(self):
        input="""
            foo: function void (a: integer, b: auto) inherit bar 
            {
                super(2);
                b = "abc";
                bar(2);
                return;
                return 1+2;
            }

            bar: function void (inherit c: auto)
            {
                foo(1,"a");
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_simple_program_3(self):
        input="""
            foo: function void (a: integer, b: auto) inherit bar 
            {
                super(2);
                b = "abc";
                return;
                if (a==1)
                    return 2;
            }

            bar: function void (inherit c: auto)
            {
                foo(1,"a");
            }
            """
        expect="Type mismatch in statement: ReturnStmt(IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_simple_program_4(self):
        input="""
            a: integer = foo(1,2);
            foo: function integer(a:auto,b:auto) inherit bar
            {
                c: float = a;
                return a+b;
                for (a=1,a<2,a+1)
                {
                    return b;
                    return false;
                }
                return "1" + "2";
            }

            bar: function void() 
            {
            
            }
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_simple_program_5(self):
        input="""
            a: integer = foo(1,2);
            foo: function integer(inherit a:auto,b:auto) inherit bar
            {
                c: float = a;
                return a+b;
                b = {1,2,3};
            }

            bar: function void() inherit foo 
            {
                preventDefault();
                return a;
            }
            """
        expect="Type mismatch in statement: AssignStmt(Id(b), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_simple_program_6(self):
        input="""
            a: integer = foo(1,2);
            foo: function integer(inherit a:auto,b:auto) inherit bar
            {
                c: float = a;
                return a+b;
                b = {1,2,3};
            }

            bar: function void() inherit foo 
            {
                preventDefault();
                return a;
            }
            """
        expect="Type mismatch in statement: AssignStmt(Id(b), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_simple_program_7(self):
        input="""
            foo: function auto (a: integer, b: auto)
            {
                if (a<1)
                {
                    return true;
                }
                else
                {
                    return false;
                }
                return 1;
                a = b + 1;
            }
            """
        expect="Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_simple_program_8(self):
        input="""
            foo: function auto (a: integer, b: auto)
            {
                if (a<1)
                {
                    return true;
                }
                else
                {
                    return false;
                }
                return bar(a,b);
            }

            bar: function void (b: integer, c:integer)
            {
            
            }
            """
        expect="Type mismatch in expression: FuncCall(bar, [Id(a), Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,478))


    def test_simple_program_9(self):
        input="""
            foo: function auto (a: integer, inherit b: auto)
            {
                return bar(a,b);
            }

            bar: function boolean (c: integer, d:integer) inherit foo
            {
                preventDefault();
                b = false;
                return true;
            }

            """
        expect="Type mismatch in statement: AssignStmt(Id(b), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_simple_program_10(self):
        input="""
            foo: function auto (a: integer, inherit b: auto)
            {
                return a + 1;
            }

            bar: function boolean (c: integer, d:integer) inherit foo
            {
                super(c,d);
                while (b<10)
                {
                    c = c - d;
                    d = d/10;
                }
                printInteger(c);
                c = readInteger();
            }

            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,480))

    """Test complex program"""

    def test_complex_program_1(self):
        input = """x: integer;
            foo1: function integer(inherit x: float){}

            foo2: function float(inherit y: float) inherit foo1{
                super(10);
                z: float = 10.1;
                return 1;
            }
            foo3: function float(out z: float) inherit foo2{
                preventDefault();
                y: integer = 10;
                printInteger(1);
                return 1.123;
            }

            main: function void(){
                x: integer = readInteger();
            }"""
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_complex_program_2(self):
        input = """x: integer;
            foo1: function integer(inherit x: float){}

            foo2: function float(inherit y: float) inherit foo1{
                super(10);
                z: float = x;
                for (x=1,x<10, x + 1)
                {
                    break;
                }
                return 1;
            }

            main: function void(){
                x: integer = readInteger();
            }"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(10)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([BreakStmt()]))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_complex_program_3(self):
        input = """x: integer = foo1(1);
            foo1: function auto(inherit x: auto){}

            foo2: function float(inherit y: float) inherit foo1{
                super(10);
                z: float = x;
                for (x=1,x<10, x + 1)
                {
                    break;
                }
                return 1;
            }

            bar: function auto (c: auto) inherit foo1
            {
                super(c);
                return {1,2,3};
            }

            main: function void(){
                x: integer = readInteger();
                b: array [2] of float = bar(1);
            }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2], FloatType), FuncCall(bar, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_complex_program_4(self):
        input = """x: integer = foo(1);
            foo: function auto(inherit x: auto)
            {
                if (x==1)
                    return 1;
                else
                    return 2;
                return 3;
            }

            bar: function auto (c: auto) inherit foo
            {
                super(c);
                return {x,c};
                for (x=1,x<10,x+1)
                {
                    return {1,2};
                }
                return {1.0,3};
            }

            main: function void(){
                x = readInteger() + bar(x);
            }"""
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(readInteger, []), FuncCall(bar, [Id(x)]))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_complex_program_5(self):
        input = """
        a: integer = {{{1,1},{1.0,1},{1.9,1.1}},{{1,1},{1.0,1},{1.3,1.1}}};
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([FloatLit(1.0), IntegerLit(1)]), ArrayLit([FloatLit(1.9), FloatLit(1.1)])]), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([FloatLit(1.0), IntegerLit(1)]), ArrayLit([FloatLit(1.3), FloatLit(1.1)])])])"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_complex_program_6(self):
        input = """
        x: integer = foo(1);
            foo: function auto(inherit x: auto)
            {
                if (x==1)
                    return 1;
                else
                    return 2;
                return 3;
            }

            bar: function auto (c: auto) inherit foo
            {
                super(c);
                a: array [2] of integer;
                for (x=1,x<10,x+1)
                {
                    return a;
                    {
                        return b;
                    }
                    if (c==1)
                    {
                        return a;
                    }
                    else
                        return d;
                }
            }

            main: function void(){
                x = readInteger() + bar(x);
            }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_complex_program_7(self):
        input = """
            foo: function void (inherit c: auto)
            {
                return;
            }

            bar: function auto (a: integer, b: auto)
            {
                super(10);
                a = readInteger();
                if (b==1)
                {
                    printInteger(a);
                }
                else
                {
                    return a;
                }
                return b;
                for (c=1,c<10,c+1)
                {
                    return a;
                }
                return 1.0;
            }

            goo: function integer(a:integer,b:float) inherit bar
            {
                super(10,10);
                return bar(a,a);
                c = 1.0;
            }
        """
        expect = "Invalid statement in function: bar"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_complex_program_8(self):
        input = """
            foo: function void (inherit c: auto)
            {
                return;
            }

            bar: function auto (a: integer, b: auto) inherit foo
            {
                super(10);
                a = readInteger();
                if (b==1)
                {
                    printInteger(a);
                }
                else
                {
                    return a;
                }
                return b;
                for (c=1,c<10,c+1)
                {
                    return a;
                }
                return 1.0;
            }

            goo: function integer(a:integer,b:float) inherit bar
            {
                super(10,10);
                return bar(a,a);
                c = 1.0;
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_complex_program_9(self):
        input = """
            foo: function void (inherit c: auto)
            {
                return;
            }

            bar: function auto (a: integer, b: auto) inherit foo
            {
                preventDefault();
                a = readInteger();
                if (b==1)
                {
                    printInteger(a);
                }
                else
                {
                    return -a;
                }
                return b;
                for (c=1,c<10,c+1)
                {
                    return a;
                }
                return 1.0;
            }

            goo: function integer(a:integer,b:float) inherit foo
            {
                super(10,10);
                return bar(a,a);
                c = 1.0;
            }

        """
        expect = "Type mismatch in expression: IntegerLit(10)"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_complex_program_10(self):
        input = """
            foo: function void (inherit c: auto)
            {
                return;
            }

            bar: function auto (a: integer, b: auto) inherit foo
            {
                preventDefault();
                a = readInteger();
                if (b==1)
                {
                    printInteger(a);
                }
                else
                {
                    return a;
                }
                return b;
                c = readString();
                for (a=1,a<10,a+1)
                {
                    return a;
                }
                return 1.0;
            }

            goo: function integer(a:integer,b:float) inherit foo
            {
                preventDefault();
                return bar(a,a);
                return true;
                while (c==1)
                {
                
                }
            }

        """
        expect = "Type mismatch in expression: BinExpr(==, Id(c), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_complex_program_11(self):
        input = """
            square: function integer(x: integer)
            {
                return x*x;
            }

            map: function void(a: array [10] of integer, n: integer)
            {
                i: integer;
                for (i=1,i<n,i+1)
                    a[i] = square(a[i]);
                    printInteger(a[i]);
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_complex_program_12(self):
        input = """
            square: function integer(x: integer)
            {
                return x*x;
            }

            map: function void(a: array [10] of integer, n: integer)
            {
                i: integer;
                for (i=1,i<n,i+1)
                    a[i] = square(a[i]);
                    printInteger(a[i]);
            }

            main: function void()
            {
                a: array [10] of integer = {1,2,3,4,5,6,7,8,9,10};
                map(a,10);
                return true;
            }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_complex_program_13(self):
        input = """
            foo: function integer(inherit a: auto)
            {
                return a;
            }

            bar: function auto(c: integer) inherit foo
            {
                super(c);
                d: string = "a"::"b";
                printString("Hello World!!!");
                return d;
                f: auto = {1,2,3,4};
                for (c=1,c<10,c+1)
                    printInteger(f[c]);
                return false;
            }

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_complex_program_14(self):
        input = """
        a: array[10] of integer;
        find_max: function integer(n: integer)
        {
            max : integer = a[0];
            i: integer = 0;
            for (i=1,i<n,i+1)
                if (max<a[i])
                    max = a[i];
            return max;
        }
        main: function void() {
            n: integer;
            printString("Input n:");
            n = readInteger();
            i: integer = 0;
            for (i = 0,i < n,i+1)
            {
                printString("Input a[i]:");
                a[i] = readInteger();
            }
            printString("The max number in arr is");
            printInteger(find_max());
        }
        """
        expect = "Type mismatch in expression: FuncCall(find_max, [])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_complex_program_15(self):
        input = """
        
        find_max: function integer(n: integer) inherit foo
        {
            super({1,2,3,4,5,6,7,8,9,10},10);
            max : integer = a[0];
            i: integer = 0;
            for (i=1,i<n,i+1)
                if (max<a[i])
                    max = a[i];
            return max;
        }

        foo: function integer(inherit a: auto, a: integer)
        {
        
        }

        main: function void() {
            n: integer;
            printString("Input n:");
            n = readInteger();
            i: integer = 0;
            for (i = 0,i < n,i+1)
            {
                printString("Input a[i]:");
                a[i] = readInteger();
            }
            printString("The max number in arr is");
            printInteger(find_max());
            }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_complex_program_16(self):
        input = """
        f, a: array[10,10] of integer;
        sum: function float(n: integer, m: integer,x: integer, y:integer)
        {
            f[0,0] = 0;
            i,j: integer = 0,0;
            for (i=0,i<n,i+1)
                f[i,0] = 0;
            for (j=0,j<m,j+1)
                f[0,j] = 0;
            for (i = 1,i < n,i+1)
                for (j = 1, j < m,j+1)
                    f[i,j] = f[i-1,j] + f[i,j-1] - f[i-1,j-1] + a[i-1,j-1];
            return f[x-1,y-1];
        }
        main: function void() {
            n,m : integer;
            printString("Input n:");
            n = readInteger();
            printString("Input m:");
            m = readInteger();
            i,j: integer = 0,0;
            for (i = 0,i < n,i+1)
                for (j = 0, j < m,j+1)
                {
                    printString("Input a[i,j]:");
                    a[i,j] = readInteger();
                }
            x,y: integer;
            printString("Input x:");
            x = readInteger();
            printString("Input y:");
            y = readInteger();
            printString("The sum from 1,1 to x,y is");
            printInteger(sum(n,m,x,y));
        }
        """
        expect = "Type mismatch in statement: CallStmt(printInteger, FuncCall(sum, [Id(n), Id(m), Id(x), Id(y)]))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_complex_program_17(self):
        input = """
        foo: function integer(inherit f: integer) {}
        fibonacci: function integer(n: integer) inherit foo
        {
            super(10);
            f: array[100] of integer;
            f[0] = 1;
            f[1] = 1;
            i : integer;
            for (i=2,i<n,i+1)
                f[i] = f[i-1] + f[i-2];
            return f[n-1];
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            print("The nth fibonacci number is", fibonacci(n));
        }
        """
        expect = "Redeclared Variable: f"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_complex_program_18(self):
        input = """
        fibonacci: function integer(n: integer)
        {
            f: array[100] of integer;
            f[0] = 1;
            f[1] = 1;
            i : integer;
            for (i=2,i<n,i+1)
                f[i] = f[i-1] + f[i-2];
            return f[n-1];
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger(n);
            print("The nth fibonacci number is");
            printBoolean(fibonacci(n));
        }
        """
        expect = "Type mismatch in expression: FuncCall(readInteger, [Id(n)])"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_complex_program_19(self):
        input = """
        
        foo: function integer(inherit a: auto,b: integer)
        {
            return bar(a,b);
        }

        bar: function auto(c: auto,d: integer) inherit foo
        {
            preventDefault();
            return c;
        }

        f: float = bar(1,2);
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_complex_program_20(self):
        input = """
        
        foo: function boolean(x: integer)
        {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(r), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,500))
