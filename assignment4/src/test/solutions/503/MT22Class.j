.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x I
.field static y I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.x I
	invokestatic io/printInteger(I)V
	getstatic MT22Class.y I
	invokestatic io/printInteger(I)V
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
	putstatic MT22Class.x I
	iconst_2
	putstatic MT22Class.y I
Label1:
	return
.limit stack 2
.limit locals 0
.end method
