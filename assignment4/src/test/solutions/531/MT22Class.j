.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.x [I
	iconst_0
	bipush 10
	iastore
	getstatic MT22Class.x [I
	iconst_2
	bipush 20
	iastore
	getstatic MT22Class.x [I
	iconst_1
	iaload
	getstatic MT22Class.x [I
	iconst_2
	iaload
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
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
	iconst_5
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
	dup
	iconst_4
	iconst_5
	iastore
	putstatic MT22Class.x [I
Label1:
	return
.limit stack 4
.limit locals 0
.end method
