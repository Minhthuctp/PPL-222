.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static checkmod2([I)V
.var 0 is arr [I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	aload_0
	iload_1
	iaload
	iconst_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	ldc "Correct"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label11
Label10:
	ldc "Wrong"
	invokestatic io/printString(Ljava/lang/String;)V
Label11:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label5:
Label3:
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
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
	astore_1
	aload_1
	invokestatic MT22Class/checkmod2([I)V
Label1:
	return
.limit stack 4
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
