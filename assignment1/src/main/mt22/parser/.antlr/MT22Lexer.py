# Generated from e:\PPL\assignment1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\3\4\3\4\3\4\7\4\u008f\n\4\f\4\16\4\u0092")
        buf.write("\13\4\3\4\3\4\6\4\u0096\n\4\r\4\16\4\u0097\7\4\u009a\n")
        buf.write("\4\f\4\16\4\u009d\13\4\3\4\3\4\5\4\u00a1\n\4\3\5\3\5\3")
        buf.write("\5\7\5\u00a6\n\5\f\5\16\5\u00a9\13\5\3\5\3\5\6\5\u00ad")
        buf.write("\n\5\r\5\16\5\u00ae\7\5\u00b1\n\5\f\5\16\5\u00b4\13\5")
        buf.write("\5\5\u00b6\n\5\3\6\3\6\7\6\u00ba\n\6\f\6\16\6\u00bd\13")
        buf.write("\6\3\7\3\7\5\7\u00c1\n\7\3\7\6\7\u00c4\n\7\r\7\16\7\u00c5")
        buf.write("\3\b\3\b\5\b\u00ca\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u00d7\n\b\3\t\3\t\5\t\u00db\n\t\3\n\3")
        buf.write("\n\7\n\u00df\n\n\f\n\16\n\u00e2\13\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\38\38\38\39\39\39\39\39\39\39\3:\3:\7:\u019f\n")
        buf.write(":\f:\16:\u01a2\13:\3;\6;\u01a5\n;\r;\16;\u01a6\3;\3;\3")
        buf.write("<\3<\3<\3<\7<\u01af\n<\f<\16<\u01b2\13<\3<\3<\3=\3=\3")
        buf.write("=\3=\7=\u01ba\n=\f=\16=\u01bd\13=\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\5>\u01c6\n>\3?\3?\3?\3@\3@\3@\5@\u01ce\n@\3A\3A\7A\u01d2")
        buf.write("\nA\fA\16A\u01d5\13A\3A\3A\3B\3B\7B\u01db\nB\fB\16B\u01de")
        buf.write("\13B\3B\3B\3B\3C\3C\3C\3\u01bb\2D\3\2\5\2\7\3\t\2\13\2")
        buf.write("\r\2\17\4\21\5\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r")
        buf.write("#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67\30")
        buf.write("9\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]")
        buf.write("+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{\2}\2\177")
        buf.write("\2\u0081:\u0083;\u0085<\3\2\f\3\2\62;\3\2\63;\4\2GGgg")
        buf.write("\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\4\2\f\f\17\17\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\2")
        buf.write("\u01f4\2\7\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u0087")
        buf.write("\3\2\2\2\5\u0089\3\2\2\2\7\u00a0\3\2\2\2\t\u00b5\3\2\2")
        buf.write("\2\13\u00b7\3\2\2\2\r\u00be\3\2\2\2\17\u00d6\3\2\2\2\21")
        buf.write("\u00da\3\2\2\2\23\u00dc\3\2\2\2\25\u00e6\3\2\2\2\27\u00eb")
        buf.write("\3\2\2\2\31\u00f1\3\2\2\2\33\u00f4\3\2\2\2\35\u00f9\3")
        buf.write("\2\2\2\37\u00ff\3\2\2\2!\u0103\3\2\2\2#\u010c\3\2\2\2")
        buf.write("%\u010f\3\2\2\2\'\u0116\3\2\2\2)\u011b\3\2\2\2+\u0121")
        buf.write("\3\2\2\2-\u0126\3\2\2\2/\u012a\3\2\2\2\61\u0133\3\2\2")
        buf.write("\2\63\u0136\3\2\2\2\65\u013e\3\2\2\2\67\u0144\3\2\2\2")
        buf.write("9\u0146\3\2\2\2;\u0148\3\2\2\2=\u014a\3\2\2\2?\u014c\3")
        buf.write("\2\2\2A\u014e\3\2\2\2C\u0150\3\2\2\2E\u0153\3\2\2\2G\u0156")
        buf.write("\3\2\2\2I\u0159\3\2\2\2K\u015c\3\2\2\2M\u015e\3\2\2\2")
        buf.write("O\u0160\3\2\2\2Q\u0163\3\2\2\2S\u0165\3\2\2\2U\u0168\3")
        buf.write("\2\2\2W\u016b\3\2\2\2Y\u016d\3\2\2\2[\u016f\3\2\2\2]\u0171")
        buf.write("\3\2\2\2_\u0173\3\2\2\2a\u0175\3\2\2\2c\u0177\3\2\2\2")
        buf.write("e\u0179\3\2\2\2g\u017b\3\2\2\2i\u017d\3\2\2\2k\u017f\3")
        buf.write("\2\2\2m\u0187\3\2\2\2o\u018d\3\2\2\2q\u0195\3\2\2\2s\u019c")
        buf.write("\3\2\2\2u\u01a4\3\2\2\2w\u01aa\3\2\2\2y\u01b5\3\2\2\2")
        buf.write("{\u01c5\3\2\2\2}\u01c7\3\2\2\2\177\u01cd\3\2\2\2\u0081")
        buf.write("\u01cf\3\2\2\2\u0083\u01d8\3\2\2\2\u0085\u01e2\3\2\2\2")
        buf.write("\u0087\u0088\t\2\2\2\u0088\4\3\2\2\2\u0089\u008a\t\3\2")
        buf.write("\2\u008a\6\3\2\2\2\u008b\u00a1\7\62\2\2\u008c\u0090\5")
        buf.write("\5\3\2\u008d\u008f\5\3\2\2\u008e\u008d\3\2\2\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u009b\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0095\7a\2\2")
        buf.write("\u0094\u0096\5\3\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u009a")
        buf.write("\3\2\2\2\u0099\u0093\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u009f\b\4\2\2\u009f\u00a1\3")
        buf.write("\2\2\2\u00a0\u008b\3\2\2\2\u00a0\u008c\3\2\2\2\u00a1\b")
        buf.write("\3\2\2\2\u00a2\u00b6\7\62\2\2\u00a3\u00a7\5\5\3\2\u00a4")
        buf.write("\u00a6\5\3\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00b2\3")
        buf.write("\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ac\7a\2\2\u00ab\u00ad")
        buf.write("\5\3\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2")
        buf.write("\u00b0\u00aa\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b5\u00a2\3\2\2\2\u00b5\u00a3\3\2\2\2\u00b6")
        buf.write("\n\3\2\2\2\u00b7\u00bb\7\60\2\2\u00b8\u00ba\5\3\2\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bb\u00bc\3\2\2\2\u00bc\f\3\2\2\2\u00bd\u00bb\3\2\2")
        buf.write("\2\u00be\u00c0\t\4\2\2\u00bf\u00c1\t\5\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2")
        buf.write("\u00c4\5\3\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\16\3\2")
        buf.write("\2\2\u00c7\u00c9\5\t\5\2\u00c8\u00ca\5\13\6\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cc\5\r\7\2\u00cc\u00cd\b\b\3\2\u00cd\u00d7\3\2\2\2")
        buf.write("\u00ce\u00cf\5\t\5\2\u00cf\u00d0\5\13\6\2\u00d0\u00d1")
        buf.write("\b\b\4\2\u00d1\u00d7\3\2\2\2\u00d2\u00d3\5\13\6\2\u00d3")
        buf.write("\u00d4\5\r\7\2\u00d4\u00d5\b\b\5\2\u00d5\u00d7\3\2\2\2")
        buf.write("\u00d6\u00c7\3\2\2\2\u00d6\u00ce\3\2\2\2\u00d6\u00d2\3")
        buf.write("\2\2\2\u00d7\20\3\2\2\2\u00d8\u00db\5\'\24\2\u00d9\u00db")
        buf.write("\5\35\17\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\22\3\2\2\2\u00dc\u00e0\7$\2\2\u00dd\u00df\5{>\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3")
        buf.write("\2\2\2\u00e3\u00e4\7$\2\2\u00e4\u00e5\b\n\6\2\u00e5\24")
        buf.write("\3\2\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9")
        buf.write("\7v\2\2\u00e9\u00ea\7q\2\2\u00ea\26\3\2\2\2\u00eb\u00ec")
        buf.write("\7d\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7m\2\2\u00f0\30\3\2\2\2\u00f1\u00f2")
        buf.write("\7f\2\2\u00f2\u00f3\7q\2\2\u00f3\32\3\2\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\34\3\2\2\2\u00f9\u00fa\7h\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\36\3\2\2\2\u00ff\u0100\7h\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7t\2\2\u0102 \3\2\2\2\u0103\u0104")
        buf.write("\7h\2\2\u0104\u0105\7w\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7e\2\2\u0107\u0108\7v\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7q\2\2\u010a\u010b\7p\2\2\u010b\"\3\2\2\2\u010c\u010d")
        buf.write("\7k\2\2\u010d\u010e\7h\2\2\u010e$\3\2\2\2\u010f\u0110")
        buf.write("\7t\2\2\u0110\u0111\7g\2\2\u0111\u0112\7v\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7t\2\2\u0114\u0115\7p\2\2\u0115&\3")
        buf.write("\2\2\2\u0116\u0117\7v\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7w\2\2\u0119\u011a\7g\2\2\u011a(\3\2\2\2\u011b\u011c")
        buf.write("\7y\2\2\u011c\u011d\7j\2\2\u011d\u011e\7k\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\u0120\7g\2\2\u0120*\3\2\2\2\u0121\u0122")
        buf.write("\7x\2\2\u0122\u0123\7q\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7f\2\2\u0125,\3\2\2\2\u0126\u0127\7q\2\2\u0127\u0128")
        buf.write("\7w\2\2\u0128\u0129\7v\2\2\u0129.\3\2\2\2\u012a\u012b")
        buf.write("\7e\2\2\u012b\u012c\7q\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e\u012f\7k\2\2\u012f\u0130\7p\2\2\u0130\u0131")
        buf.write("\7w\2\2\u0131\u0132\7g\2\2\u0132\60\3\2\2\2\u0133\u0134")
        buf.write("\7q\2\2\u0134\u0135\7h\2\2\u0135\62\3\2\2\2\u0136\u0137")
        buf.write("\7k\2\2\u0137\u0138\7p\2\2\u0138\u0139\7j\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a\u013b\7t\2\2\u013b\u013c\7k\2\2\u013c\u013d")
        buf.write("\7v\2\2\u013d\64\3\2\2\2\u013e\u013f\7c\2\2\u013f\u0140")
        buf.write("\7t\2\2\u0140\u0141\7t\2\2\u0141\u0142\7c\2\2\u0142\u0143")
        buf.write("\7{\2\2\u0143\66\3\2\2\2\u0144\u0145\7-\2\2\u01458\3\2")
        buf.write("\2\2\u0146\u0147\7/\2\2\u0147:\3\2\2\2\u0148\u0149\7,")
        buf.write("\2\2\u0149<\3\2\2\2\u014a\u014b\7\61\2\2\u014b>\3\2\2")
        buf.write("\2\u014c\u014d\7\'\2\2\u014d@\3\2\2\2\u014e\u014f\7#\2")
        buf.write("\2\u014fB\3\2\2\2\u0150\u0151\7(\2\2\u0151\u0152\7(\2")
        buf.write("\2\u0152D\3\2\2\2\u0153\u0154\7~\2\2\u0154\u0155\7~\2")
        buf.write("\2\u0155F\3\2\2\2\u0156\u0157\7?\2\2\u0157\u0158\7?\2")
        buf.write("\2\u0158H\3\2\2\2\u0159\u015a\7#\2\2\u015a\u015b\7?\2")
        buf.write("\2\u015bJ\3\2\2\2\u015c\u015d\7?\2\2\u015dL\3\2\2\2\u015e")
        buf.write("\u015f\7>\2\2\u015fN\3\2\2\2\u0160\u0161\7>\2\2\u0161")
        buf.write("\u0162\7?\2\2\u0162P\3\2\2\2\u0163\u0164\7@\2\2\u0164")
        buf.write("R\3\2\2\2\u0165\u0166\7@\2\2\u0166\u0167\7?\2\2\u0167")
        buf.write("T\3\2\2\2\u0168\u0169\7<\2\2\u0169\u016a\7<\2\2\u016a")
        buf.write("V\3\2\2\2\u016b\u016c\7*\2\2\u016cX\3\2\2\2\u016d\u016e")
        buf.write("\7+\2\2\u016eZ\3\2\2\2\u016f\u0170\7]\2\2\u0170\\\3\2")
        buf.write("\2\2\u0171\u0172\7_\2\2\u0172^\3\2\2\2\u0173\u0174\7}")
        buf.write("\2\2\u0174`\3\2\2\2\u0175\u0176\7\177\2\2\u0176b\3\2\2")
        buf.write("\2\u0177\u0178\7=\2\2\u0178d\3\2\2\2\u0179\u017a\7<\2")
        buf.write("\2\u017af\3\2\2\2\u017b\u017c\7.\2\2\u017ch\3\2\2\2\u017d")
        buf.write("\u017e\7\60\2\2\u017ej\3\2\2\2\u017f\u0180\7d\2\2\u0180")
        buf.write("\u0181\7q\2\2\u0181\u0182\7q\2\2\u0182\u0183\7n\2\2\u0183")
        buf.write("\u0184\7g\2\2\u0184\u0185\7c\2\2\u0185\u0186\7p\2\2\u0186")
        buf.write("l\3\2\2\2\u0187\u0188\7h\2\2\u0188\u0189\7n\2\2\u0189")
        buf.write("\u018a\7q\2\2\u018a\u018b\7c\2\2\u018b\u018c\7v\2\2\u018c")
        buf.write("n\3\2\2\2\u018d\u018e\7k\2\2\u018e\u018f\7p\2\2\u018f")
        buf.write("\u0190\7v\2\2\u0190\u0191\7g\2\2\u0191\u0192\7i\2\2\u0192")
        buf.write("\u0193\7g\2\2\u0193\u0194\7t\2\2\u0194p\3\2\2\2\u0195")
        buf.write("\u0196\7u\2\2\u0196\u0197\7v\2\2\u0197\u0198\7t\2\2\u0198")
        buf.write("\u0199\7k\2\2\u0199\u019a\7p\2\2\u019a\u019b\7i\2\2\u019b")
        buf.write("r\3\2\2\2\u019c\u01a0\t\6\2\2\u019d\u019f\t\7\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1t\3\2\2\2\u01a2\u01a0\3\2\2")
        buf.write("\2\u01a3\u01a5\t\b\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a9\b;\7\2\u01a9v\3\2\2\2\u01aa")
        buf.write("\u01ab\7\61\2\2\u01ab\u01ac\7\61\2\2\u01ac\u01b0\3\2\2")
        buf.write("\2\u01ad\u01af\n\t\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b2")
        buf.write("\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\b<\7\2")
        buf.write("\u01b4x\3\2\2\2\u01b5\u01b6\7\61\2\2\u01b6\u01b7\7,\2")
        buf.write("\2\u01b7\u01bb\3\2\2\2\u01b8\u01ba\13\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01bf\7,\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c1\3")
        buf.write("\2\2\2\u01c1\u01c2\b=\7\2\u01c2z\3\2\2\2\u01c3\u01c6\n")
        buf.write("\n\2\2\u01c4\u01c6\5}?\2\u01c5\u01c3\3\2\2\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c6|\3\2\2\2\u01c7\u01c8\7^\2\2\u01c8\u01c9")
        buf.write("\t\13\2\2\u01c9~\3\2\2\2\u01ca\u01cb\7^\2\2\u01cb\u01ce")
        buf.write("\n\13\2\2\u01cc\u01ce\7^\2\2\u01cd\u01ca\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u0080\3\2\2\2\u01cf\u01d3\7$\2\2")
        buf.write("\u01d0\u01d2\5{>\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5\3\2")
        buf.write("\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d6")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d7\bA\b\2\u01d7")
        buf.write("\u0082\3\2\2\2\u01d8\u01dc\7$\2\2\u01d9\u01db\5{>\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01dc\3")
        buf.write("\2\2\2\u01df\u01e0\5\177@\2\u01e0\u01e1\bB\t\2\u01e1\u0084")
        buf.write("\3\2\2\2\u01e2\u01e3\13\2\2\2\u01e3\u01e4\bC\n\2\u01e4")
        buf.write("\u0086\3\2\2\2\32\2\u0090\u0097\u009b\u00a0\u00a7\u00ae")
        buf.write("\u00b2\u00b5\u00bb\u00c0\u00c5\u00c9\u00d6\u00da\u00e0")
        buf.write("\u01a0\u01a6\u01b0\u01bb\u01c5\u01cd\u01d3\u01dc\13\3")
        buf.write("\4\2\3\b\3\3\b\4\3\b\5\3\n\6\b\2\2\3A\7\3B\b\3C\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLIT = 3
    STRLIT = 4
    Auto = 5
    Break = 6
    Do = 7
    Else = 8
    FALSE = 9
    For = 10
    Function = 11
    If = 12
    Return = 13
    TRUE = 14
    While = 15
    Void = 16
    Out = 17
    Continue = 18
    Of = 19
    Inherit = 20
    Array = 21
    ADDOP = 22
    SUBSTROP = 23
    MULOP = 24
    DIVOP = 25
    MODOP = 26
    LOGICALNOT = 27
    LOGICALAND = 28
    LOGICALOR = 29
    EQUAL = 30
    NOTEQUAL = 31
    ASSIGN = 32
    SMALLER = 33
    SMALLEREQUAL = 34
    GREATER = 35
    GREATEREQUAL = 36
    STRCONCAT = 37
    LB = 38
    RB = 39
    LS = 40
    RS = 41
    LP = 42
    RP = 43
    SEMI = 44
    COLON = 45
    COMMA = 46
    DOT = 47
    BOOLEAN = 48
    FLOAT = 49
    INTEGER = 50
    STRING = 51
    ID = 52
    WS = 53
    Line_cmt = 54
    Block_cmt = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'do'", "'else'", "'false'", "'for'", "'function'", 
            "'if'", "'return'", "'true'", "'while'", "'void'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "';'", "':'", "','", "'.'", "'boolean'", 
            "'float'", "'integer'", "'string'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLIT", "STRLIT", "Auto", "Break", "Do", 
            "Else", "FALSE", "For", "Function", "If", "Return", "TRUE", 
            "While", "Void", "Out", "Continue", "Of", "Inherit", "Array", 
            "ADDOP", "SUBSTROP", "MULOP", "DIVOP", "MODOP", "LOGICALNOT", 
            "LOGICALAND", "LOGICALOR", "EQUAL", "NOTEQUAL", "ASSIGN", "SMALLER", 
            "SMALLEREQUAL", "GREATER", "GREATEREQUAL", "STRCONCAT", "LB", 
            "RB", "LS", "RS", "LP", "RP", "SEMI", "COLON", "COMMA", "DOT", 
            "BOOLEAN", "FLOAT", "INTEGER", "STRING", "ID", "WS", "Line_cmt", 
            "Block_cmt", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "DIGIT", "NoZeroDIGIT", "INTLIT", "INTR", "DECR", "EXPR", 
                  "FLOATLIT", "BOOLIT", "STRLIT", "Auto", "Break", "Do", 
                  "Else", "FALSE", "For", "Function", "If", "Return", "TRUE", 
                  "While", "Void", "Out", "Continue", "Of", "Inherit", "Array", 
                  "ADDOP", "SUBSTROP", "MULOP", "DIVOP", "MODOP", "LOGICALNOT", 
                  "LOGICALAND", "LOGICALOR", "EQUAL", "NOTEQUAL", "ASSIGN", 
                  "SMALLER", "SMALLEREQUAL", "GREATER", "GREATEREQUAL", 
                  "STRCONCAT", "LB", "RB", "LS", "RS", "LP", "RP", "SEMI", 
                  "COLON", "COMMA", "DOT", "BOOLEAN", "FLOAT", "INTEGER", 
                  "STRING", "ID", "WS", "Line_cmt", "Block_cmt", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.INTLIT_action 
            actions[6] = self.FLOATLIT_action 
            actions[8] = self.STRLIT_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


