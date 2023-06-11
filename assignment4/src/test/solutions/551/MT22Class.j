.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
Label6:
.var 2 is j I from Label6 to Label7
	iconst_0
	istore_2
Label10:
Label12:
	iload_2
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
Label14:
	iload_1
	iload_2
	iadd
	iconst_0
	if_icmplt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label13
	goto Label19
Label18:
Label19:
	iload_2
	iconst_1
	iadd
	istore_2
Label15:
	goto Label10
Label13:
Label11:
	iload_1
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label7:
Label4:
	iload_1
	bipush 10
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label3
	goto Label2
Label5:
Label3:
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
