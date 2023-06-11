.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x F
.field static y F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.x F
	invokestatic io/writeFloat(F)V
	getstatic MT22Class.y F
	invokestatic io/writeFloat(F)V
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
	i2f
	putstatic MT22Class.x F
	ldc 10.5
	putstatic MT22Class.y F
Label1:
	return
.limit stack 2
.limit locals 0
.end method
