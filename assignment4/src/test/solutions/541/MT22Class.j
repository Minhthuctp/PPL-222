.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static i I
.field static j I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MT22Class.i I
Label2:
	getstatic MT22Class.i I
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	iconst_1
	putstatic MT22Class.j I
Label10:
	getstatic MT22Class.j I
	iconst_5
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label11
Label16:
	getstatic MT22Class.i I
	getstatic MT22Class.j I
	iadd
	iconst_2
	if_icmplt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
Label22:
	getstatic MT22Class.i I
	getstatic MT22Class.j I
	iadd
	invokestatic io/printInteger(I)V
Label23:
	goto Label21
Label20:
Label24:
	getstatic MT22Class.i I
	getstatic MT22Class.j I
	isub
	invokestatic io/printInteger(I)V
Label25:
Label21:
Label17:
Label12:
	getstatic MT22Class.j I
	iconst_1
	iadd
	putstatic MT22Class.j I
	goto Label10
Label13:
Label11:
Label9:
Label4:
	getstatic MT22Class.i I
	iconst_1
	iadd
	putstatic MT22Class.i I
	goto Label2
Label5:
Label3:
Label1:
	return
.limit stack 9
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
