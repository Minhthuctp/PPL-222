import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_000(self):
        input = """ a: integer = 1;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_001(self):
        input = """ a: integer = 1;
                    b: auto = c + 1;
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Identifier: c"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_002(self):
        input = """ a: float = 1 + 2.0;
                    b: auto = a + 1;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_003(self):
        input = """ main1: function integer () {
                    }
                    a: integer = 1;
                    b: auto = a + 1;
                    c: auto = a + main1();
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_004(self):
        input = """ alo: function float () {
                    }
                    a: integer = 1;
                    b: auto = 1.0;
                    c: auto = b + alo();
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_005(self):
        input = """ 
                    a: array [1, 2, 3] of integer = {1,2,3};
                    b: integer = a[2];
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2, 3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_006(self):
        input = """ alo: function float (b: string, c: string) {
                        a: integer = b;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_007(self):
        input = """ alo: function float (b: string, c: string) {
                        a = b;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 407))
        
    def test_008(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_009(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test_010(self):
        input = """ alo: function float (b: string, b: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Redeclared Parameter: b"""
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test_011(self):
        input = """ alo: function float (b: string, c: string) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 > 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_012(self):
        input = """ main1: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 > 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_013(self):
        input = """ alo: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 + 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in statement: IfStmt(BinExpr(+, IntegerLit(3), IntegerLit(2)), BlockStmt([VarDecl(a, BooleanType, BooleanLit(True))]), BlockStmt([VarDecl(a, BooleanType, BooleanLit(True))]))"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_014(self):
        input = """ alo: function float (b: string, c: boolean) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c < 3, c + 1){
                           c = c + 1; 
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(0)), BinExpr(<, Id(c), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_015(self):
        input = """ main1: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c + 3, c + 1){
                           c = c + 1; 
                        }
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(c), IntegerLit(0)), BinExpr(+, Id(c), IntegerLit(3)), BinExpr(+, Id(c), IntegerLit(1)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_016(self):
        input = """ alo: function float (b: string, c: integer) {
                        b = b;
                        {
                            a : boolean = true;
                        }
                        if (3 < 2){
                            a: boolean = true;
                        }
                        else {
                            a: boolean = true;
                        }
                        for(c = 0, c < 3, c + 1){
                           c = c + 1; 
                        }
                        break;
                    }
                    a: boolean = true;
                    c: auto = !a;
                    b: auto = !c;
                    main: function void () {
                        
                    }
                    """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_017(self):
        input = """ 
                    alo: function float (c: integer){
                        
                    }
                    a: float = alo(7.4) + 5;
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in expression: FuncCall(alo, [FloatLit(7.4)])"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_018(self):
        input = """ 
                    a: integer = main1(7) + 5;
                    main1: function integer (c: integer){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_019(self):
        input = """ 
                    a: float = main1(7) + 5;
                    foo: function integer(c: float){
                        
                    }
                    main1: function float (c: integer){
                        foo(6.5);
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_020(self):
        input = """ 
                    a: float = main1(7) + 5;
                    main1: function float (c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_021(self):
        input = """ 
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        boo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Function: boo"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_022(self):
        input = """ 
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main2: function integer () inherit main1 {
                        c = c + 1;
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_023(self):
        input = """
                    main2: function integer () inherit main1 {
                        c = c + 1;
                    }
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Invalid statement in function: main2"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_024(self):
        input = """
                    main2: function integer () inherit main1 {
                        preventDefault();
                        d = d + 1;
                    }
                    a: float = main1(7) + 5;
                    main1: function float (inherit c: integer, d: integer){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """Undeclared Identifier: d"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_025(self):
        input = """
                    main2: function integer () inherit main1 {
                        super(2, 1);
                        d = c + 1;
                    }
                    a: float = main1(7,8) + 5;
                    main1: function float (inherit c: integer, inherit d: float){
                        foo(6.5);
                    }
                    foo: function integer(c: float){
                        
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_026(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    a: float = foo(1,2);
                    c: float = a + 2;
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_027(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    a: float = foo(1,2);
                    b: integer = foo(1,2) + 1;
                    c: float = a + 2;
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_028(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: integer = foo(1,2) + 1;
                    a: integer = foo(1,2);
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_029(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: float = (foo(1,2) + 1.0) * (foo(1,2) + 1);
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_030(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: integer = (foo(1,2) + 1) * (foo(1,2) + 1.0);
                    main: function void () {
                        
                    }
                    
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(*, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)), BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), FloatLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_031(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    b: integer = (foo(1,2) + 1) * (foo(1,2) + 1.0);
                    main: function void () {
                        
                    }
                    
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(*, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)), BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), FloatLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_032(self):
        input = """
                    foo: function auto (a: integer, b: integer){
                        
                    }
                    boo: function void (){
                        foo(2,3);
                    }
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_033(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22];
                    main: function void () {
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_034(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22];
                """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_035(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2.4];
                    main: function void () {
                        
                    }
                """
        expect = """Type mismatch in expression: ArrayCell(a, [FloatLit(2.4)])"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_036(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    main: function void () {
                        c: array[3] of integer = {1, 2.3};
                    }
                """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.3)])"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_037(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    main: function void(){
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_038(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2.0;
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_039(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function float () {
                        return 2.0;
                    }
                    main: function void(){
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_040(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function auto () {
                        return 2.0;
                    }
                    main: function void(){
                        a: integer = boo();
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(boo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_041(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function auto () {
                        return 2.0;
                    }
                    main: function void(){
                        a: float = boo();
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_042(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    c: integer = a[1] + a[22] + a[2];
                    foo: function integer () {
                        return 2;
                    }
                    boo: function auto (a: integer) {
                        return 2.0;
                    }
                    main: function void(){
                        a: float = boo(2.0);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(boo, [FloatLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_043(self):
        input = """
                    b: auto = main();
                    main: function void(){
                        
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, AutoType, FuncCall(main, []))"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_044(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    b: integer;
                    main: function void(){
                        c: integer = a[1];
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_045(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    b: integer;
                    main: function void(){
                        b: array[5] of integer = {1,2,3,4,5};
                        c: integer = b[1];
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_046(self):
        input = """
                    a: array[5] of integer = {1,2,3,4,5};
                    b: integer;
                    main: function void(){
                        b: array[5] of integer = {1,2,3,4,5};
                        c: integer = b[1];
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_047(self):
        input = """
                    a: function integer(c: integer){
                        
                    }
                    main: function void(){
                        b: integer = a(1,2);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(a, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_048(self):
        input = """
                    a: function integer(c: integer){
                        
                    }
                    c: integer = a(1,2);
                    main: function void(){
                        b: integer = a(1,2);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(a, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_049(self):
        input = """
                    main1: function float (inherit c: integer){
                        
                    }
                    a: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Invalid Parameter: c"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_050(self):
        input = """
                    main1: function float (c: integer){
                        
                    }
                    a: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_051(self):
        input = """
                    main1: function float (){
                        
                    }
                    a: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_052(self):
        input = """
                    main1: function float (){
                        
                    }
                    main1: function integer (c: integer) inherit main1{
                        
                    }
                    main: function void(){
                        
                    }
                """
        expect = """Redeclared Function: main1"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_053(self):
        input = """
                    a: integer = 1;
                    a: float = 1.0;
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_054(self):
        input = """
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_055(self):
        input = """
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_056(self):
        input = """
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    foo: integer = 2;
                    
                """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_057(self):
        input = """
                    foo: integer = 2;
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    
                """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 457))


    def test_058(self):
        input = """
                    foo: integer = 2;
                    iden : integer = 5;
                    main: function void (){
                        while (foo < -3){
                            if (iden % 2 == 1) {
                                iden = iden + 1;
                            }
                            else {
                                iden = iden + 2;
                            }
                            foo = foo - 1;
                        }
                    }
                    
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_059(self):
        input = """
                    foo: integer = 2;
                    foo: function void(a: integer){
                        a: float = 2.0;
                    }
                    main: function void (){
                        
                    }
                    
                """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_060(self):
        input = """
                    
                    foo: function auto(a: integer){
                        
                    }
                    main: function void (){
                        
                    }
                    a: auto = foo(2);
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_061(self):
        input = """
                    
                    foo: function float(a: integer){
                        return a;
                    }
                    main: function void (){
                        
                    }
                    a: auto = foo(2);
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_062(self):
        input = """
                    
                    foo: function integer(a: float){
                        return a;
                    }
                    main: function void (){
                        
                    }
                    a: auto = foo(2);
                """
        expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_063(self):
        input = """
                    foo: function float (a: float){
                        return a;
                    }
                    foo1: function integer(){
                        foo(2);
                    }
                    main: function void (){
                        
                    }
                    c: auto = foo(2);
                    a: auto = foo1();
                    b: float = foo1();
                """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_064(self):
        input = """
                    y: function void (a: string) {}
                    x: function void (a: auto) {
                        y(a);
                        b: string = a :: "Hello";
                    }
                    main: function void () {
                        x(5);
                    }
                """
        expect = """Type mismatch in statement: CallStmt(x, IntegerLit(5))"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_065(self):
        input = """
                    
                    x: function void (a: auto) {}
                    main: function void () {
                        x("a");
                        x(2);
                    }
                """
        expect = """Type mismatch in statement: CallStmt(x, IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_066(self):
        input = """
                    y: function auto (a: string) {}
                    x: function string (a: string) {}
                    main: function void () {
                        x(y("abc"));
                        a: integer = y("a");
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(y, [StringLit(a)]))"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_067(self):
        input = """
                    y: function string (a: auto) {}
                    x: function string (a: string) {}
                    main: function void () {
                        a: string = y("a");
                        b: string = y(2);
                    }
                """
        expect = """Type mismatch in expression: FuncCall(y, [IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_068(self):
        input = """
                    y: function auto (a: integer) {
                        
                    }
                    x: function string (a: string) {
                        
                    }
                    main: function void () {
                        a: string = x(y(5));
                        b: integer = y(5);
                    }
                """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FuncCall(y, [IntegerLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_069(self):
        input = """
                    y: function auto (a: auto) {
                        
                    }
                    x: function string (a: string) {
                        
                    }
                    z: function integer (a: integer) {
                        
                    }
                    main: function void () {
                        x(y(5));
                        a: string = y(6);
                        z(y(6));
                    }
                """
        expect = """Type mismatch in statement: CallStmt(z, FuncCall(y, [IntegerLit(6)]))"""
        self.assertTrue(TestChecker.test(input, expect, 469))
    
    def test_070(self):
        input = """a,b: integer = false, true;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BooleanLit(False))"
        self.assertTrue(TestChecker.test(input,expect,470))
        
    def test_071(self):
        input = """bar: function boolean() {
            b : boolean = true;
            c = b;
            return c;
        }"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_072(self):
        input = """a : integer = 3;
            b,c : float = a + 1,5;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_073(self):
        input = """a,b,c,d,e: string = 1+2, 3, 4, 5, 7+8;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(+, IntegerLit(1), IntegerLit(2)))"
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_074(self):
        input = """main: function boolean (n: auto, b: integer, a: float) inherit foo {}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,474))
        
    def test_075(self):
        input = """foo: function string (inherit a: string, out b: float) {}
            main: function auto (a: array[2] of integer, b: float) inherit foo {}"""
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_076(self):
        input = """foo: function void(a: integer) {
                a: float = 2.0;
            }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_077(self):
        input = """a,b : array [2] of string = {},{};
            main: function void ()
            {
                return a[{1,2,3},2,3,4];
            }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], StringType), ArrayLit([]))"
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_078(self):
        input = """ y: function void (a: string) {}
                    x: function void (a: auto) {}
                    main: function void() {
                        x("a");
                        x(2);
                    }"""
        expect = "Type mismatch in statement: CallStmt(x, IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_079(self):
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType())])
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input,expect,479))
        
    def test_080(self):
        input = """gcdRecursion: function integer(p: integer, q: integer){
            if (p > q)
                return gcdRecursion(p - q, q);
            else
                if (p < q)
                    return gcdRecursion(p, q - p);
                else
                    return p;
            }
        gcdIteration: function integer(p: integer, q: integer){
            while (p != q) {
                if (p > q)
                    p = p - q;
                else
                    q = q - p;
                }
            return p;
            }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_081(self):
        input = """getDiameter: function float(radius: integer){
            diameter: float = 2*radius;
            return diameter;
            }
        getCircumference: function float(radius: integer){
            C: float = 2*3.14*radius;
            return C;
            }
        getArea: function float(radius: integer){
            S: float = 3.14*radius*radius;
            return S;
            }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_082(self):
        input = """ bar: function float() {}
        foo: function boolean(x: integer) inherit bar 
        {
            r, s: integer;
            r = 2;
            a, b: array [5] of integer;
            a[0] = s;
        }
        myPI : float = 3;
        main: function void() {
            r, s: integer;
            r = 2;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI)))"
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_083(self):
        input = """bar: function float(x: string) {}
        foo: function boolean(x: integer) inherit bar 
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
            s = r * r * myPI;
            a[0] = s;
        }"""
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_084(self):
        input = """bar: function float(inherit x: float, z: integer) {}
        foo: function boolean(x: integer) inherit bar 
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
            s = r * r * myPI;
            a[0] = s;
        }"""
        expect = "Invalid Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,484))
        
    def test_085(self):
        input = """bar: function float(inherit y: float, z: integer) {}
        foo: function boolean(x: integer) inherit bar 
        {
            super("hello", 1)
            r, s: integer;
            r = 2;
            a, b: array [5] of integer;
            a[0] = s;
        }
        main: function void() {
            r, s: integer;
            r = 2;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
        }"""
        expect = "Type mismatch in expression: StringLit(hello)"
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_086(self):
        input = """
        check: function void(n: integer)
        {
            i: integer;
            for (i = 0, i < n, i + 1)
                if (foo(i) == true)
                    foo(i);
            return;
        }
        main: function void() {
            n : integer = 1;
            check(n);
        }
        foo: function boolean(x: integer)
        {
            if (x%2 == 0)
                return true;
            else
                return 0;
        }"""
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(0))"
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_087(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(inherit out n: integer, inherit delta: integer) {
            n = n + delta;
        }
        inc1: function integer(out n: integer, double: integer) inherit inc {
            super(m, double);
            m = m + double;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            a : array [0] of string;
        }"""
        expect = "Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_088(self):
        input = """main: function void() {
            for (i = 0, i < n, i*9 + i*i){
            }
        }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_089(self):
        input = """main: function void() {
            i: integer;
            for (i = 0, i < n, i*9 + i*i){
                break;
            }
        }"""
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_090(self):
        input = """main: function void() {
            i: integer;
            for (i = 0, i < 5.2, i*9 + i*i){
                break;
            }
            continue;
        }"""
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_091(self):
        input = """main: function void() {
            i: integer;
            a: float = 5;
            for (i = 0, i < 5.2, i*9 + i*i){
                if (i < 4) {
                    a = a + i;
                    continue;
                }
                else {
                    if (a < 50)
                        break;
                    {
                        a = a*i;
                        b: boolean = true;
                        while (b == a){
                            a = a + 1;
                            b = false;
                        }
                        continue;
                    }
                }
            }
        }"""
        expect = "Type mismatch in expression: BinExpr(==, Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,491))
        
    def test_092(self):
        input = """main: function void() {
            i: integer;
            a: float = 5;
            for (i = 0, i < 5.2, i*9 + i*i){
                if (i < 4) {
                    a = a + i;
                    continue;
                }
                else {
                    if (a < 50)
                        break;
                    {
                        a = a*i;
                        b: float = 8.564;
                        while (b + a){
                            a = a + 1;
                            b = false;
                        }
                        continue;
                    }
                }
            }
        }"""
        expect = "Type mismatch in statement: WhileStmt(BinExpr(+, Id(b), Id(a)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BooleanLit(False))]))"
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_093(self):
        input = """a: array [6] of integer = {1, 2.5, 2, 4, 10, 159}"""
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.5), IntegerLit(2), IntegerLit(4), IntegerLit(10), IntegerLit(159)])"
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_094(self):
        input = """a: array [2,3] of string = { {"a", "b"}, {"c", "d", "e"}}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([StringLit(a), StringLit(b)]), ArrayLit([StringLit(c), StringLit(d), StringLit(e)])])"
        self.assertTrue(TestChecker.test(input,expect,494))
        
    def test_095(self):
        input = """a: array [2,3] of string = { {"a", "b", 2}, {"c", "d", "e"}}"""
        expect = "Illegal array literal: ArrayLit([StringLit(a), StringLit(b), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,495))
        
    def test_096(self):
        input = """a: array [2,3] of string = { {1, 3, 2}, {6, 5, 4}}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(2)]), ArrayLit([IntegerLit(6), IntegerLit(5), IntegerLit(4)])]))"
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_097(self):
        input = """a: array [2,3] of string = { {1, 3, 2}, {"a", "b", "c"}}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(2)]), ArrayLit([StringLit(a), StringLit(b), StringLit(c)])])"
        self.assertTrue(TestChecker.test(input,expect,497))
        
    def test_098(self):
        input = """a: string = "hello";
        b: function void() inherit a {
            preventDefault();
        }
        a: function auto() {
        }
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def test_099(self):
        input = """b: function void() inherit a {
            preventDefault(2, true);
        }
        a: function auto() {
        }"""
        expect = "Type mismatch in statement: CallStmt(preventDefault, IntegerLit(2), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,499))
