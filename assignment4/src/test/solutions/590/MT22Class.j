.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static checkUnique([I)Z
.var 0 is arr [I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
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
	iload_1
	iconst_1
	iadd
	istore_2
Label8:
	iload_2
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	aload_0
	iload_1
	iaload
	aload_0
	iload_2
	iaload
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	iconst_0
	ireturn
Label16:
Label17:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
Label11:
Label9:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label5:
Label3:
	iconst_1
	ireturn
Label1:
.limit stack 11
.limit locals 3
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
	invokestatic MT22Class/checkUnique([I)Z
	invokestatic io/printBoolean(Z)V
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
