.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static checkValid Z

.method public static foo(I)V
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
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
	iconst_1
	putstatic MT22Class.checkValid Z
	goto Label5
Label4:
	iconst_0
	putstatic MT22Class.checkValid Z
Label5:
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 20
	invokestatic MT22Class/foo(I)V
	getstatic MT22Class.checkValid Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 1
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
	iconst_1
	putstatic MT22Class.checkValid Z
Label1:
	return
.limit stack 2
.limit locals 0
.end method
