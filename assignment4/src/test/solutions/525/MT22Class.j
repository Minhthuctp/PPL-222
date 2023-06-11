.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 11.5
	bipush 20
	i2f
	fmul
	bipush 100
	i2f
	ldc 2.1
	fmul
	fsub
	ldc 10.5
	iconst_3
	i2f
	fmul
	iconst_3
	iconst_5
	imul
	i2f
	fadd
	bipush 10
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	bipush 10
	i2f
	fadd
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/printBoolean(Z)V
	ldc 11.5
	bipush 20
	i2f
	fmul
	bipush 100
	i2f
	ldc 2.1
	fmul
	fsub
	ldc 10.5
	iconst_3
	i2f
	fmul
	iconst_3
	iconst_5
	imul
	i2f
	fadd
	bipush 10
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	bipush 10
	i2f
	fadd
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/printBoolean(Z)V
	ldc 11.5
	bipush 20
	i2f
	fmul
	bipush 100
	i2f
	ldc 2.1
	fmul
	fsub
	ldc 10.5
	iconst_3
	i2f
	fmul
	iconst_3
	iconst_5
	imul
	i2f
	fadd
	bipush 10
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	bipush 10
	i2f
	fadd
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/printBoolean(Z)V
	ldc 11.5
	bipush 20
	i2f
	fmul
	bipush 100
	i2f
	ldc 2.1
	fmul
	fsub
	ldc 10.5
	iconst_3
	i2f
	fmul
	iconst_3
	iconst_5
	imul
	i2f
	fadd
	bipush 10
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	bipush 10
	i2f
	fadd
	fcmpl
	iflt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/printBoolean(Z)V
	ldc 11.5
	bipush 20
	i2f
	fmul
	bipush 100
	i2f
	ldc 2.1
	fmul
	fsub
	ldc 10.5
	iconst_3
	i2f
	fmul
	iconst_3
	iconst_5
	imul
	i2f
	fadd
	bipush 10
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	bipush 10
	i2f
	fadd
	fcmpl
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/printBoolean(Z)V
	ldc 11.5
	bipush 20
	i2f
	fmul
	bipush 100
	i2f
	ldc 2.1
	fmul
	fsub
	ldc 10.5
	iconst_3
	i2f
	fmul
	iconst_3
	iconst_5
	imul
	i2f
	fadd
	bipush 10
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	bipush 10
	i2f
	fadd
	fcmpl
	ifeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 14
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
