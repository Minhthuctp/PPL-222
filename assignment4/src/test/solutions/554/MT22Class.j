.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MT22Class.i I
Label2:
	getstatic MT22Class.i I
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	getstatic MT22Class.i I
	invokestatic io/printInteger(I)V
	return
Label9:
Label4:
	getstatic MT22Class.i I
	iconst_1
	iadd
	putstatic MT22Class.i I
Label5:
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
