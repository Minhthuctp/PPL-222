from functools import reduce
from typing import List
from Utils import *
from AST import *
from Visitor import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC


class MType:
    def __init__(self, partype, rettype, param = None):
        self.partype = partype
        self.rettype = rettype
        self.param = param


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"

class ArrayPointerType(Type):
    def __init__(self, eleType,size = 0,dimension: List[int] = []):
        self.eleType = eleType
        self.size = size
        self.dimension = dimension

    def __str__(self):
        return "ArrayPointerType({0}, [{1}], {2})".format(str(self.size), ", ".join([str(dimen) for dimen in self.dimension]), str(self.eleType))

    def accept(self, v, param):
        return None

class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None

class CodeUtils:
    @staticmethod
    def getType(typ):
        if isinstance(typ,ArrayType):
            size = reduce(lambda pre,curr: pre*curr,typ.dimensions)
            return ArrayPointerType(typ.typ,size,typ.dimensions)
        return typ
    
    @staticmethod
    def checkType(typ1,typ2):
        return FloatType() if (isinstance(typ1,FloatType) or isinstance(typ2,FloatType)) else IntegerType() 

    @staticmethod
    def isNumberOp(op):
        return op in ["+","-","*","/","%"]
    
    @staticmethod
    def isStringOp(op):
        return op == "::"
    
    @staticmethod
    def isNumberBoolOp(op):
        return op in [">","<",">=","<=","==","!="]

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType([], IntegerType()),CName(self.libName)),
        Symbol("printInteger", MType([IntegerType()], VoidType()),CName(self.libName)),
        Symbol("readFloat", MType([], FloatType()),CName(self.libName)),
        Symbol("writeFloat", MType([FloatType()], VoidType()),CName(self.libName)),
        Symbol("readBoolean", MType([], BooleanType()),CName(self.libName)),
        Symbol("printBoolean", MType([BooleanType()], VoidType()),CName(self.libName)),
        Symbol("readString", MType([], StringType()),CName(self.libName)),
        Symbol("printString", MType([StringType()], VoidType()),CName(self.libName)),
        Symbol("super",MType([List[Expr]],VoidType()),CName(self.libName)),
        Symbol("preventDefault",MType([],VoidType()),CName(self.libName))
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym, isGlobal = False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal


class Access():
    def __init__(self, frame, sym, isLeft, eleType = None):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.eleType = eleType

class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return "Index({})".format(str(self.value))


class CName(Val):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return "CName({})".format(str(self.value))

class GetEnv(BaseVisitor):
    def __init__(self,astTree):
        self.astTree = astTree
        self.className = "MT22Class"
    
    def visitProgram(self, ast: Program, o: SubBody):    
        for x in ast.decls:
            if (isinstance(x,FuncDecl)):
                funcSym = self.visit(x,o)
                o.sym = [funcSym] + o.sym
        return o
    
    def visitFuncDecl(self, ast: FuncDecl, o: SubBody):
        param = []
        for x in ast.params:
            typ = CodeUtils.getType(x.typ)
            param+=[ParamDecl(x.name,typ,x.out,x.inherit)]
        return Symbol(ast.name, MType([CodeUtils.getType(x.typ) for x in ast.params], ast.return_type,ast.params), CName(self.className))
    

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.globalVardecls = []
        self.curIndex = 0

    def visitProgram(self, ast: Program, c):
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        globalEnv = self.env
        globalFrame = Frame("<clinit>",VoidType)
        globalEnv = GetEnv(self.astTree).visit(ast,SubBody(None,globalEnv)).sym
        for decl in ast.decls:
            if (isinstance(decl,FuncDecl)):
                self.visit(decl,SubBody(None,globalEnv))
            else:
                varSym = self.visit(decl,SubBody(globalFrame,globalEnv,isGlobal=True))
                globalEnv = [varSym] + globalEnv

        self.genMETHOD(FuncDecl("<init>", None, list(), None, BlockStmt(list())), globalEnv, Frame("<init>", VoidType()))
        self.genMETHOD(FuncDecl("<clinit>", None, list(), None, BlockStmt(list())), globalEnv, globalFrame)

        # [self.visit(i, c)for i in ast.decl]
        # return c

        self.emit.emitEPILOG()
        return c
    
    def visitParamDecl(self,ast:ParamDecl,o: SubBody):
        typ = CodeUtils.getType(ast.typ)
        index = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(index, ast.name, typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return SubBody(o.frame,[Symbol(ast.name,typ,Index(index))]+o.sym)

    def genMETHOD(self, func: FuncDecl, o, frame: Frame):
        isInit = func.return_type is None and func.name == "<init>"
        isStaticInit = func.return_type is None and func.name == "<clinit>"
        isMain = func.name == "main" and len(func.params) == 0 and type(func.return_type) is VoidType
        returnType = VoidType() if isInit or isStaticInit else CodeUtils.getType(func.return_type)
        intype = [ArrayPointerType(StringType())] if isMain else list(
            map(lambda x: CodeUtils.getType(x.typ), func.params))
        mtype = MType(intype, returnType)
        self.emit.printout(self.emit.emitMETHOD(
            func.name, mtype, not isInit, frame))

        if not isStaticInit:
            frame.enterScope(False)
        else:
            frame.enterScope(False)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        # local = reduce(lambda env, ele: SubBody(
        #         frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
        # glenv = local.sym+glenv
        localSubBody = SubBody(frame,glenv) 
        for param in func.params:
            localSubBody = self.visit(param,localSubBody)
        parentSym = None
        if (func.inherit is not None):
            for sym in glenv:
                if (func.inherit == sym.name):
                    parentSym = sym
                    break
            for x in parentSym.mtype.param:
                if (x.inherit == True):
                    inherit_typ = CodeUtils.getType(x.typ)
                    index = frame.getNewIndex()
                    self.emit.printout(self.emit.emitVAR(index, x.name, inherit_typ, localSubBody.frame.getStartLabel(), localSubBody.frame.getEndLabel(), localSubBody.frame))
                    localSubBody.sym = [Symbol(x.name,inherit_typ,Index(index))] + localSubBody.sym

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        if isStaticInit:
            for (name,typ,initCode) in self.globalVardecls:
                if isinstance(typ,ArrayPointerType):
                    self.emit.printout(self.emit.emitInitNewStaticArray(self.className+"."+name,typ.size,typ.eleType,initCode,frame))
                else:
                    if (initCode!=""):
                        self.emit.printout(initCode+self.emit.emitPUTSTATIC(self.className+"."+name,typ,frame))
        if (parentSym is not None):
            if (len(func.body.body)!=0):
                stmt = func.body.body[0]
                if (len(parentSym.mtype.partype) == 0):
                    for x in func.body.body:
                        if (isinstance(x,VarDecl)):
                            localSubBody = self.visit(x,localSubBody)
                        else:
                            self.visit(x,localSubBody)
                else:
                    if (stmt.name == "super"):
                        for i, arg in enumerate(stmt.args):
                            if (parentSym.mtype.param[i].inherit == True):
                                self.visit(AssignStmt(Id(parentSym.mtype.param[i].name),arg),localSubBody)
                    for x in func.body.body[1:]:
                        if (isinstance(x,VarDecl)):
                            localSubBody = self.visit(x,localSubBody)
                        else:
                            self.visit(x,localSubBody)

        else:
            for x in func.body.body:
                if (isinstance(x,VarDecl)):
                    localSubBody = self.visit(x,localSubBody)
                else:
                    self.visit(x,localSubBody)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    
    def visitVarDecl(self,ast:VarDecl,o: SubBody):
        frame = o.frame
        typ = CodeUtils.getType(ast.typ)
        initCode = ""
        if (ast.init):
            if (isinstance(ast.init,ArrayLit)):
                self.curIndex = 0
                frame.push()
                access = Access(o.frame,o.sym,False,typ.eleType)
            else:
                access= Access(frame,o.sym,False)
            initCode, initTyp = self.visit(ast.init,access)
            if (isinstance(ast.init,ArrayLit)):
                frame.pop()
            initTyp = CodeUtils.getType(initTyp)
            if (isinstance(initTyp,IntegerType) and isinstance(typ,FloatType)):
                initCode += self.emit.emitI2F(frame)
        if (o.isGlobal):
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name,typ,False))
            self.globalVardecls.append((ast.name,typ,initCode))
            return Symbol(ast.name,typ,CName(self.className))
        index = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(index,ast.name,typ,frame.getStartLabel(),frame.getEndLabel(),frame))
        if (isinstance(typ,ArrayPointerType)):
            self.emit.printout(self.emit.emitInitNewLocalArray(index,typ.size,typ.eleType,initCode,frame))
        elif (ast.init):
            self.emit.printout(initCode + self.emit.emitWRITEVAR(ast.name,typ,index,frame))
        return SubBody(frame,[Symbol(ast.name,typ,Index(index))] + o.sym,o.isGlobal)

    def visitFuncDecl(self, ast:FuncDecl, o:SubBody):
        frame = Frame(ast.name, ast.return_type)
        self.genMETHOD(ast, o.sym, frame)
    
    #=================================Statement========================================
    def visitAssignStmt(self, ast: AssignStmt, o: SubBody):
        if (isinstance(ast.lhs,ArrayCell)):
            o.frame.push()
            o.frame.push()
        rhsCode, rhsType = self.visit(ast.rhs,Access(o.frame,o.sym,False))
        lhsCode, lhsType = self.visit(ast.lhs,Access(o.frame,o.sym,True))
        if (isinstance(rhsType,IntegerType) and isinstance(lhsType,FloatType)):
            rhsCode += self.emit.emitI2F(o.frame)
        if (isinstance(ast.lhs,ArrayCell)):
            self.emit.printout(lhsCode[0] + rhsCode + lhsCode[1])
        else:
            self.emit.printout(rhsCode + lhsCode)

    def visitIfStmt(self, ast: IfStmt, o: SubBody):
        expCode, expType = self.visit(ast.cond,Access(o.frame,o.sym,False))
        self.emit.printout(expCode)
        label1 = o.frame.getNewLabel()
        label2 = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label1,o.frame))
        hasReturnStmt = self.visit(ast.tstmt,o) is True
        if (not hasReturnStmt):
            self.emit.printout(self.emit.emitGOTO(label2,o.frame))
        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        if (ast.fstmt):
            self.visit(ast.fstmt,o)
        self.emit.printout(self.emit.emitLABEL(label2,o.frame))
        return hasReturnStmt

    def visitForStmt(self, ast: ForStmt, o: SubBody):
        exprCode, exprType = self.visit(ast.init.rhs,Access(o.frame,o.sym,False))
        initCode, initType = self.visit(ast.init.lhs,Access(o.frame,o.sym,True))
        
        self.emit.printout(exprCode + initCode)

        label1 = o.frame.getNewLabel()
        label2 = o.frame.getNewLabel()

        o.frame.enterLoop()

        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        condCode, condType = self.visit(ast.cond,Access(o.frame,o.sym,False))
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label2,o.frame))
        hasReturnStmt = self.visit(ast.stmt,o) is True
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame))
        updateCode, updateType = self.visit(ast.upd,Access(o.frame,o.sym,False))
        self.emit.printout(updateCode + initCode)
        if (not hasReturnStmt):
            self.emit.printout(self.emit.emitGOTO(label1,o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(),o.frame))
        self.emit.printout(self.emit.emitLABEL(label2,o.frame))
        
        o.frame.exitLoop()

    def visitWhileStmt(self, ast: WhileStmt, o: SubBody):
        exprCode, exprType = self.visit(ast.cond,Access(o.frame,o.sym,False))

        label1 = o.frame.getNewLabel()
        label2 = o.frame.getNewLabel()

        o.frame.enterLoop()
        
        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame))
        self.emit.printout(exprCode)
        self.emit.printout(self.emit.emitIFFALSE(label2,o.frame))
        hasReturnStmt = self.visit(ast.stmt,o) is True
        if (not hasReturnStmt):
            self.emit.printout(self.emit.emitGOTO(label1,o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(),o.frame))
        self.emit.printout(self.emit.emitLABEL(label2,o.frame))

        o.frame.exitLoop()

    def visitDoWhileStmt(self, ast: DoWhileStmt, o: SubBody):
        label1 = o.frame.getNewLabel()
        label2 = o.frame.getNewLabel()

        o.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(label1,o.frame))
        hasReturnStmt = self.visit(ast.stmt,o) is True
        
        exprCode, exprType = self.visit(ast.cond,Access(o.frame,o.sym,False))
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame))
        self.emit.printout(exprCode)
        self.emit.printout(self.emit.emitIFFALSE(label2,o.frame))
        if (not hasReturnStmt):
            self.emit.printout(self.emit.emitGOTO(label1,o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(),o.frame))
        self.emit.printout(self.emit.emitLABEL(label2,o.frame))

        o.frame.exitLoop()
    
    def visitContinueStmt(self, ast: ContinueStmt, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitBreakStmt(self, ast: BreakStmt, o: SubBody):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
    
    def visitReturnStmt(self, ast: ReturnStmt, o: SubBody):
        return_type = o.frame.returnType
        if ast.expr:
            exprCode, exprTyp = self.visit(ast.expr, Access(o.frame, o.sym, False))
            if type(exprTyp) is IntegerType and type(return_type) is FloatType:
                exprCode += self.emit.emitI2F(o.frame)
            self.emit.printout(exprCode)
        self.emit.printout(self.emit.emitRETURN(return_type, o.frame))
        return True

    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        for sym in o.sym:
            if (sym.name == ast.name):
                funcSym = sym
                break

        argsCode = ""
        for i, arg in enumerate(ast.args):
            argCode, argTyp = self.visit(arg, Access(o.frame, o.sym, False))
            if type(argTyp) is IntegerType and type(funcSym.mtype.partype[i]) is FloatType:
                argCode += self.emit.emitI2F(o.frame)
            argsCode += argCode
        self.emit.printout(argsCode + self.emit.emitINVOKESTATIC(funcSym.value.value + "/" + funcSym.name, funcSym.mtype, o.frame))

    def visitBlockStmt(self, ast: BlockStmt, o: SubBody):
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(),o.frame))
        hasReturnStmt = False
        for x in ast.body:
            if isinstance(x,VarDecl):
                o = self.visit(x,o)
            else:
                hasReturnStmt = self.visit(x,o)
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(),o.frame))
        o.frame.exitScope()
        return hasReturnStmt


    #====================Expression==========================
    def visitIntegerLit(self, ast:IntegerLit, o: Access):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
    
    def visitFloatLit(self, ast:FloatLit, o: Access):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()

    def visitBooleanLit(self, ast:BooleanLit, o: Access):
        return self.emit.emitPUSHICONST(str(ast.val).lower(), o.frame), BooleanType()
    
    def visitStringLit(self, ast:StringLit, o: Access):
        return self.emit.emitPUSHCONST(str(ast.val), StringType(), o.frame), StringType()
    
    def visitArrayCell(self, ast: ArrayCell, o: Access):
        arrCode, arrType = self.visit(Id(ast.name),o)
        # changeDimension = list(map(lambda x: self.visit(IntegerLit(x),o)[0],arrType.dimension))
        # codeGetCell = [self.visit(x,o)[0] for x in ast.cell]
        cellCode = ""
        cellLst = []
        if (len(arrType.dimension) == len(ast.cell)):
            for i, curCell in enumerate(ast.cell):
                cell = self.visit(curCell,Access(o.frame,o.sym,False))[0]
                currDimension = ""
                for x in arrType.dimension[i+1:]:
                    currDimension = self.visit(IntegerLit(x),o)[0]
                    cell = cell + currDimension + self.emit.emitMULOP("*",IntegerType(),o.frame)
                cellLst += [cell]
            cellCode += reduce(lambda pre,curr: pre + curr + self.emit.emitADDOP("+",IntegerType(),o.frame),cellLst[1:],cellLst[0])
        if (o.isLeft):
            return [arrCode + cellCode, self.emit.emitASTORE(arrType.eleType,o.frame)], arrType.eleType
        else:
            return arrCode + cellCode + self.emit.emitALOAD(arrType.eleType,o.frame), arrType.eleType
    
    def visitArrayLit(self, ast: ArrayLit, o: Access):
        frame = o.frame
        eleType = o.eleType
        resCode = ""
        for expr in ast.explist:
            if (isinstance(expr,ArrayLit)):
                exprCode, exprType = self.visit(expr,Access(frame,o.sym,o.isLeft,eleType))
                resCode += exprCode
            else:
                exprCode, exprType = self.visit(expr,o)
                if (isinstance(exprType,IntegerType) and isinstance(eleType,FloatType)):
                    exprCode += self.emit.emitI2F(frame)
                resCode += self.emit.emitDUP(frame) +  self.emit.emitPUSHICONST(self.curIndex,frame) + exprCode + self.emit.emitASTORE(eleType,frame)
                self.curIndex += 1
        return resCode, eleType

    def visitBinExpr(self, ast: BinExpr, o: Access):
        str1, typ1 = self.visit(ast.left, o)
        str2, typ2 = self.visit(ast.right, o)
        frame = o.frame

        if  (CodeUtils.isNumberOp(ast.op) or CodeUtils.isNumberBoolOp(ast.op)):
            result_typ = CodeUtils.checkType(typ1,typ2)
            if ast.op == "/":
                result_typ = FloatType()
            if (isinstance(typ1,IntegerType) and isinstance(result_typ,FloatType)):
                str1 = str1 + self.emit.emitI2F(frame)
            if (isinstance(typ2,IntegerType) and isinstance(result_typ,FloatType)):
                str2 = str2 + self.emit.emitI2F(frame)
            if (CodeUtils.isNumberOp(ast.op)):
                if (ast.op in ["+","-"]):
                    return str1 + str2 + self.emit.emitADDOP(ast.op,result_typ,frame), result_typ
                elif (ast.op in ["*","/"]):
                    return str1 + str2 + self.emit.emitMULOP(ast.op,result_typ,frame), result_typ
                else:
                    return str1 + str2 + self.emit.emitMOD(frame), result_typ
            else:
                return str1 + str2 + self.emit.emitREOP(ast.op,result_typ,frame), BooleanType()
        elif CodeUtils.isStringOp(ast.op):
            cName = CName("java/lang/String").value
            mtype = MType([StringType()],StringType())
            return str1 + str2 + self.emit.emitINVOKEVIRTUAL(cName + "/" + "concat",mtype,frame), StringType()
        else:
            if (ast.op == "&&"):
                return str1 + str2 + (self.emit.emitANDOP(frame)), BooleanType()
            else:
                return str1 + str2 + (self.emit.emitOROP(frame)), BooleanType()
            
    def visitUnExpr(self, ast: UnExpr, o: Access):
        expstr, typ = self.visit(ast.val,o)
        if (ast.op=="!"):
            return expstr + self.emit.emitNOT(typ,o.frame), typ
        else:
            return expstr + self.emit.emitNEGOP(typ,o.frame), typ

    def visitId(self, ast: Id, o: Access):
        for x in o.sym:
            if (ast.name == x.name):
                if (isinstance(x.value,CName)):
                    if (o.isLeft and not isinstance(x.mtype,ArrayPointerType)):
                        return self.emit.emitPUTSTATIC(x.value.value+"."+ast.name,x.mtype,o.frame), x.mtype
                    else:
                        return self.emit.emitGETSTATIC(x.value.value+"."+ast.name,x.mtype,o.frame), x.mtype
                else:
                    if (o.isLeft and not isinstance(x.mtype,ArrayPointerType)):
                        return self.emit.emitWRITEVAR(ast.name,x.mtype,x.value.value,o.frame), x.mtype
                    else:
                        return self.emit.emitREADVAR(ast.name,x.mtype,x.value.value,o.frame), x.mtype
    
    def visitFuncCall(self, ast: FuncCall, o: Access):
        for sym in o.sym:
            if (sym.name == ast.name):
                funcSym = sym
                break

        argsCode = ""
        for i, arg in enumerate(ast.args):
            argCode, argTyp = self.visit(arg, Access(o.frame, o.sym, False))
            if type(argTyp) is IntegerType and type(funcSym.mtype.partype[i]) is FloatType:
                argCode += self.emit.emitI2F(o.frame)
            argsCode += argCode
            
        funcCode = argsCode + self.emit.emitINVOKESTATIC(funcSym.value.value + "/" + funcSym.name, funcSym.mtype, o.frame)
        return funcCode, funcSym.mtype.rettype