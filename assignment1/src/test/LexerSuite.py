import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    """Check lowercase ID"""
    def test_lowercase_identifier1(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_lowercase_identifier2(self):
        self.assertTrue(TestLexer.test("zavc", "zavc,<EOF>", 102))

    """Check uppercase ID"""
    def test_uppercase_identifier1(self):
        self.assertTrue(TestLexer.test("ABCBA", "ABCBA,<EOF>", 103))
    def test_uppercase_identifier2(self):
        self.assertTrue(TestLexer.test("ASGSA", "ASGSA,<EOF>", 104))

    """Check mix ID"""
    def test_mix_upperlower_identifier1(self):
        self.assertTrue(TestLexer.test("uABCAu", "uABCAu,<EOF>", 105))
    def test_mix_upperlower_identifier2(self):
        self.assertTrue(TestLexer.test("AUKuaaaa", "AUKuaaaa,<EOF>", 106))
    def test_mix_upperlower_identifier3(self):
        self.assertTrue(TestLexer.test("aUaZUz", "aUaZUz,<EOF>", 107))
    def test_mix_upperlower_identifier4(self):
        self.assertTrue(TestLexer.test("UaZazzz", "UaZazzz,<EOF>", 108))

    """Check underscore ID"""
    def test_underscore_identifier1(self):
        self.assertTrue(TestLexer.test("_ancaaAB123", "_ancaaAB123,<EOF>", 109))
    def test_underscore_identifier2(self):
        self.assertTrue(TestLexer.test("_abc_123_ab", "_abc_123_ab,<EOF>", 110))
    def test_underscore_identifier3(self):
        self.assertTrue(TestLexer.test("ANC_asb_123", "ANC_asb_123,<EOF>", 111))
    def test_underscore_identifier4(self):
        self.assertTrue(TestLexer.test("123abc123_", "123,abc123_,<EOF>", 112))
    def test_underscore_identifier5(self):
        self.assertTrue(TestLexer.test("abc__abc", "abc__abc,<EOF>", 113))
    def test_underscore_identifier6(self):
        self.assertTrue(TestLexer.test("_N_Z_123", "_N_Z_123,<EOF>", 114))
    def test_underscore_identifier7(self):
        self.assertTrue(TestLexer.test("abc#abc", "abc,Error Token #", 115))
    def test_underscore_identifier8(self):
        self.assertTrue(TestLexer.test("!abcabc", "!,abcabc,<EOF>", 116))
    def test_underscore_identifier9(self):
        self.assertTrue(TestLexer.test("@abcabc", "Error Token @", 117))
    def test_underscore_identifier10(self):
        self.assertTrue(TestLexer.test("__123", "__123,<EOF>", 118))

    """Check integer literal"""
    def test_integer_literal1(self):
        self.assertTrue(TestLexer.test("1234", "1234,<EOF>", 119))
    def test_integer_literal2(self):
        self.assertTrue(TestLexer.test("123_4123", "1234123,<EOF>", 120))
    def test_integer_literal3(self):
        self.assertTrue(TestLexer.test("1_2_3_4", "1234,<EOF>", 121))
    def test_integer_literal4(self):
        self.assertTrue(TestLexer.test("1_2_3_4_", "1234,_,<EOF>", 122))
    def test_integer_literal5(self):
        self.assertTrue(TestLexer.test("1_2__3__4", "12,__3__4,<EOF>", 123))

    """Check float literal full"""
    def test_float_literal1(self):
        self.assertTrue(TestLexer.test("12_2.e-3", "122.e-3,<EOF>", 124))
    def test_float_literal2(self):
        self.assertTrue(TestLexer.test("122_12.12e+3", "12212.12e+3,<EOF>", 125))
    def test_float_literal3(self):
        self.assertTrue(TestLexer.test("_1234.e124", "_1234,.e124,<EOF>", 126))
   
    """Check float (INT DEC)"""
    def test_float_literal4(self):
        self.assertTrue(TestLexer.test("124.0000001", "124.0000001,<EOF>", 127))
    def test_float_literal5(self):
        self.assertTrue(TestLexer.test("0000000.000000", "0,0,0,0,0,0,0.000000,<EOF>", 128))
    def test_float_literal6(self):
        self.assertTrue(TestLexer.test("1_124.123", "1124.123,<EOF>", 129))
    def test_float_literal7(self):
        self.assertTrue(TestLexer.test("1_1_2.", "112.,<EOF>", 130))
    
    """Check float (INT EXP)"""
    def test_float_literal8(self):
        self.assertTrue(TestLexer.test("124e3", "124e3,<EOF>", 131))
    def test_float_literal9(self):
        self.assertTrue(TestLexer.test("123_2e-000000", "1232e-000000,<EOF>", 132))
    def test_float_literal10(self):
        self.assertTrue(TestLexer.test("1_2_4e12_32", "124e12,_32,<EOF>", 133))
    def test_float_literal11(self):
        self.assertTrue(TestLexer.test("123e+3", "123e+3,<EOF>", 134))

    """Check float (DEC EXP)"""
    def test_float_literal12(self):
        self.assertTrue(TestLexer.test(".e3", ".e3,<EOF>", 135))
    def test_float_literal13(self):
        self.assertTrue(TestLexer.test(".0000e-0", ".0000e-0,<EOF>", 136))
    def test_float_literal14(self):
        self.assertTrue(TestLexer.test(".112e+3", ".112e+3,<EOF>", 137))
    def test_float_literal15(self):
        self.assertTrue(TestLexer.test(".1e+3_3", ".1e+3,_3,<EOF>", 138))

    """Check string literal"""
    def test_string_literal1(self):
        self.assertTrue(TestLexer.test("\" What are you doing? \"", " What are you doing? ,<EOF>", 139))
    def test_string_literal2(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"", "This is a string containing tab \\t,<EOF>", 140))
    def test_string_literal3(self):
        self.assertTrue(TestLexer.test("\"Hi, My name \\b is \\n John\"", "Hi, My name \\b is \\n John,<EOF>", 141))
    def test_string_literal4(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" Where is John? \\\"\" ", "He asked me: \\\" Where is John? \\\",<EOF>", 142))
    def test_string_literal5(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' sentence\"", "This \\' is a \\' sentence,<EOF>", 143))
    def test_string_literal6(self):
        self.assertTrue(TestLexer.test("\"How \\\\ are \\r you?\"", "How \\\\ are \\r you?,<EOF>", 144))
    def test_string_literal7(self):
        self.assertTrue(TestLexer.test("\"I will \\f be there \\b for you\"", "I will \\f be there \\b for you,<EOF>", 145))
    def test_string_literal8(self):
        self.assertTrue(TestLexer.test("\"Now \\b \\f I \\'m \\r \\n \\t \\\' \\\\ here\" ", "Now \\b \\f I \\'m \\r \\n \\t \\\' \\\\ here,<EOF>", 146))
    def test_string_literal9(self):
        self.assertTrue(TestLexer.test("\"This is \\t \\b \\f the end.\"", "This is \\t \\b \\f the end.,<EOF>", 147))
    def test_string_literal10(self):
        self.assertTrue(TestLexer.test("\"Hello, what \\'are\\' you doing ?\"", "Hello, what \\'are\\' you doing ?,<EOF>", 148))
        
    """Check unclosed string"""
    def test_unclosed_string_literal1(self):
        self.assertTrue(TestLexer.test("\" What are you doing?", "Unclosed String:  What are you doing?", 149))
    def test_unclosed_string_literal2(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t", "Unclosed String: This is a string containing tab \\t", 150))
    def test_unclosed_string_literal3(self):
        self.assertTrue(TestLexer.test("\"Hi, My name \\b is \\n John", "Unclosed String: Hi, My name \\b is \\n John", 151))
    def test_unclosed_string_literal4(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" Where is John? \\\"", "Unclosed String: He asked me: \\\" Where is John? \\\"", 152))
    def test_unclosed_string_literal5(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' sentence", "Unclosed String: This \\' is a \\' sentence", 153))

    """Check illegal string"""
    def test_illegal_string_literal1(self):
        self.assertTrue(TestLexer.test("\" What are you doing? \\a", "Illegal Escape In String:  What are you doing? \\a", 154))
    def test_illegal_string_literal2(self):
        self.assertTrue(TestLexer.test("\"This is a string \\h containing tab \\t", "Illegal Escape In String: This is a string \\h", 155))
    def test_illegal_string_literal3(self):
        self.assertTrue(TestLexer.test("\"Hi, My name \\b \\w is \\n John", "Illegal Escape In String: Hi, My name \\b \\w", 156))
    def test_illegal_string_literal4(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" \\c Where is John? \\\"", "Illegal Escape In String: He asked me: \\\" \\c", 157))
    def test_illegal_string_literal5(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' \\m sentence", "Illegal Escape In String: This \\' is a \\' \\m", 158))

    "Check boolean literal"
    def test_boolean_literal1(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 159))
    def test_boolean_literal2(self):
        self.assertTrue(TestLexer.test("false true", "false,true,<EOF>", 160))

    "Check operator"
    def test_operator1(self):
        self.assertTrue(TestLexer.test("==-==", "==,-,==,<EOF>", 161))
    def test_operator2(self):
        self.assertTrue(TestLexer.test("123+321", "123,+,321,<EOF>", 162))
    def test_operator3(self):
        self.assertTrue(TestLexer.test("[1+3,1,abc]", "[,1,+,3,,,1,,,abc,],<EOF>", 163))
    def test_operator4(self):
        self.assertTrue(TestLexer.test("1!=2", "1,!=,2,<EOF>", 164))
    def test_operator5(self):
        self.assertTrue(TestLexer.test("123&&333 123%1", "123,&&,333,123,%,1,<EOF>", 165))
    def test_operator6(self):
        self.assertTrue(TestLexer.test("-3-4-1-5", "-,3,-,4,-,1,-,5,<EOF>", 166))
    def test_operator7(self):
        self.assertTrue(TestLexer.test("abc<=abc", "abc,<=,abc,<EOF>", 167))
    def test_operator8(self):
        self.assertTrue(TestLexer.test("===", "==,=,<EOF>", 168))
    def test_operator9(self):
        self.assertTrue(TestLexer.test("abc::::abc", "abc,::,::,abc,<EOF>", 169))
    def test_operator10(self):
        self.assertTrue(TestLexer.test("====", "==,==,<EOF>", 170))

    """Check keywords && seperator"""
    def test_keywords1(self):
        self.assertTrue(TestLexer.test("auto break boolean do else false float", "auto,break,boolean,do,else,false,float,<EOF>", 171))
    def test_keywords2(self):
        self.assertTrue(TestLexer.test("for function if integer return string true", "for,function,if,integer,return,string,true,<EOF>", 172))
    def test_keywords3(self):
        self.assertTrue(TestLexer.test("while void out continue of inherit array", "while,void,out,continue,of,inherit,array,<EOF>", 173))
    def test_keywords4(self):
        self.assertTrue(TestLexer.test("+-*/%!&&||==!=<<=>>=::", "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>", 174))
    def test_keywords5(self):
        self.assertTrue(TestLexer.test("()[].,;:{}=", "(,),[,],.,,,;,:,{,},=,<EOF>", 175))

    """Check complex"""
    def test_complex1(self):
        self.assertTrue(TestLexer.test("a: integer;", "a,:,integer,;,<EOF>", 176))
    def test_complex2(self):
        self.assertTrue(TestLexer.test("""{
            r = r * a[0];
            b,c: array [4] of string;
        }""", "{,r,=,r,*,a,[,0,],;,b,,,c,:,array,[,0,],of,string,},<EOF>", 177))
    def test_complex3(self):
        self.assertTrue(TestLexer.test("foo(3);", "foo,(,3,),;,<EOF>", 178))
    def test_complex4(self):
        self.assertTrue(TestLexer.test("""{
            abc = a[0,1,2];
            return true;
        }""", "{,abc,=,a,[,0,,,1,,,2,],;,return,true,;,},<EOF>", 179))
    def test_complex1(self):
        self.assertTrue(TestLexer.test("a: integer;", "a,:,integer,;,<EOF>", 176))
    def test_complex2(self):
        self.assertTrue(TestLexer.test("""{
            r = r * a[0];
            b,c: array [4] of string;
        }""", "{,r,=,r,*,a,[,0,],;,b,,,c,:,array,[,4,],of,string,;,},<EOF>", 177))
    def test_complex3(self):
        self.assertTrue(TestLexer.test("foo(3);", "foo,(,3,),;,<EOF>", 178))
    def test_complex4(self):
        self.assertTrue(TestLexer.test("""{
            abc = a[0,1,2];
            return true;
        }""", "{,abc,=,a,[,0,,,1,,,2,],;,return,true,;,},<EOF>", 179))
    def test_complex5(self):
        self.assertTrue(TestLexer.test("if a!=b a=b; ", "if,a,!=,b,a,=,b,;,<EOF>", 180))
    def test_complex6(self):
        self.assertTrue(TestLexer.test("""{
            for (a=1,a<0,a=a+1) 
                b=b+1;
        }""", "{,for,(,a,=,1,,,a,<,0,,,a,=,a,+,1,),b,=,b,+,1,;,},<EOF>", 181))
    def test_complex7(self):
        self.assertTrue(TestLexer.test("a,b,c,d: integer = 2,3,4,5;", "a,,,b,,,c,,,d,:,integer,=,2,,,3,,,4,,,5,;,<EOF>", 182))
    def test_complex8(self):
        self.assertTrue(TestLexer.test("""{
            main: function void() {}
        }""", "{,main,:,function,void,(,),{,},},<EOF>", 183))
    def test_complex9(self):
        self.assertTrue(TestLexer.test("do {} while a=b;", "do,{,},while,a,=,b,;,<EOF>", 184))
    def test_complex10(self):
        self.assertTrue(TestLexer.test("""
            foo: function void(a : integer, out x:float) inherit bar {}
        """, "foo,:,function,void,(,a,:,integer,,,out,x,:,float,),inherit,bar,{,},<EOF>", 185))
    
    """Test random"""
    def test_random1(self):
        self.assertTrue(TestLexer.test("1..1..1..1", "1.,.,1.,.,1.,.,1,<EOF>", 186))
    def test_random2(self):
        self.assertTrue(TestLexer.test("1a___1___a1", "1,a___1___a1,<EOF>", 187))
    def test_random3(self):
        self.assertTrue(TestLexer.test("{1_32,2_12,3_12,4_1,5_4}", "{,132,,,212,,,312,,,41,,,54,},<EOF>", 188))
    def test_random4(self):
        self.assertTrue(TestLexer.test("""{
            r, s: int;
            r = 2.0;
            a, b: array [5] of int;
            s = r * r * myPI;
            a[0] = s;
            }
        """, "{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>", 189))
    def test_random5(self):
        self.assertTrue(TestLexer.test("_____________", "_____________,<EOF>", 190))

    """Test comment"""
    def test_comment1(self):
        self.assertTrue(TestLexer.test("// hello world", "<EOF>", 191))
    def test_comment2(self):
        self.assertTrue(TestLexer.test("// ancnnnnn a \n anc", "anc,<EOF>", 192))
    def test_comment3(self):
        self.assertTrue(TestLexer.test("// THIS IS A \t \b \z COMMENT", "<EOF>", 193))
    def test_comment4(self):
        self.assertTrue(TestLexer.test("// This \t is \b a \w beautiful \w moment", "<EOF>", 194))
    def test_comment5(self):
        self.assertTrue(TestLexer.test("// This // is // a // beautiful // moment", "<EOF>", 195))
    
    def test_comment6(self):
        self.assertTrue(TestLexer.test("/* This is a comment */", "<EOF>", 196))
    def test_comment7(self):
        self.assertTrue(TestLexer.test("""
         /* hellllooo
                holllloo
                    hellllloooo
                                */
        """, "<EOF>", 197))
    def test_comment8(self):
        self.assertTrue(TestLexer.test("""
            /* /* \t \a \b \a \f \t */
        """, "<EOF>", 198))
    def test_comment9(self):
        self.assertTrue(TestLexer.test(""" /* /*
            Just a small test for assignment
        */ */
        """, "*,/,<EOF>", 199))
    def test_comment10(self):
        self.assertTrue(TestLexer.test("""
            /* \\This is a comment */
        """, "<EOF>", 200))