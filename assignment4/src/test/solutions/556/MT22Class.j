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
Label2:
	iload_2
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
Label12:
Label14:
	iload_0
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label13
Label16:
	iload_2
	ireturn
Label17:
Label15:
Label13:
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label5:
Label3:
	bipush 10
	ireturn
Label1:
.limit stack 6
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
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
