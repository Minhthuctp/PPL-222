.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is x [I from Label0 to Label1
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	astore_2
	aload_2
	iconst_1
	iconst_2
	imul
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	iadd
	iconst_2
	irem
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	aload_2
	iload_1
	iconst_2
	imul
	iconst_0
	iadd
	iload_1
	iastore
Label7:
	goto Label5
Label4:
Label8:
	aload_2
	iconst_0
	iconst_2
	imul
	iload_1
	iadd
	iload_1
	iconst_1
	iadd
	iastore
Label9:
Label5:
	aload_2
	iconst_0
	iconst_2
	imul
	iload_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 10
.limit locals 3
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
