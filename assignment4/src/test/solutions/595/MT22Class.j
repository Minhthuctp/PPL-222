.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static bar(I)V
.var 0 is a I from Label0 to Label1
Label0:
	return
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static foo()V
.var 0 is a I from Label0 to Label1
Label0:
	bipush 10
	istore_0
	iload_0
	invokestatic io/printInteger(I)V
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MT22Class/foo()V
Label1:
	return
.limit stack 0
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
