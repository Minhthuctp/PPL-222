.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is f [Z from Label0 to Label1
	iconst_5
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	dup
	iconst_3
	iconst_0
	bastore
	dup
	iconst_4
	iconst_1
	bastore
	astore_1
	aload_1
	iconst_0
	baload
	aload_1
	iconst_1
	baload
	iand
	aload_1
	iconst_2
	baload
	iand
	aload_1
	iconst_3
	baload
	iand
	aload_1
	iconst_4
	baload
	iand
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 9
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
