import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """Test program structure"""
    def test_program_structure1(self):
        input = """midSquare: function integer (seed: integer) inherit bar {
          temp: integer = pow(seed, 2);
          s: string = to_string(temp);
          erase(s, begin() + size(s) - 2, end(s));
          return stoi(substr(s, size(s) - 4));
        }"""
        expect = """Program([
	FuncDecl(midSquare, IntegerType, [Param(seed, IntegerType)], bar, BlockStmt([VarDecl(temp, IntegerType, FuncCall(pow, [Id(seed), IntegerLit(2)])), VarDecl(s, StringType, FuncCall(to_string, [Id(temp)])), CallStmt(erase, Id(s), BinExpr(-, BinExpr(+, FuncCall(begin, []), FuncCall(size, [Id(s)])), IntegerLit(2)), FuncCall(end, [Id(s)])), ReturnStmt(FuncCall(stoi, [FuncCall(substr, [Id(s), BinExpr(-, FuncCall(size, [Id(s)]), IntegerLit(4))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_program_structure2(self):
        input = """a : integer;"""
        expect = """Program([
	VarDecl(a, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_program_structure3(self):
        input = """a,b : float;
                main: function void() {}
        """
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_program_structure4(self):
        input = """main: function void(){} 
            foo: function string(){}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
	FuncDecl(foo, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_program_structure5(self):
        input = """foo: function auto() {}
            a : integer;
        """
        expect = """Program([
	FuncDecl(foo, AutoType, [], None, BlockStmt([]))
	VarDecl(a, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_program_structure6(self):
        input = """bar: function void() {
            if (a==b) 
                print(a);
            }
        """
        expect = """Program([
	FuncDecl(bar, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(print, Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_program_structure7(self):
        input = """
            main: function void() {
            for (a = 1, b < 100, c+1) {
                d : integer = 0;
                while (e < 200) {f = g+1;}
                while (h != 20) {}
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(b), IntegerLit(100)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([VarDecl(d, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(e), IntegerLit(200)), BlockStmt([AssignStmt(Id(f), BinExpr(+, Id(g), IntegerLit(1)))])), WhileStmt(BinExpr(!=, Id(h), IntegerLit(20)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_program_structure8(self):
        input = """
            temp: function void() {}
        """
        expect = """Program([
	FuncDecl(temp, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_program_structure9(self):
        input = """
            c: integer = 2;
        """
        expect = """Program([
	VarDecl(c, IntegerType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_program_structure10(self):
        input = """
            a: string = "hello";
        """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))


    """Test variable declaration"""
    def test_variable_decleration1(self):
        input = """
            a: integer;
            b: float;
            c,d: auto;
            f: boolean;
            e,g,h: boolean;
            i,j: array[3,4,5] of integer;            
        """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, FloatType)
	VarDecl(c, AutoType)
	VarDecl(d, AutoType)
	VarDecl(f, BooleanType)
	VarDecl(e, BooleanType)
	VarDecl(g, BooleanType)
	VarDecl(h, BooleanType)
	VarDecl(i, ArrayType([3, 4, 5], IntegerType))
	VarDecl(j, ArrayType([3, 4, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_variable_decleration2(self):
        input = """
            a : integer = 3;
            b,c : float = a+1,5;
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, FloatType, BinExpr(+, Id(a), IntegerLit(1)))
	VarDecl(c, FloatType, IntegerLit(5))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_variable_decleration3(self):
        input = """
            a: auto = 3;
            b,c,d: integer = 1,2,3;
        """
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(1))
	VarDecl(c, IntegerType, IntegerLit(2))
	VarDecl(d, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_variable_decleration4(self):
        input = """
            a,b,c,d: float = 1+2,3,4,7+8;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(b, FloatType, IntegerLit(3))
	VarDecl(c, FloatType, IntegerLit(4))
	VarDecl(d, FloatType, BinExpr(+, IntegerLit(7), IntegerLit(8)))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_variable_decleration5(self):
        input = """
            a,b : array[5] of integer = {1,2,3},{2,3,4};
            c: float = 2.2;
            d: boolean = true;
        """
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(c, FloatType, FloatLit(2.2))
	VarDecl(d, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    """Test function declaration"""
    def test_function_decleration1(self):
        input = """
            foo: function auto() {
                if (a==b)
                    print(a);
            }        
        """
        expect = """Program([
	FuncDecl(foo, AutoType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(print, Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_function_decleration2(self):
        input = """
            main: function array[5] of string () {}
        """
        expect = """Program([
	FuncDecl(main, ArrayType([5], StringType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_function_decleration3(self):
        input = """
            foo: function float (n : integer, inherit out a: float) {}
        """
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(n, IntegerType), InheritOutParam(a, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_function_decleration4(self):
        input = """
            main: function boolean (n: auto, b: integer, a: float) inherit foo {}
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(n, AutoType), Param(b, IntegerType), Param(a, FloatType)], foo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_function_decleration5(self):
        input = """
            foo: function string (a: string, b: float) {}
            main: function auto (a: integer, b: float) {}
        """
        expect = """Program([
	FuncDecl(foo, StringType, [Param(a, StringType), Param(b, FloatType)], None, BlockStmt([]))
	FuncDecl(main, AutoType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    
    """Test array index"""
    def test_array_index1(self):
        input = """
            a : array [5] of string = {1,2,3};       
        """
        expect = """Program([
	VarDecl(a, ArrayType([5], StringType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_array_index2(self):
        input = """
            a : array [10] of float = {{1,2,4},{1,2,4},{1,2,4}};
        """
        expect = """Program([
	VarDecl(a, ArrayType([10], FloatType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_array_index3(self):
        input = """
            a,b : array [2] of string = {},{};
            main: function void ()
            {
                return a[{1,2,3},2,3,4];
            }
        """
        expect = """Program([
	VarDecl(a, ArrayType([2], StringType), ArrayLit([]))
	VarDecl(b, ArrayType([2], StringType), ArrayLit([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_array_index4(self):
        input = """
            main: function void() {
                return a[1];
                return {1,2,3};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(1)])), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_array_index5(self):
        input = """
            main: function void() {
                return a[id+1,a,c,true+false];
                return {1,2,3};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(a, [BinExpr(+, Id(id), IntegerLit(1)), Id(a), Id(c), BinExpr(+, BooleanLit(True), BooleanLit(False))])), ReturnStmt(ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    """Test operator"""
    def test_operator1(self):
        input = """
            a: integer = a::b;       
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(::, Id(a), Id(b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_operator2(self):
        input = """
            a: boolean = True && False && True || False :: e;
        """
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(::, BinExpr(||, BinExpr(&&, BinExpr(&&, Id(True), Id(False)), Id(True)), Id(False)), Id(e)))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_operator3(self):
        input = """
            a,b : string = 1+2+3*4+5+6,!True;
        """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), IntegerLit(4))), IntegerLit(5)), IntegerLit(6)))
	VarDecl(b, StringType, UnExpr(!, Id(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_operator4(self):
        input = """
            a: integer = a!=b + !2 + -2;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(!=, Id(a), BinExpr(+, BinExpr(+, Id(b), UnExpr(!, IntegerLit(2))), UnExpr(-, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_operator5(self):
        input = """
                b: integer = 2 || 2 + 3 / 3 + a[2] + c && d;
        """
        expect = """Program([
	VarDecl(b, IntegerType, BinExpr(&&, BinExpr(||, IntegerLit(2), BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(2), BinExpr(/, IntegerLit(3), IntegerLit(3))), ArrayCell(a, [IntegerLit(2)])), Id(c))), Id(d)))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_operator6(self):
        input = """
            c : float = id + a[1,2,3,4] + -2 + -4 + !true + !false;    
        """
        expect = """Program([
	VarDecl(c, FloatType, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, Id(id), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), UnExpr(-, IntegerLit(2))), UnExpr(-, IntegerLit(4))), UnExpr(!, BooleanLit(True))), UnExpr(!, BooleanLit(False))))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_operator7(self):
        input = """
            a: string = !id > 3 + 2 / 5; 
        """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(>, UnExpr(!, Id(id)), BinExpr(+, IntegerLit(3), BinExpr(/, IntegerLit(2), IntegerLit(5)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_operator8(self):
        input = """
            a,b : string = 1+2+3*4+5+6,!True;
        """
        expect = """Program([
	VarDecl(a, StringType, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(*, IntegerLit(3), IntegerLit(4))), IntegerLit(5)), IntegerLit(6)))
	VarDecl(b, StringType, UnExpr(!, Id(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_operator9(self):
        input = """
            a: integer = a!=b + !2 + -2;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(!=, Id(a), BinExpr(+, BinExpr(+, Id(b), UnExpr(!, IntegerLit(2))), UnExpr(-, IntegerLit(2)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_operator10(self):
        input = """
                b: integer = !-2 + 3 + 3 >= 3;
        """
        expect = """Program([
	VarDecl(b, IntegerType, BinExpr(>=, BinExpr(+, BinExpr(+, UnExpr(!, UnExpr(-, IntegerLit(2))), IntegerLit(3)), IntegerLit(3)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    """Test statement"""
    """Test assignment statement"""
    def test_assign_stmt1(self):
        input = """
            main: function void() {
                a = 2;
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_assign_stmt2(self):
        input = """
            main: function void() {
                a = b + c - d - a[1,2,3];
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(-, BinExpr(+, Id(b), Id(c)), Id(d)), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_assign_stmt3(self):
        input = """
            main: function void() {
                a = 2+4;
                b = "anc"+ "cfg" +5;
                c = 2.3;
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(2), IntegerLit(4))), AssignStmt(Id(b), BinExpr(+, BinExpr(+, StringLit(anc), StringLit(cfg)), IntegerLit(5))), AssignStmt(Id(c), FloatLit(2.3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_assign_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                if (a==1)
                    a = a + 1;
            }  
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_assign_stmt5(self):
        input = """
            foo : function integer() {}
            main: function void() {
                a = foo();
                b = foo();
                a = b ;
            }       
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [])), AssignStmt(Id(b), FuncCall(foo, [])), AssignStmt(Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_assign_stmt6(self):
        input = """
            main: function void() {
                a = b;
                c = 5;
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(c), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_assign_stmt7(self):
        input = """
            main: function void() {
                b = a || 2 + 3 + foo(2,3,4,1+2);
                c = a_2 + 3 + 111_223;
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), BinExpr(||, Id(a), BinExpr(+, BinExpr(+, IntegerLit(2), IntegerLit(3)), FuncCall(foo, [IntegerLit(2), IntegerLit(3), IntegerLit(4), BinExpr(+, IntegerLit(1), IntegerLit(2))])))), AssignStmt(Id(c), BinExpr(+, BinExpr(+, Id(a_2), IntegerLit(3)), IntegerLit(111223)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_assign_stmt8(self):
        input = """
            bar: function integer() {
                a = x*y + y*x;
            }    
        """
        expect = """Program([
	FuncDecl(bar, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(*, Id(x), Id(y)), BinExpr(*, Id(y), Id(x))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_assign_stmt9(self):
        input = """
            main: function void() {
                do
                {
                    a = a + 1;
                    b = b + 1;
                    c = c * 2;
                    d = a || b && c + !c;
                }
                while (a==c);
            }  
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(c)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1))), AssignStmt(Id(c), BinExpr(*, Id(c), IntegerLit(2))), AssignStmt(Id(d), BinExpr(&&, BinExpr(||, Id(a), Id(b)), BinExpr(+, Id(c), UnExpr(!, Id(c)))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_assign_stmt10(self):
        input = """
            foo : function integer() {
                d = inc(3) + 3;
                h = d + 2 + -2 + -3;
            }       
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([AssignStmt(Id(d), BinExpr(+, FuncCall(inc, [IntegerLit(3)]), IntegerLit(3))), AssignStmt(Id(h), BinExpr(+, BinExpr(+, BinExpr(+, Id(d), IntegerLit(2)), UnExpr(-, IntegerLit(2))), UnExpr(-, IntegerLit(3))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    """Test if statement"""
    def test_if_else_stmt1(self):
        input = """
            main: function void() {
                if (a+c==d)
                    b = b + c;
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(a), Id(c)), Id(d)), AssignStmt(Id(b), BinExpr(+, Id(b), Id(c))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_if_else_stmt2(self):
        input = """
            main: function void() {
                if (a > b )
                    o = c - 1;
                else
                    c = d - f;
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(o), BinExpr(-, Id(c), IntegerLit(1))), AssignStmt(Id(c), BinExpr(-, Id(d), Id(f))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_if_else_stmt3(self):
        input = """
            main: function void() {
                if (a==c)
                    if (an + ad == cd)
                        b = c + 1;
                else 
                    c = abc;
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(c)), IfStmt(BinExpr(==, BinExpr(+, Id(an), Id(ad)), Id(cd)), AssignStmt(Id(b), BinExpr(+, Id(c), IntegerLit(1))), AssignStmt(Id(c), Id(abc))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_if_else_stmt4(self):
        input = """
            a : float = 2.e3;
            main: function void() {
                if ((a!=1) && (a==f) || (c==d))
                    a = a + 1;
            }  
        """
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(2000.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, BinExpr(!=, Id(a), IntegerLit(1)), BinExpr(==, Id(a), Id(f))), BinExpr(==, Id(c), Id(d))), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_if_else_stmt5(self):
        input = """
            main: function void() {
                if (a==c)
                    if (c==d)
                        b=c;
                else
                    if ((f==c) && (g==h) || (c<=d))
                        d=c;
                    else
                        b=c;
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(c)), IfStmt(BinExpr(==, Id(c), Id(d)), AssignStmt(Id(b), Id(c)), IfStmt(BinExpr(||, BinExpr(&&, BinExpr(==, Id(f), Id(c)), BinExpr(==, Id(g), Id(h))), BinExpr(<=, Id(c), Id(d))), AssignStmt(Id(d), Id(c)), AssignStmt(Id(b), Id(c)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    """Test for statement"""
    def test_for_stmt1(self):
        input = """
            main: function void() {
                for (a = 1, a < 10 + 20, a + 1)
                {
                
                }
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(a), BinExpr(+, IntegerLit(10), IntegerLit(20))), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_for_stmt2(self):
        input = """
            main: function void() {
                for (b = 1, b < 10 , b + 1)
                {
                    print(a[i]);
                }
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(b), IntegerLit(1)), BinExpr(<, Id(b), IntegerLit(10)), BinExpr(+, Id(b), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_for_stmt3(self):
        input = """
            main: function void() {
                for (a=1,b<2,c+1)
                    print(a[i]);
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<, Id(b), IntegerLit(2)), BinExpr(+, Id(c), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_for_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                for (a = 1,b<=20+30,c + 1)
                    print(a[i]);
            }  
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(1)), BinExpr(<=, Id(b), BinExpr(+, IntegerLit(20), IntegerLit(30))), BinExpr(+, Id(c), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_for_stmt5(self):
        input = """
            main: function void() {
                for (c=2,c==3,c+1)
                {
                
                }
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(c), IntegerLit(2)), BinExpr(==, Id(c), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    """Test while-do statement"""
    def test_while_do_stmt1(self):
        input = """
            main: function void() {
                while ((a==b) && (c<=3))
                {
                
                }
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(==, Id(a), Id(b)), BinExpr(<=, Id(c), IntegerLit(3))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_while_do_stmt2(self):
        input = """
            main: function void() {
                while ((anc) + (cnd) == d)
                {
                
                }
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, BinExpr(+, Id(anc), Id(cnd)), Id(d)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_while_do_stmt3(self):
        input = """
            main: function void() {
                while ((anc+nccc) || (aaaa+vc!=c))
                {
                
                }
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(||, BinExpr(+, Id(anc), Id(nccc)), BinExpr(!=, BinExpr(+, Id(aaaa), Id(vc)), Id(c))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_while_do_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                while ((a<=c) || (c>=d) || (d==c))
                    print(a);
            }  
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(||, BinExpr(||, BinExpr(<=, Id(a), Id(c)), BinExpr(>=, Id(c), Id(d))), BinExpr(==, Id(d), Id(c))), CallStmt(print, Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_while_do_stmt5(self):
        input = """
            main: function void() {
                while ((a==c) || (d))
                {
                
                }
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(||, BinExpr(==, Id(a), Id(c)), Id(d)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    """Test do-while statement"""
    def test_do_while_stmt1(self):
        input = """
            main: function void() {
                do
                {
                    
                }
                while (a==c);
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(c)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_do_while_stmt2(self):
        input = """
            main: function void() {
                do
                {
                
                }
                while (a==c);
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(c)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_do_while_stmt3(self):
        input = """
            main: function void() {
                do
                {
                    a = a + 1;
                    c = c + 1;
                    return true;
                }
                while ((a==c) || (c==d));
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(||, BinExpr(==, Id(a), Id(c)), BinExpr(==, Id(c), Id(d))), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1))), ReturnStmt(BooleanLit(True))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_do_while_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                do
                {
                    c = c + 1;
                }
                while (a==c);
            }  
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(c)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_do_while_stmt5(self):
        input = """
            main: function void() {
                do
                {
                    print(a[i]);
                    a: integer = true;
                    b = c;
                }
                while ((a==d) || (b>c));
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(||, BinExpr(==, Id(a), Id(d)), BinExpr(>, Id(b), Id(c))), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)])), VarDecl(a, IntegerType, BooleanLit(True)), AssignStmt(Id(b), Id(c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    """Test other statement"""
    def test_other_stmt1(self):
        input = """
            main: function void() {
                return;
            }      
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_other_stmt2(self):
        input = """
            main: function void() {
                return abc[1,2,3,4,5];
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(abc, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_other_stmt3(self):
        input = """
            main: function void() {
                break;
            }    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_other_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                break;
            }  
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	FuncDecl(main, VoidType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_other_stmt5(self):
        input = """
            main: function void() {
                continue;
                return true;
            }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt(), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    """Test simple program"""
    def test_simple_program1(self):
        input = """
            foo: function auto() {
                a : integer;
                b = b + 1;
                for (b = 1, b < 3, c + 1)
                    print(a[i]);
            }           
        """
        expect = """Program([
	FuncDecl(foo, AutoType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(b), BinExpr(+, Id(b), IntegerLit(1))), ForStmt(AssignStmt(Id(b), IntegerLit(1)), BinExpr(<, Id(b), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), CallStmt(print, ArrayCell(a, [Id(i)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_simple_program2(self):
        input = """
            main: function array[5] of string () {
                if ((a!=b) && (b==c)) 
                    a=b; 
            }
            foo: function float () {
                return ; 
            }
        """
        expect = """Program([
	FuncDecl(main, ArrayType([5], StringType), [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(a), Id(b)), BinExpr(==, Id(b), Id(c))), AssignStmt(Id(a), Id(b)))]))
	FuncDecl(foo, FloatType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_simple_program3(self):
        input = """
            foo: function float (n : integer, inherit out a: float) {
                return true;
            }
            main: function void (out m : float, out a: float) inherit foo {
                continue;
                return true;
            }
        """
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(n, IntegerType), InheritOutParam(a, FloatType)], None, BlockStmt([ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [OutParam(m, FloatType), OutParam(a, FloatType)], foo, BlockStmt([ContinueStmt(), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_simple_program4(self):
        input = """
            main: function boolean (n: auto, b: integer, a: float) inherit foo {
                for (i=1,i<=10,i+1)
                    print(i);
            }
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(n, AutoType), Param(b, IntegerType), Param(a, FloatType)], foo, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_simple_program5(self):
        input = """
            foo: function string (a: string, b: float) {
                do {
                    print("hello");
                }
                while (a==b);
            }
        """
        expect = """Program([
	FuncDecl(foo, StringType, [Param(a, StringType), Param(b, FloatType)], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([CallStmt(print, StringLit(hello))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_simple_program6(self):
        input = """
            foo: function auto() {
                for (i = 1.e1, i<=3, i+1)
                    break;
            }           
        """
        expect = """Program([
	FuncDecl(foo, AutoType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(10.0)), BinExpr(<=, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_simple_program7(self):
        input = """
            main: function array[5] of string () {
                if (a!=b) 
                    a=b; 
                else
                    if (a==b)
                    {
                        print(a);
                        a = a + 1;
                        b = b % 10;
                    }
            }
        """
        expect = """Program([
	FuncDecl(main, ArrayType([5], StringType), [], None, BlockStmt([IfStmt(BinExpr(!=, Id(a), Id(b)), AssignStmt(Id(a), Id(b)), IfStmt(BinExpr(==, Id(a), Id(b)), BlockStmt([CallStmt(print, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BinExpr(%, Id(b), IntegerLit(10)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_simple_program8(self):
        input = """
            foo: function float (n : integer, inherit out a: float) {
                return ;
            }
            a : integer = 3;
            b : float = 2.5;
            c : string = "anc_ac";
        """
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(n, IntegerType), InheritOutParam(a, FloatType)], None, BlockStmt([ReturnStmt()]))
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, FloatType, FloatLit(2.5))
	VarDecl(c, StringType, StringLit(anc_ac))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_simple_program9(self):
        input = """
            main: function boolean (n: auto, b: integer, a: float) inherit foo {
                while (a==b)
                    print("Hello");
                a=c;
            }
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(n, AutoType), Param(b, IntegerType), Param(a, FloatType)], foo, BlockStmt([WhileStmt(BinExpr(==, Id(a), Id(b)), CallStmt(print, StringLit(Hello))), AssignStmt(Id(a), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_simple_program10(self):
        input = """
            foo: function string (a: string, b: float) {
                foo(2,x+3,foo(3),a[3]);
            }
        """
        expect = """Program([
	FuncDecl(foo, StringType, [Param(a, StringType), Param(b, FloatType)], None, BlockStmt([CallStmt(foo, IntegerLit(2), BinExpr(+, Id(x), IntegerLit(3)), FuncCall(foo, [IntegerLit(3)]), ArrayCell(a, [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_simple_program11(self):
        input = """
            foo: function string (a: string, b: float) {
                c : integer = 2;
                d = c + 1;
                f : array [5] of string;
                f[1] = d + 2.5;
                return f[1];
            }
        """
        expect = """Program([
	FuncDecl(foo, StringType, [Param(a, StringType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, IntegerType, IntegerLit(2)), AssignStmt(Id(d), BinExpr(+, Id(c), IntegerLit(1))), VarDecl(f, ArrayType([5], StringType)), AssignStmt(ArrayCell(f, [IntegerLit(1)]), BinExpr(+, Id(d), FloatLit(2.5))), ReturnStmt(ArrayCell(f, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_simple_program12(self):
        input = """
            bar: function void (inherit out a: float, inherit out b: string) inherit foo {
                for (i = 1, i < 10, i + 1)
                {
                    print(a[i,j,e,f]);
                }
                if (a[1]==2)
                    return ;
                else
                    break;
                foo(1+2,x+1,true);
            }
        """
        expect = """Program([
	FuncDecl(bar, VoidType, [InheritOutParam(a, FloatType), InheritOutParam(b, StringType)], foo, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i), Id(j), Id(e), Id(f)]))])), IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1)]), IntegerLit(2)), ReturnStmt(), BreakStmt()), CallStmt(foo, BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(+, Id(x), IntegerLit(1)), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_simple_program13(self):
        input = """
            inc: function auto(a: integer, b: float)
            {
                a = -1 + -2 + -3;
                b = a + a / b + a;
                while (a!=0)
                    a = a - 1;
                return a;
                do
                {
                    a = b + 1;
                    d: integer = true;
                    print("anc dbafd",d);
                }
                while (a==true);
            }
        """
        expect = """Program([
	FuncDecl(inc, AutoType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(+, UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(2))), UnExpr(-, IntegerLit(3)))), AssignStmt(Id(b), BinExpr(+, BinExpr(+, Id(a), BinExpr(/, Id(a), Id(b))), Id(a))), WhileStmt(BinExpr(!=, Id(a), IntegerLit(0)), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1)))), ReturnStmt(Id(a)), DoWhileStmt(BinExpr(==, Id(a), BooleanLit(True)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(b), IntegerLit(1))), VarDecl(d, IntegerType, BooleanLit(True)), CallStmt(print, StringLit(anc dbafd), Id(d))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_simple_program14(self):
        input = """
            foo: function void()
            {
                a: integer = 1+2+3;
                b: float = 2.e3;
                c = !c + 1;
                break;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3))), VarDecl(b, FloatType, FloatLit(2000.0)), AssignStmt(Id(c), BinExpr(+, UnExpr(!, Id(c)), IntegerLit(1))), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_simple_program15(self):
        input = """
            foo: function float(a : integer, b: float)
            {
                if ((a==b) && (c==d))
                    return true;
                else
                    return false;
            }
        """
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, Id(a), Id(b)), BinExpr(==, Id(c), Id(d))), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    """Test complex program"""
    def test_complex_program1(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            a : array [0] of string;
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), VarDecl(a, ArrayType([0], StringType)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_complex_program2(self):
        input = """
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else 
                return false;
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            if (count(n) == true)
                print("n is prime number");
            else
                print("n is not prime number");
        }"""
        expect = """Program([
	FuncDecl(count, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(c, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1))))), IfStmt(BinExpr(==, Id(c), IntegerLit(2)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), IfStmt(BinExpr(==, FuncCall(count, [Id(n)]), BooleanLit(True)), CallStmt(print, StringLit(n is prime number)), CallStmt(print, StringLit(n is not prime number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_complex_program3(self):
        input = """
        check_palindrom: function boolean(s: string)
        {
            i: integer;
            s1: string = "";
            for (i=0,i<length(s),i+1)
                s1 = s1 + s[i]; 
            if (s1==s)
                return true;
            else 
                return false;
        }
        main: function void() {
            s: string;
            print("Input s:");
            readString(s);
            if (chec_palindrom(s) == true)
                print("s is palindrom string");
            else
                print("s not is palindrom string");
        }"""
        expect = """Program([
	FuncDecl(check_palindrom, BooleanType, [Param(s, StringType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(s1, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s)])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(s1), BinExpr(+, Id(s1), ArrayCell(s, [Id(i)])))), IfStmt(BinExpr(==, Id(s1), Id(s)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType), CallStmt(print, StringLit(Input s:)), CallStmt(readString, Id(s)), IfStmt(BinExpr(==, FuncCall(chec_palindrom, [Id(s)]), BooleanLit(True)), CallStmt(print, StringLit(s is palindrom string)), CallStmt(print, StringLit(s not is palindrom string)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_complex_program4(self):
        input = """
        inc_x: function void(out x: integer, d: integer) 
        {
            x = x + d;
        }
        foo: function integer(n: integer)
        {
            i: integer;
            sum: integer = 0;
            for (i=0,i<n,inc_x(i,1))
                inc_x(sum,i);
            return sum;
        }
        main: function void() {
            n: integer;
            print("Input n:");
            readInteger(n);
            print("The sum is ",foo(n));
        }"""
        expect = """Program([
	FuncDecl(inc_x, VoidType, [OutParam(x, IntegerType), Param(d, IntegerType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), Id(d)))]))
	FuncDecl(foo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), FuncCall(inc_x, [Id(i), IntegerLit(1)]), CallStmt(inc_x, Id(sum), Id(i))), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInteger, Id(n)), CallStmt(print, StringLit(The sum is ), FuncCall(foo, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_complex_program5(self):
        input = """
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == n)
                return true;
            else 
                return false;
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            if (count(n) == true)
                print("n is perfect number");
            else
                print("n is not perfect number");
        }"""
        expect = """Program([
	FuncDecl(count, BooleanType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(c, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1))))), IfStmt(BinExpr(==, Id(c), Id(n)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), IfStmt(BinExpr(==, FuncCall(count, [Id(n)]), BooleanLit(True)), CallStmt(print, StringLit(n is perfect number)), CallStmt(print, StringLit(n is not perfect number)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_complex_program6(self):
        input = """
        sum: function integer(n: integer)
        {
            total,dem : integer = 0,0;
            do
            {
                total = total + (n%10);
                dem = dem + 1;
                n = n % 10;
            }
            while (n!=0);
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            print("The sum is", sum(n));
        }"""
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(total, IntegerType, IntegerLit(0)), VarDecl(dem, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(total), BinExpr(+, Id(total), BinExpr(%, Id(n), IntegerLit(10)))), AssignStmt(Id(dem), BinExpr(+, Id(dem), IntegerLit(1))), AssignStmt(Id(n), BinExpr(%, Id(n), IntegerLit(10)))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), CallStmt(print, StringLit(The sum is), FuncCall(sum, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
    
    def test_complex_program7(self):
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
            print("Input n:");
            readInt(n);
            print("The nth fibonacci number is", fibonacci(n));
        }"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(f, ArrayType([100], IntegerType)), AssignStmt(ArrayCell(f, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(f, [IntegerLit(1)]), IntegerLit(1)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(f, [Id(i)]), BinExpr(+, ArrayCell(f, [BinExpr(-, Id(i), IntegerLit(1))]), ArrayCell(f, [BinExpr(-, Id(i), IntegerLit(2))])))), ReturnStmt(ArrayCell(f, [BinExpr(-, Id(n), IntegerLit(1))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), CallStmt(print, StringLit(The nth fibonacci number is), FuncCall(fibonacci, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test_complex_program8(self):
        input = """
        f, a: array[10,10] of integer;
        sum: function integer(n: integer, m: integer,x: integer, y:integer)
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
            print("Input n:");
            readInt(n);
            print("Input m:");
            readInt(m);
            i,j: integer = 0,0;
            for (i = 0,i < n,i+1)
                for (j = 0, j < m,j+1)
                {
                    print("Input a[i,j]:");
                    readInt(a[i,j]);
                }
            x,y: integer;
            print("Input x:");
            readInt(x);
            print("Input y:");
            readInt(y);
            print("The sum from 1,1 to x,y is", sum(n,m,x,y));
        }"""
        expect = """Program([
	VarDecl(f, ArrayType([10, 10], IntegerType))
	VarDecl(a, ArrayType([10, 10], IntegerType))
	FuncDecl(sum, IntegerType, [Param(n, IntegerType), Param(m, IntegerType), Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(f, [IntegerLit(0), IntegerLit(0)]), IntegerLit(0)), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(f, [Id(i), IntegerLit(0)]), IntegerLit(0))), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(m)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(ArrayCell(f, [IntegerLit(0), Id(j)]), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), Id(m)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(ArrayCell(f, [Id(i), Id(j)]), BinExpr(+, BinExpr(-, BinExpr(+, ArrayCell(f, [BinExpr(-, Id(i), IntegerLit(1)), Id(j)]), ArrayCell(f, [Id(i), BinExpr(-, Id(j), IntegerLit(1))])), ArrayCell(f, [BinExpr(-, Id(i), IntegerLit(1)), BinExpr(-, Id(j), IntegerLit(1))])), ArrayCell(a, [BinExpr(-, Id(i), IntegerLit(1)), BinExpr(-, Id(j), IntegerLit(1))]))))), ReturnStmt(ArrayCell(f, [BinExpr(-, Id(x), IntegerLit(1)), BinExpr(-, Id(y), IntegerLit(1))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(m, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), CallStmt(print, StringLit(Input m:)), CallStmt(readInt, Id(m)), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(m)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(Input a[i,j]:)), CallStmt(readInt, ArrayCell(a, [Id(i), Id(j)]))]))), VarDecl(x, IntegerType), VarDecl(y, IntegerType), CallStmt(print, StringLit(Input x:)), CallStmt(readInt, Id(x)), CallStmt(print, StringLit(Input y:)), CallStmt(readInt, Id(y)), CallStmt(print, StringLit(The sum from 1,1 to x,y is), FuncCall(sum, [Id(n), Id(m), Id(x), Id(y)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_complex_program9(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + randomChar();
            return s;
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            print("The random string length n is ", random(n));
        }"""
        expect = """Program([
	VarDecl(s, StringType)
	FuncDecl(random, StringType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), AssignStmt(Id(s), StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(s), BinExpr(+, Id(s), FuncCall(randomChar, [])))), ReturnStmt(Id(s))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), CallStmt(print, StringLit(The random string length n is ), FuncCall(random, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_complex_program10(self):
        input = """
        foo: function boolean(x: integer) inherit bar 
        {
            if (x%2==0)
                return true;
            else
                return false;
        }
        check: function void(n: integer)
        {
            i: integer;
            for (i = 0,i < n,i+1)
                if (foo(i) == true)
                    print(i);
            return;
        }
        main: function void() {
            n : integer;
            print("Input n:");
            readInt(n);
            print("The even number from 0 to n is ");
            check(n);
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(x, IntegerType)], bar, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
	FuncDecl(check, VoidType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, FuncCall(foo, [Id(i)]), BooleanLit(True)), CallStmt(print, Id(i)))), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), CallStmt(print, StringLit(The even number from 0 to n is )), CallStmt(check, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_complex_program11(self):
        input = """
        a,b: array[10] of integer;
        swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
        {
            if (n>10)
                return;
            else
            {
                temp,i : integer;
                for (i=0,i<n,i+1)
                {
                    temp=a[i];
                    a[i]=b[i];
                    b[i]=temp;
                }
            }
        }
        main: function void() {
            n : integer;
            print("Input n:");
            i : integer;
            for (i=0,i<n,i+1)
            {
                print("Input a[i]");
                readInteger(a[i]);
            }
            for (i=0,i<n,i+1)
            {
                print("Input b[i]");
                readInteger(b[i]);
            }
            swap(a,b,n);
            print("Array a and b after swapping:");
            for (i=0,i<n,i+1)
            {
                print(a[i]);
            }
            for (i=0,i<n,i+1)
            {
                print(b[i]);
            }
        }"""
        expect = """Program([
	VarDecl(a, ArrayType([10], IntegerType))
	VarDecl(b, ArrayType([10], IntegerType))
	FuncDecl(swap, VoidType, [OutParam(a, ArrayType([10], IntegerType)), OutParam(b, ArrayType([10], IntegerType)), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(n), IntegerLit(10)), ReturnStmt(), BlockStmt([VarDecl(temp, IntegerType), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(temp), ArrayCell(a, [Id(i)])), AssignStmt(ArrayCell(a, [Id(i)]), ArrayCell(b, [Id(i)])), AssignStmt(ArrayCell(b, [Id(i)]), Id(temp))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(Input a[i])), CallStmt(readInteger, ArrayCell(a, [Id(i)]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(Input b[i])), CallStmt(readInteger, ArrayCell(b, [Id(i)]))])), CallStmt(swap, Id(a), Id(b), Id(n)), CallStmt(print, StringLit(Array a and b after swapping:)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(b, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    
    def test_complex_program12(self):
        input = """
        freq: function integer(s: string,c:string)
        {
            count : integer =0;
            i : auto;
            for (i = 0,i<length(s),i+1)
                if (s[i]==c)
                    count = count + 1;
            return count;
        }
        main: function void() {
            s,c : string;
            print("Input s:");
            readString(n);
            print("Input c:");
            readString(c);
            print("The frequency of c in s is", freq(s,c));
        }"""
        expect = """Program([
	FuncDecl(freq, IntegerType, [Param(s, StringType), Param(c, StringType)], None, BlockStmt([VarDecl(count, IntegerType, IntegerLit(0)), VarDecl(i, AutoType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s)])), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), Id(c)), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))))), ReturnStmt(Id(count))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(s, StringType), VarDecl(c, StringType), CallStmt(print, StringLit(Input s:)), CallStmt(readString, Id(n)), CallStmt(print, StringLit(Input c:)), CallStmt(readString, Id(c)), CallStmt(print, StringLit(The frequency of c in s is), FuncCall(freq, [Id(s), Id(c)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test_complex_program13(self):
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
            print("Input n:");
            readInt(n);
            i: integer = 0;
            for (i = 0,i < n,i+1)
            {
                print("Input a[i]:");
                readInt(a[i]);
            }
            print("The max number in arr is", max(n));
        }"""
        expect = """Program([
	VarDecl(a, ArrayType([10], IntegerType))
	FuncDecl(find_max, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(max, IntegerType, ArrayCell(a, [IntegerLit(0)])), VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(<, Id(max), ArrayCell(a, [Id(i)])), AssignStmt(Id(max), ArrayCell(a, [Id(i)])))), ReturnStmt(Id(max))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Input n:)), CallStmt(readInt, Id(n)), VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(Input a[i]:)), CallStmt(readInt, ArrayCell(a, [Id(i)]))])), CallStmt(print, StringLit(The max number in arr is), FuncCall(max, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_complex_program14(self):
        input = """
        foo: function void()
        {
            i: integer;
            a: float = 1;
            {
                c : integer = true;
                d,f,g: float = 1.2,3,4;
                for (i=0,i<c,i+1)
                    print(g);
            }
        }
        main: function auto() {
            n : integer;
            a_b_c: auto;
            {
                foo();
                foo();
                hello_foo();
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(a, FloatType, IntegerLit(1)), BlockStmt([VarDecl(c, IntegerType, BooleanLit(True)), VarDecl(d, FloatType, FloatLit(1.2)), VarDecl(f, FloatType, IntegerLit(3)), VarDecl(g, FloatType, IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(c)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(print, Id(g)))])]))
	FuncDecl(main, AutoType, [], None, BlockStmt([VarDecl(n, IntegerType), VarDecl(a_b_c, AutoType), BlockStmt([CallStmt(foo, ), CallStmt(foo, ), CallStmt(hello_foo, )])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_complex_program15(self):
        input = """
        foo: function boolean(x: integer) inherit bar 
        {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
        }
        main: function void() {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(x, IntegerType)], bar, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))