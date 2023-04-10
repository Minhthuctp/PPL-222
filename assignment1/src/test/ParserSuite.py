import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    """Test program structure"""
    def test_program_structure1(self):
        input = """"""
        expect = """Error on line 1 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_program_structure2(self):
        input = """a : integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_program_structure3(self):
        input = """a,b : float;
                main: function void() {}
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_program_structure4(self):
        input = """main: function void(){} 
            foo: function string(){}
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_program_structure5(self):
        input = """foo: function auto() {}
            a : integer;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_program_structure6(self):
        input = """bar: function void() {}
            if (a==b) 
                print(a);
        """
        expect = """Error on line 2 col 12: if"""
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_program_structure7(self):
        input = """
            b : boolean = true;
            c = b;
        """
        expect = """Error on line 3 col 14: ="""
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_program_structure8(self):
        input = """
            break: function void() {}
        """
        expect = """Error on line 2 col 12: break"""
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_program_structure9(self):
        input = """
            continue: integer = 2;
        """
        expect = """Error on line 2 col 12: continue"""
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_program_structure10(self):
        input = """
            while = hello;
        """
        expect = """Error on line 2 col 12: while"""
        self.assertTrue(TestParser.test(input, expect, 210))


    """Test variable declaration"""
    def test_variable_decleration1(self):
        input = """
            a: integer;
            b: float;
            c,d: auto;
            f: boolean;
            e,g,h: boolean;
            i,j: array[3,4,5] of void;            
        """
        expect = """Error on line 7 col 33: void"""
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_variable_decleration2(self):
        input = """
            a : integer = 3;
            b,c : float = a+1,5;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_variable_decleration3(self):
        input = """
            a: auto = 3;
            b,c,d: integer = 1,2;
        """
        expect = """Error on line 3 col 32: ;"""
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_variable_decleration4(self):
        input = """
            a,b,c,d: float = 1+2,3,4,5,7+8;
        """
        expect = """Error on line 2 col 38: ,"""
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_variable_decleration5(self):
        input = """
            a,b : array[5] of integer = {1,2,3},{2,3,4};
            c: float = 2.2;
            d: boolean = true;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 215))

    """Test function declaration"""
    def test_function_decleration1(self):
        input = """
            foo: function auto()           
        """
        expect = """Error on line 3 col 8: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_function_decleration2(self):
        input = """
            main: function array[5] of string () {}
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_function_decleration3(self):
        input = """
            foo: function float (n : integer, inherit out a,b,c: float) {}
        """
        expect = """Error on line 2 col 59: ,"""
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_function_decleration4(self):
        input = """
            main: function boolean (n: auto, b: integer, a: float) inherit foo {}
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_function_decleration5(self):
        input = """
            foo: function string (a: string, b: float) {}
            main: function auto (a: void, b: float) {}
        """
        expect = """Error on line 3 col 36: void"""
        self.assertTrue(TestParser.test(input, expect, 220))
    
    """Test array index"""
    def test_array_index1(self):
        input = """
            a : array [5] of string = {1,2,3};       
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_array_index2(self):
        input = """
            a : array [10] of float = {{1,2,4},{1,2,4},{1,2,4}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_array_index3(self):
        input = """
            a,b : array [2] of string = {},{};
            main: function void ()
            {
                return a[{1,2,3},2,3,4];
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_array_index4(self):
        input = """
            main: function void() {
                return a[1];
                return {1,2,3};
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_array_index5(self):
        input = """
            main: function void() {
                return a[id+1,a,c,true+false];
                return {1,2,3};
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 225))

    """Test operator"""
    def test_operator1(self):
        input = """
            a: integer = a::b;       
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_operator2(self):
        input = """
            a: boolean = True && False && True || False :: e;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_operator3(self):
        input = """
            a,b : string = 1+2+3*4+5+6,!True;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_operator4(self):
        input = """
            a: integer = a!=b + !2 + -2;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_operator5(self):
        input = """
                b: integer = 2 || 2 + 3 / 3 + a[2] + c && d;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_operator6(self):
        input = """
            c : float = id + a[1,2,3,4] + -2 + -4 + !true + !false;    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_operator7(self):
        input = """
            a: string = !id > 3 + 2 / 5 <= 6; 
        """
        expect = """Error on line 2 col 40: <="""
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_operator8(self):
        input = """
            a,b : string = 1+2+3*4+5+6,!True;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_operator9(self):
        input = """
            a: integer = a!=b + !2 + -2;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_operator10(self):
        input = """
                b: integer = !-2 + 3 + 3 <= >= 3;
        """
        expect = """Error on line 2 col 44: >="""
        self.assertTrue(TestParser.test(input, expect, 235))

    """Test statement"""
    """Test assignment statement"""
    def test_assign_stmt1(self):
        input = """
            main: function void() {
                a = 2,3,4;
            }      
        """
        expect = """Error on line 3 col 21: ,"""
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_assign_stmt2(self):
        input = """
            main: function void() {
                a = b + c - d - a[1,2,3];
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_assign_stmt3(self):
        input = """
            main: function void() {
                a = 2+4;
                b = "anc"+ "cfg" +5;
                c = 2.3;
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_assign_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                if (a==1)
                    a = a + 1;
            }  
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_assign_stmt5(self):
        input = """
            foo : function integer() {}
            main: function void() {
                a = foo();
                b = foo();
                a = b = foo();
            }       
        """
        expect = """Error on line 6 col 22: ="""
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_assign_stmt6(self):
        input = """
            main: function void() {
                a = b = c = 5;
            }      
        """
        expect = """Error on line 3 col 22: ="""
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_assign_stmt7(self):
        input = """
            main: function void() {
                b = a || 2 + 3 + foo(2,3,4,1+2);
                c = a_2 + 3 + 111_223;
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_assign_stmt8(self):
        input = """
            bar: function integer() {
                a = x**y + y**x;
            }    
        """
        expect = """Error on line 3 col 22: *"""
        self.assertTrue(TestParser.test(input, expect, 243))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_assign_stmt10(self):
        input = """
            foo : function integer() {
                d = inc(3) + 3;
                h = d + 2 + -2 + -3;
            }       
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245))

    """Test if statement"""
    def test_if_else_stmt1(self):
        input = """
            main: function void() {
                if (a+c=d)
                    b = b + c;
            }      
        """
        expect = """Error on line 3 col 23: ="""
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_if_else_stmt2(self):
        input = """
            main: function void() {
                if (a > b > c)
                    o = c - 1;
                else
                    c = d - f;
            }    
        """
        expect = """Error on line 3 col 26: >"""
        self.assertTrue(TestParser.test(input, expect, 247))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_if_else_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                if ((a!=1) && (a==f) || (c=d))
                    a = a + 1;
            }  
        """
        expect = """Error on line 4 col 42: ="""
        self.assertTrue(TestParser.test(input, expect, 249))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))

    """Test for statement"""
    def test_for_stmt1(self):
        input = """
            main: function void() {
                for (a = 1, a < 10 + 20, a + 1)
                {
                
                }
            }      
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_for_stmt2(self):
        input = """
            main: function void() {
                for (b == 1, b < 10 , b + 1)
                {
                    print(a[i]);
                }
            }    
        """
        expect = """Error on line 3 col 23: =="""
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_for_stmt3(self):
        input = """
            main: function void() {
                for (a=1,b<2,c+1)
                    print(a[i]);
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_for_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                for (a = 1,b<=20+30,c = c + 1)
                    print(a[i]);
            }  
        """
        expect = """Error on line 4 col 38: ="""
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_for_stmt5(self):
        input = """
            main: function void() {
                for (c=2,c==3,c+1)
                {
                
                }
            }       
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))

    """Test while-do statement"""
    def test_while_do_stmt1(self):
        input = """
            main: function void() {
                while ((a==b) && (c<=3));
            }      
        """
        expect = """Error on line 3 col 40: ;"""
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_while_do_stmt2(self):
        input = """
            main: function void() {
                while ((anc) + (cnd) == d)
                {
                
                }
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_while_do_stmt3(self):
        input = """
            main: function void() {
                while ((anc+nccc) || (aaaa+vc!=c)
                {
                
                }
            }    
        """
        expect = """Error on line 4 col 16: {"""
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_while_do_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                while ((a<=c) || (c>=d) || (d==c))
                    print(a);
            }  
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_while_do_stmt5(self):
        input = """
            main: function void() {
                while ((a=c) || (d))
                {
                
                }
            }       
        """
        expect = """Error on line 3 col 25: ="""
        self.assertTrue(TestParser.test(input, expect, 260))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_do_while_stmt2(self):
        input = """
            main: function void() {
                do
                while (a==c);
            }    
        """
        expect = """Error on line 4 col 16: while"""
        self.assertTrue(TestParser.test(input, expect, 262))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_do_while_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                do
                    c = c + 1;
                while (a==c);
            }  
        """
        expect = """Error on line 5 col 20: c"""
        self.assertTrue(TestParser.test(input, expect, 264))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))
    
    """Test other statement"""
    def test_other_stmt1(self):
        input = """
            main: function void() {
                return;
            }      
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_other_stmt2(self):
        input = """
            main: function void() {
                return abc[1,2,3,4,5];
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_other_stmt3(self):
        input = """
            main: function void() {
                break;
            }    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_other_stmt4(self):
        input = """
            a : integer = 2;
            main: function void() {
                break abc;
            }  
        """
        expect = """Error on line 4 col 22: abc"""
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_other_stmt5(self):
        input = """
            main: function void() {
                continue;
                continue abc;
            }       
        """
        expect = """Error on line 4 col 25: abc"""
        self.assertTrue(TestParser.test(input, expect, 270))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_simple_program4(self):
        input = """
            main: function boolean (n: auto, b: integer, a: float) inherit foo {
                for (i=1,i<=10,i+1)
                    print(i);
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_simple_program5(self):
        input = """
            foo: function string (a: string, b: float) {
                do {
                    print("hello");
                }
                while (a==b);
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_simple_program6(self):
        input = """
            foo: function auto() {
                break anv;
            }           
        """
        expect = """Error on line 3 col 22: anv"""
        self.assertTrue(TestParser.test(input, expect, 276))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_simple_program8(self):
        input = """
            foo: function float (n : integer, inherit out a: float) {
                return ;
            }
            a : integer = 3;
            b : float = 2.5;
            c : string = "anc_ac \\t \\b";
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_simple_program9(self):
        input = """
            main: function boolean (n: auto, b: integer, a: float) inherit foo {
                while (a=b)
                    print("Hello");
                a==c;
            }
        """
        expect = """Error on line 3 col 24: ="""
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_simple_program10(self):
        input = """
            foo: function string (a: string, b: float) {
                foo(2,x+3,foo(3),a[3]);
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))

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
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 282))

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
                    print("anc dbafd \\t \\f",d);
                }
                while (a==true);
            }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))

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
        expect = """Error on line 6 col 26: !"""
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_simple_program15(self):
        input = """
            foo: function float(a : integer, b: float)
            {
                if ((a==b) && (c==d)
                    return true;
                else
                    return false;
            }
        """
        expect = """Error on line 5 col 20: return"""
        self.assertTrue(TestParser.test(input, expect, 285))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_anc(self):
        input = """
            main: function void() {
                while (1)
                 a=20;
            }       
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 400))