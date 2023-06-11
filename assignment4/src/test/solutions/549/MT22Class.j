.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is n I from Label0 to Label1
	iconst_5
	istore_2
Label2:
Label6:
	iconst_0
	istore_1
Label8:
	iload_1
	iload_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	iload_2
	bipush 20
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	goto Label11
	goto Label17
Label16:
	iload_2
	iconst_1
	iadd
	istore_2
Label17:
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label11:
Label9:
	goto Label5
Label7:
Label4:
	iconst_1
	ifle Label3
	goto Label2
Label5:
Label3:
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
.limit locals 3
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
