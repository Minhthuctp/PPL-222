.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [Ljava/lang/String; from Label0 to Label1
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Hello"
	aastore
	dup
	iconst_1
	ldc "World"
	aastore
	dup
	iconst_2
	ldc "!"
	aastore
	astore_1
	aload_1
	iconst_0
	aload_1
	iconst_0
	aaload
	aload_1
	iconst_1
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_1
	iconst_2
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aastore
	aload_1
	iconst_0
	aaload
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
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
