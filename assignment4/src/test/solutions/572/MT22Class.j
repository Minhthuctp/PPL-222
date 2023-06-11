.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static checkPrime(I)Z
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is count I from Label0 to Label1
	iconst_0
	istore_2
	iconst_1
	istore_1
Label2:
	iload_1
	iload_0
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label11
Label10:
Label11:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label5:
Label3:
	iload_2
	iconst_2
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	iconst_1
	ireturn
Label14:
	iconst_0
	ireturn
Label15:
Label1:
.limit stack 10
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MT22Class/checkPrime(I)Z
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
