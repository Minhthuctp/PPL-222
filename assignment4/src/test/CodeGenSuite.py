import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """
        x : integer = 1;
        main: function void()
        {
            printInteger(x);
        }
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test2(self):
        input = """
        x: integer = 12_1234;
        main: function void() {
            printInteger(x);
        }
        """
        expect = "121234\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test3(self):
        input = """
        x,y: integer = 1,2;
        main: function void() {
            printInteger(x);
            printInteger(y);
        }
        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test3(self):
        input = """
        x,y: integer = 1,2;
        main: function void() {
            printInteger(x);
            printInteger(y);
        }
        """
        expect = "1\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test4(self):
        input = """
        x: integer = 10;
        main: function void() {
            printInteger(x);
        }
        """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test5(self):
        input = """
        x: integer = 12_11_11;
        main: function void() {
            printInteger(x);
        }
        """
        expect = "121111\n"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test6(self):
        input = """
        x, y: float = 1, 10.5;
        main: function void() {
            writeFloat(x);
            writeFloat(y);
        }
        """
        expect = "1.0\n10.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test7(self):
        input = """
        x: boolean = false;
        main: function void() {
            printBoolean(x);
        }
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test8(self):
        input = """
        x: string = "PPL";
        main: function void() {
            printString(x);
        }
        """
        expect = "PPL"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test9(self):
        input = """
        main: function void() {
            printInteger(15+20);
        }
        """
        expect = "35\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test10(self):
        input = """
        main: function void() {
            writeFloat(11.1 + 11);
        }
        """
        expect = "22.1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test11(self):
        input = """
        main: function void() {
            writeFloat(11 + 11.1);
        }
        """
        expect = "22.1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test12(self):
        input = """
        main: function void() {
            writeFloat(10_0 + 20_0);
        }
        """
        expect = "300.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test13(self):
        input = """
        main: function void() {
            printInteger(25 * 25);
        }
        """
        expect = "625\n"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test14(self):
        input = """
        main: function void() {
            printInteger(10 - 5);
            writeFloat(10 - 5);
            printInteger(50 - 30);
            writeFloat(50.0 - 30.0);
        }
        """
        expect = "5\n5.0\n20\n20.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test15(self):
        input = """
        main: function void() {
            printInteger(10 * 20);
            writeFloat(10 * 20);
            printInteger(100 * 200);
            writeFloat(10.0 * 20.25);
        }
        """
        expect = "200\n200.0\n20000\n202.5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test16(self):
        input = """
        main: function void() {
            writeFloat(50 / 10);
            writeFloat(50 / 10.0);
            writeFloat(40.0 / 20);
            writeFloat(40.0 / 20.0);
        }
        """
        expect = "5.0\n5.0\n2.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test17(self):
        input = """
        main: function void() {
            printInteger(11 % 5);
        }
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test18(self):
        input = """
        main: function void() {
          printString("PPL"::"sogreat");
        }
        """
        expect = "PPLsogreat"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test19(self):
        input = """
        main: function void() {
            printString(("new"::"day")::"goodmorning");
            printString(("new"::"day")::("good"::"morning"));
        }
        """
        expect = "newdaygoodmorningnewdaygoodmorning"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test20(self):
        input = """
        main: function void() {
            printBoolean(true);
        }
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test21(self):
        input = """
        main: function void() {
            printBoolean(false && false);
        }
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test22(self):
        input = """
        main: function void() {
            printBoolean((5.0 > 3) || (1.0 < 2));
        }
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test23(self):
        input = """
        main: function void() {
            printBoolean(!(false && false));
            printBoolean(!true);
        }
        """
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test24(self):
        input = """
        main: function void() {
            printInteger(-100);
            printInteger(-100 + 200);
        }
        """
        expect = "-100\n100\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test25(self):
        input = """
        main: function void() {
            printBoolean(1_1.5 * 2_0 - 10_0 * 2.1 > 10.5*3 + 3 * 5 + 10/2 + 10);
            printBoolean(1_1.5 * 2_0 - 10_0 * 2.1 < 10.5*3 + 3 * 5 + 10/2 + 10);
            printBoolean(1_1.5 * 2_0 - 10_0 * 2.1 == 10.5*3 + 3 * 5 + 10/2 + 10);
            printBoolean(1_1.5 * 2_0 - 10_0 * 2.1 >= 10.5*3 + 3 * 5 + 10/2 + 10);
            printBoolean(1_1.5 * 2_0 - 10_0 * 2.1 <= 10.5*3 + 3 * 5 + 10/2 + 10);
            printBoolean(1_1.5 * 2_0 - 10_0 * 2.1 != 10.5*3 + 3 * 5 + 10/2 + 10);
        }
        """
        expect = "false\ntrue\nfalse\nfalse\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test26(self):
        input = """
        a: array[5] of integer = {1, 2, 3, 4, 5};
        main: function void() {
            b: array[10] of integer = {1, 2, 3, 4, 5};
            printInteger(a[2] + b[1]);
        }
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test27(self):
        input = """
        arr1 : array [2, 2] of integer = {{1, 3},{2, 4}};
        arr2 : array [2, 3] of integer = {{1, 2, 3}, {123, 1238, 6}};
        main: function void() {
            arr3 : array [2, 3, 2] of integer = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
            printInteger(arr1[ 1 + 0, 1]);
            printInteger(arr2[ 1 + 0, 1]);
            printInteger(arr2[ 0 - (-1), 1]);
            printInteger(arr2[10%3, 1]);
            printInteger(arr3[0, 1, 1]);
        }
        """
        expect = "4\n1238\n1238\n1238\n13\n"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test28(self):
        input = """
        x: integer = 2;
        main: function void() {
            x = 0;
            printInteger(x);
        }
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test29(self):
        input = """
        x: string = "hi";
        main: function void() {
            x = "world";
            printString(x);
        }
        """
        expect = "world"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test30(self):
        input = """
        temp: boolean;
        main: function void() {
            temp = false;
            printBoolean(temp);
            temp = true;
            printBoolean(temp);
        }
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test31(self):
        input = """
        x: array[5] of integer = {1, 2, 3, 4, 5};
        main: function void() {
            x[0] = 10;
            x[2] = 20;
            printInteger(x[1] + x[2]);
        }
        """
        expect = "22\n"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test32(self):
        input = """
        x: array[2, 2] of integer = {{1, 2}, {3, 4}};
        y: array[2, 2] of float = {{5, 6}, {7, 8}};
        main: function void() {
            printInteger(x[1, 1] + x[0, 0]);
            writeFloat(y[0, 2] + x[1,1]);
        }
        """
        expect = "5\n11.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    """Test statement"""
    def test33(self):
        input = """
        main: function void() {
            if (10 + 20 < 40) {
                printBoolean(false);
            } else {
                printBoolean(true);
            }
        }
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test34(self):
        input = """
        main: function void() {
            if (true != false) {
                printBoolean(true);
            } else {
                printBoolean(false);
            }
            printBoolean(false);
        }
        """
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test35(self):
        input = """
        main: function void() {
            if (!(true && false)) {
                printBoolean(false);
            } else {
                printBoolean(true);
            }
            printBoolean(true);
        }
        """
        expect = "false\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test36(self):
        input = """
        main: function void() {
            i: integer = 2;
            x: array[5, 5] of integer;
            if (i == 3) {
                x[i, 0] = i;
            } else {
                x[0, i] = i + 1;
            }
            printInteger(x[0, i]);
        }
        """
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test37(self):
        input = """
        i: integer = 3;
        main: function void() {
            x: array[5, 5] of integer;
            x[1,0] = 1;
            if (i % 2 == 0) {
                x[i, 0] = i;
            } else {
                x[0, i] = i + 1;
            }
            printInteger(x[i, 0]);
        }
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test38(self):
        input = """
        main: function void() {
            i: integer = 1;
            x: array[2, 2] of integer = {{1,2},{3,4}};
            printInteger(x[1, 0]);
            if ( (i + 1) % 2 != 0) {
                x[i, 0] = i;
            }  else {
                x[0, i] = i + 1;
            }
            printInteger(x[0, i]);
        }
        """
        expect = "3\n2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test39(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 1, i < 10, i+1) {
                printInteger(i);
            }
        }
        """
        expect = "1\n2\n3\n4\n5\n6\n7\n8\n9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test40(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 1, i < 5, i+1) {
                j: integer;
                for (j = 1, j < 5, j+1) {
                    if (i + j >= 2) {
                        printInteger(i+j);
                    } else {
                        printInteger(i-j);
                    }
                }
            }
        }
        """
        expect = "2\n3\n4\n5\n3\n4\n5\n6\n4\n5\n6\n7\n5\n6\n7\n8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test41(self):
        input = """
        i,j : integer;
        main: function void() {
            for (i = 1, i < 5, i+1) {
                for (j = 1, j < 5, j+1) {
                    if (i + j >= 2) {
                        printInteger(i+j);
                    } else {
                        printInteger(i-j);
                    }
                }
            }
        }
        """
        expect = "2\n3\n4\n5\n3\n4\n5\n6\n4\n5\n6\n7\n5\n6\n7\n8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test42(self):
        input = """
        main: function void() {
            i,j : integer;
            for (i = 1, i < 5.0, i+1) {
                for (j = 1, j < 5.0, j+1) {
                    if (i + j >= 2.0) {
                        printInteger(i+j);
                    } else {
                        printInteger(i-j);
                    }
                }
            }
        }
        """
        expect = "2\n3\n4\n5\n3\n4\n5\n6\n4\n5\n6\n7\n5\n6\n7\n8\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test43(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 10, i < 15.0, i+1) {
                printInteger(i);
                break;
            }
        }
        """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test44(self):
        input = """
        i, j: integer;
        main: function void() {
            for (i = 1, i < 3, i+1) {
                for (j = 1, j < 3, j+1) {
                    if (i + j >= 2) {
                        printInteger(i+j);
                        break;
                    } else {
                        printInteger(i-j);
                    }
                }
            }
        }
        """
        expect = "2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test45(self):
        input = """
        main: function void() {
            i, j: integer = 1, 2;
            for (i = 1, i < 5, i+1) {
                printInteger(i+j);
            }
        }
        """
        expect = "3\n4\n5\n6\n"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test46(self):
        input = """
        main: function void() {
            i, j: integer = 1, 2;
            for (j = 1, j < 5, j+1) {
                printInteger(i+j);
            }
        }
        """
        expect = "2\n3\n4\n5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test47(self):
        input = """
        main: function void() {
            i: integer = 1;
            while (i < 10) {
                i = i + 1;
            }
            printInteger(i);
        }
        """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test48(self):
        input = """
        main: function void() {
            i: integer = 0;
            while (i < 20) {
                if (i == 10) {
                    printInteger(i);
                    i = 100;
                    break;
                }
                i = i + 1;
            }
            printInteger(i);
        }
        """
        expect = "10\n100\n"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test49(self):
        input = """
        main: function void() {
            i, n: integer = 0, 5;
            do {
                for (i = 0, i < n, i+1)
                    if (n == 20)
                        break;
                    else
                        n = n + 1;
                break;
            } while(true);
            printInteger(i);
        }
        """
        expect = "15\n"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test50(self):
        input = """
        main: function void() {
            i, n: integer = 0, 5;
            do {
                for (i = 0, i < n, i+1)
                    if (n == 20)
                    {
                        printInteger(n);
                        break;
                    }
                    else
                        n = n + 1;
                break;
            } while(true);
            printInteger(i);
        }
        """
        expect = "20\n15\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test51(self):
        input = """
        main: function void() {
            i: integer = 0;
            do{
                j : integer = 0;
                while (j < 2) {
                    if (i + j >= 0) 
                        break;
                    j = j + 1;
                }
                printInteger(i);
                i = i + 1;
            }while(i < 10);
        }
            """
        expect = "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test52(self):
        input = """
        checkValid: function boolean (n: integer) {
            if (n % 2 == 0)
                return true;
            else
                return false;
        }
        main: function void() {
            res: boolean = checkValid(3);
            printBoolean(res);
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test53(self):
        input = """
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(n: integer, delta: integer) {
            n = n + delta;
            printInteger(n);
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
        }
            """
        expect = "71\n"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test54(self):
        input = """
        i: integer;
        main: function void() {
            for (i = 5, i < 10, i+1) {
                printInteger(i);
                return;
            }
        }
            """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test55(self):
        input = """
        foo: function integer(n: integer, d: integer) {
            n = n + d;
            i : integer = 1;
            while (i < 10)
                return i;
            return 10;
        }
        main: function void() {
            printInteger(foo(10, 1));
        }
            """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test56(self):
        input = """
        foo: function integer(n: integer, d: integer) {
            n = n + d;
            i: integer;
            for (i = 1, i < 10, i+1) {
                while(n < 10) {
                    return i;
                }
            }
            return 10;
        }
        main: function void() {
            printInteger(foo(1, 1));
        }
            """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test57(self):
        input = """
        foo: function integer(n: integer, d: integer) {
            i,j : integer;
            n = n + d;
            for (i = 1, i < n, i+1) {
                for (j = 1, j < n, j+1) {
                    if (i + j >= 2) {
                        return i + j;
                    } else {
                        printInteger(i-j);
                    }
                }
            }
            return 0;
        }
        main: function void() {
            writeFloat(foo(2, 2));
        }
        """
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test58(self):
        input = """
        main: function void() {
            i: integer = 1;
            while(i < 10)
            {
                printInteger(i);
                return;
            }
        }
            """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test59(self):
        input = """
        checkPrime: function boolean(n : integer)
        {
            i, count : integer = 0, 0;
            for (i = 1, i <= n, i+1)
                if (n % i == 0)
                    count = count + 1;
            if (count == 2)
                return true;
            else
                return false;
        }

        main: function void() {
            printBoolean(checkPrime(10));
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test60(self):
        input = """
        checkValid : boolean = true;
        foo: function void (n: integer)
        {
            if (n % 2 == 0)
                checkValid = true;
            else
                checkValid = false;
        }
        main: function void() {
            foo(20);
            printBoolean(checkValid);
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test61(self):
        input = """
        checkmod2: function void(arr: array [5] of integer)
        {
            i : integer;
            for (i = 0, i < 5, i+1)
                if (arr[i] % 2 == 0)
                    printInteger(i);
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            checkmod2(arr);
        }
            """
        expect = "1\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test62(self):
        input = """
        checkmod2: function void(arr: array [5] of integer)
        {
            i : integer;
            for (i = 0, i < 5, i+1)
                if (arr[i] % 2 == 0)
                    printString("Correct");
                else
                    printString("Wrong");
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            checkmod2(arr);
        }
            """
        expect = "WrongCorrectWrongCorrectWrong"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test63(self):
        input = """
        checkUnique: function boolean(arr: array [5] of integer)
        {
            i, j : integer;
            for (i = 0, i < 5, i+1)
                for (j = i+1 ,j < 5, j+1)
                    if (arr[i] == arr[j])
                        return false;
            return true;
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            printBoolean(checkUnique(arr));
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test64(self):
        input = """
        checkUnique: function boolean(arr: array [5] of integer)
        {
            i, j : integer;
            check : boolean = true;
            for (i = 0, i < 5, i+1)
                for (j = i+1 , j < 5, j+1)
                    if (arr[i] == arr[j])
                        check = false;
            return check;
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 2, 5};
            printBoolean(checkUnique(arr));
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test65(self):
        input = """
        main : function void () {
            f : array [5] of boolean = {true, false, true, false, true};
            printBoolean(f[0]);
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test66(self):
        input = """
        main: function void() {
            arr : array [3] of string = {"Hello", "World", "!"};
            arr[0] = (arr[0]::arr[1])::arr[2];
            printString(arr[0]);
        }
        """
        expect = "HelloWorld!"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test67(self):
        input = """
        main: function void() {
            f : array [5] of boolean = {true, false, true, false, true};
            printBoolean(f[0] && f[1] && f[2] && f[3] && f[4]);
        }
                """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test68(self):
        input = """
        bar: function void(inherit a: integer)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super(10);
            printInteger(a);
            return;
        }
        main : function void () {
            foo();
        }
            """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test69(self):
        input = """
        bar: function void(inherit a: string)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super("Hello");
            printString(a);
            return;
        }
        main : function void () {
            foo();
        }
            """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test70(self):
        input = """
            bar: function void(inherit a: boolean)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super(true);
            printBoolean(a);
            return;
        }
        main : function void () {
            foo();
        }
                """
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test71(self):
        input = """
        foo: function integer (inherit a: integer, inherit b: integer)
        {
            while (a!=0)
                a = a - 1;
            do {
                a = b + 1;
            }
            while (a <= b);
            return a;
        }
        main: function void() {
            printInteger(foo(5, 10));
        }
            """
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test72(self):
        input = """
        checkPrime: function boolean(n : integer)
        {
            i, count : integer = 0, 0;
            for (i = 1, i <= n, i+1)
                if (n % i == 0)
                    count = count + 1;
            if (count == 2)
                return true;
            else
                return false;
        }

        main: function void() {
            printBoolean(checkPrime(10));
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test73(self):
        input = """
        checkValid : boolean = true;
        foo: function void (n: integer)
        {
            if (n % 2 == 0)
                checkValid = true;
            else
                checkValid = false;
        }
        main: function void() {
            foo(20);
            printBoolean(checkValid);
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test74(self):
        input = """
        checkmod2: function void(arr: array [5] of integer)
        {
            i : integer;
            for (i = 0, i < 5, i+1)
                if (arr[i] % 2 == 0)
                    printInteger(i);
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            checkmod2(arr);
        }
            """
        expect = "1\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test75(self):
        input = """
        checkmod2: function void(arr: array [5] of integer)
        {
            i : integer;
            for (i = 0, i < 5, i+1)
                if (arr[i] % 2 == 0)
                    printString("Correct");
                else
                    printString("Wrong");
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            checkmod2(arr);
        }
            """
        expect = "WrongCorrectWrongCorrectWrong"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test76(self):
        input = """
        checkUnique: function boolean(arr: array [5] of integer)
        {
            i, j : integer;
            for (i = 0, i < 5, i+1)
                for (j = i+1 ,j < 5, j+1)
                    if (arr[i] == arr[j])
                        return false;
            return true;
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            printBoolean(checkUnique(arr));
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test77(self):
        input = """
        checkUnique: function boolean(arr: array [5] of integer)
        {
            i, j : integer;
            check : boolean = true;
            for (i = 0, i < 5, i+1)
                for (j = i+1 , j < 5, j+1)
                    if (arr[i] == arr[j])
                        check = false;
            return check;
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 2, 5};
            printBoolean(checkUnique(arr));
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test78(self):
        input = """
        main : function void () {
            f : array [5] of boolean = {true, false, true, false, true};
            printBoolean(f[0]);
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test79(self):
        input = """
        main: function void() {
            arr : array [3] of string = {"Hello", "World", "!"};
            arr[0] = (arr[0]::arr[1])::arr[2];
            printString(arr[0]);
        }
        """
        expect = "HelloWorld!"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test80(self):
        input = """
        main: function void() {
            f : array [5] of boolean = {true, false, true, false, true};
            printBoolean(f[0] && f[1] && f[2] && f[3] && f[4]);
        }
                """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test81(self):
        input = """
        bar: function void(inherit a: integer)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super(10);
            printInteger(a);
            return;
        }
        main : function void () {
            foo();
        }
            """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test82(self):
        input = """
        bar: function void(inherit a: string)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super("Hello");
            printString(a);
            return;
        }
        main : function void () {
            foo();
        }
            """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test83(self):
        input = """
            bar: function void(inherit a: boolean)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super(true);
            printBoolean(a);
            return;
        }
        main : function void () {
            foo();
        }
                """
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test84(self):
        input = """
        foo: function integer (inherit a: integer, inherit b: integer)
        {
            while (a!=0)
                a = a - 1;
            do {
                a = b + 1;
            }
            while (a <= b);
            return a;
        }
        main: function void() {
            printInteger(foo(5, 10));
        }
            """
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    
    def test85(self):
        input = """
        foo: function integer (inherit a: integer, inherit b: integer)
        {
            while (a!=0)
                a = a - 1;
            do {
                a = b + 1;
            }
            while (a <= b);
            return a;
        }
        main: function void() {
            printInteger(foo(5, 10));
        }
            """
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test86(self):
        input = """
        checkPrime: function boolean(n : integer)
        {
            i, count : integer = 0, 0;
            for (i = 1, i <= n, i+1)
                if (n % i == 0)
                    count = count + 1;
            if (count == 2)
                return true;
            else
                return false;
        }

        main: function void() {
            printBoolean(checkPrime(10));
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test87(self):
        input = """
        checkValid : boolean = true;
        foo: function void (n: integer)
        {
            if (n % 2 == 0)
                checkValid = true;
            else
                checkValid = false;
        }
        main: function void() {
            foo(20);
            printBoolean(checkValid);
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test88(self):
        input = """
        checkmod2: function void(arr: array [5] of integer)
        {
            i : integer;
            for (i = 0, i < 5, i+1)
                if (arr[i] % 2 == 0)
                    printInteger(i);
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            checkmod2(arr);
        }
            """
        expect = "1\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test89(self):
        input = """
        checkmod2: function void(arr: array [5] of integer)
        {
            i : integer;
            for (i = 0, i < 5, i+1)
                if (arr[i] % 2 == 0)
                    printString("Correct");
                else
                    printString("Wrong");
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            checkmod2(arr);
        }
            """
        expect = "WrongCorrectWrongCorrectWrong"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test90(self):
        input = """
        checkUnique: function boolean(arr: array [5] of integer)
        {
            i, j : integer;
            for (i = 0, i < 5, i+1)
                for (j = i+1 ,j < 5, j+1)
                    if (arr[i] == arr[j])
                        return false;
            return true;
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 4, 5};
            printBoolean(checkUnique(arr));
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test91(self):
        input = """
        checkUnique: function boolean(arr: array [5] of integer)
        {
            i, j : integer;
            check : boolean = true;
            for (i = 0, i < 5, i+1)
                for (j = i+1 , j < 5, j+1)
                    if (arr[i] == arr[j])
                        check = false;
            return check;
        }
        main: function void() {
            arr: array [5] of integer = {1, 2, 3, 2, 5};
            printBoolean(checkUnique(arr));
        }
            """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test92(self):
        input = """
        main : function void () {
            f : array [5] of boolean = {true, false, true, false, true};
            printBoolean(f[0]);
        }
            """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test93(self):
        input = """
        main: function void() {
            arr : array [3] of string = {"Hello", "World", "!"};
            arr[0] = (arr[0]::arr[1])::arr[2];
            printString(arr[0]);
        }
        """
        expect = "HelloWorld!"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test94(self):
        input = """
        main: function void() {
            f : array [5] of boolean = {true, false, true, false, true};
            printBoolean(f[0] && f[1] && f[2] && f[3] && f[4]);
        }
                """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test95(self):
        input = """
        bar: function void(inherit a: integer)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super(10);
            printInteger(a);
            return;
        }
        main : function void () {
            foo();
        }
            """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test96(self):
        input = """
        bar: function void(inherit a: string)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super("Hello");
            printString(a);
            return;
        }
        main : function void () {
            foo();
        }
            """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test97(self):
        input = """
            bar: function void(inherit a: boolean)
        {
            return;
        }
        foo : function void() inherit bar
        {
            super(true);
            printBoolean(a);
            return;
        }
        main : function void () {
            foo();
        }
                """
        expect = """true\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test98(self):
        input = """
        foo: function integer (inherit a: integer, inherit b: integer)
        {
            while (a!=0)
                a = a - 1;
            do {
                a = b + 1;
            }
            while (a <= b);
            return a;
        }
        main: function void() {
            printInteger(foo(5, 10));
        }
            """
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test99(self):
        input = """
        foo: function integer (inherit a: integer, inherit b: integer)
        {
            while (a!=0)
                a = a - 1;
            do {
                a = b + 1;
            }
            while (a <= b);
            return a;
        }
        main: function void() {
            a: array [2] of integer;
            a[0] = foo(1,2);
            a[1] = foo(2,3);
            printInteger(a[0] + a[1]);
        }
            """
        expect = "7\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test100(self):
        input = """
        foo: function integer (inherit a: integer, inherit b: integer)
        {
            while (a!=0)
                a = a - 1;
            do {
                a = b + 1;
            }
            while (a <= b);
            return a;
        }
        main: function void() {
            a: array [2] of integer;
            a[0] = foo(1,2);
            a[1] = a[0] + foo(2,3);
            printInteger(a[0] + a[1]);
        }
            """
        expect = "10\n"
        self.assertTrue(TestCodeGen.test(input, expect, 600))