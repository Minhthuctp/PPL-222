.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(II)I
.var 0 is n I from Label0 to Label1
.var 1 is d I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	istore_0
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
Label4:
Label6:
	iload_2
	bipush 10
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_2
	ireturn
Label7:
Label5:
	bipush 10
	ireturn
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	iconst_1
	invokestatic MT22Class/foo(II)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 2
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
