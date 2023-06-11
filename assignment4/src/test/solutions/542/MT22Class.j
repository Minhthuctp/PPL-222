.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_1
	istore_1
Label2:
	iload_1
	i2f
	ldc 5.0
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	iconst_1
	istore_2
Label10:
	iload_2
	i2f
	ldc 5.0
	fcmpl
	ifge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label11
Label16:
	iload_1
	iload_2
	iadd
	i2f
	ldc 2.0
	fcmpl
	iflt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
Label22:
	iload_1
	iload_2
	iadd
	invokestatic io/printInteger(I)V
Label23:
	goto Label21
Label20:
Label24:
	iload_1
	iload_2
	isub
	invokestatic io/printInteger(I)V
Label25:
Label21:
Label17:
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label13:
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
Label1:
	return
.limit stack 9
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
