.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
Label4:
Label6:
	iload_0
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_0
	iconst_1
	isub
	istore_0
	goto Label4
Label7:
Label5:
Label8:
Label12:
	iload_1
	iconst_1
	iadd
	istore_0
Label13:
Label10:
	iload_0
	iload_1
	if_icmpgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label9
	goto Label8
Label11:
Label9:
	iload_0
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_2
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iconst_2
	invokestatic MT22Class/foo(II)I
	iastore
	aload_1
	iconst_1
	iconst_2
	iconst_3
	invokestatic MT22Class/foo(II)I
	iastore
	aload_1
	iconst_0
	iaload
	aload_1
	iconst_1
	iaload
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
