.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "world"
	putstatic MT22Class.x Ljava/lang/String;
	getstatic MT22Class.x Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
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
	ldc "hi"
	putstatic MT22Class.x Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
