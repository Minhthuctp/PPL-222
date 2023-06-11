.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x [I from Label0 to Label1
	bipush 25
	newarray int
	astore_1
	aload_1
	iconst_1
	iconst_5
	imul
	iconst_0
	iadd
	iconst_1
	iastore
	getstatic MT22Class.i I
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	aload_1
	getstatic MT22Class.i I
	iconst_5
	imul
	iconst_0
	iadd
	getstatic MT22Class.i I
	iastore
Label7:
	goto Label5
Label4:
Label8:
	aload_1
	iconst_0
	iconst_5
	imul
	getstatic MT22Class.i I
	iadd
	getstatic MT22Class.i I
	iconst_1
	iadd
	iastore
Label9:
Label5:
	aload_1
	getstatic MT22Class.i I
	iconst_5
	imul
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 12
.limit locals 2
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
	iconst_3
	putstatic MT22Class.i I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
