from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self,param,rettype):
        self.param = param
        self.rettype = rettype

    def __str__(self):
        return str(self.partype) + " " + str(self.rettype)

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + ", " + [str(x) for x in self.mtype] + ", " +str(self.value)

def infer(id,typ,env):
    for x in env:
        if x.get(id) is not None:
            if (isinstance(x[id],list)):
                if (x[id][1] is not None):
                    func_name = x[id][1]
                    func = env[1].get(func_name)
                    for i in range(0,len(func["param"])):
                        if (func["param"][i].name == id):
                            func["param"][i].typ = typ
                            break
                x[id][1] = typ
            return

class GetEnv(Visitor):

    def visitProgram(self, ast:Program, o):
        o = [{}]
        for x in ast.decls:
            if (isinstance(x,FuncDecl)):
                self.visit(x,o)
        return o
    
    # def visitVarDecl(self, ast, o):
    #     if (o[0].get(ast.name) is not None):
    #         raise Redeclared(Variable(),ast.name)
    #     o[0][ast.name] = self.visit(ast.typ,o)

    def visitFuncDecl(self, ast: FuncDecl, o):
        if (o[0].get(ast.name) is not None):
            return
        typ = ast.return_type
        o[0][ast.name] = {
            "name": ast.name,
            "typ" : typ,
            "parent": ast.inherit,
            "param": ast.params
        }


class StaticChecker(Visitor):
    global_env = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("printFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
        Symbol("super",MType([],VoidType())),
        Symbol("preventDefault",MType([],VoidType()))
    ]

    def __init__(self,ast):
        self.ast = ast
        self.illegal_array_lit = False

    def check_type(self,typ1,typ2):
        if (isinstance(typ1,FloatType) and isinstance(typ2,IntegerType)):
            return True
        if (isinstance(typ1,ArrayType) and (isinstance(typ2,ArrayType))):
            if (typ1.dimensions==typ2.dimensions):
                return self.check_type(typ1.typ,typ2.typ)
            else:
                return False
        if (isinstance(typ1,type(typ2))):
            return True
        return False
    
    def check(self):
        return self.visit(self.ast, {})

    def visitProgram(self, ast:Program, o):
        
        find_main_func = False
        for x in ast.decls:
            if (isinstance(x,FuncDecl) and (isinstance(x.return_type,VoidType)) and (len(x.params)==0)):
                find_main_func = True
        o = GetEnv().visit(ast,o)
        o = [{}] + o
        for x in ast.decls:
            self.visit(x,o)
        if (find_main_func == False):
            raise NoEntryPoint()
        return []
                    
    def visitVarDecl(self, ast: VarDecl, o):
        if (o[0].get(ast.name) is not None):
            raise Redeclared(Variable(),ast.name)
        o[0][ast.name] = self.visit(ast.typ,o)
        typ = o[0][ast.name][0]
        if (ast.init is not None):
            init = self.visit(ast.init,o)
            init_typ = init[0]
            if (isinstance(typ,AutoType)):
                o[0][ast.name][0] = init_typ
                return
            if (isinstance(init_typ,AutoType)):
                init_typ = typ
                infer(ast.init.name,typ,o)
            if (self.check_type(typ,init_typ) == False):
                raise TypeMismatchInVarDecl(ast)            
        else:
            if (isinstance(o[0][ast.name][0],AutoType)):
                raise Invalid(Variable(), ast.name)    

    def visitParamDecl(self, ast:ParamDecl, o):
        (env,func_name) = o
        if (env[0].get(ast.name) is not None):
            raise Redeclared(ParamDecl(),ast.name)
        env[0][ast.name] = [ast.typ,func_name]

    def visitFuncDecl(self, ast: FuncDecl, o):
        prototype = o[1].get(ast.name)
        if (o[0].get(ast.name)):
            raise Redeclared(Function(),ast.name)
        
        env = [{}] + o
        for x in prototype["param"]:
            self.visit(x,(env,ast.name))

        o[0][ast.name] = prototype
        
        # env = [{}] + o

        # for x in o[0][ast.name]["param"]:
        #     env[0][x[0]] = x[1]
        if (o[0][ast.name]["parent"] is not None):
            if (ast.body.body is None):
                raise InvalidStatementInFunction(ast)
            if (isinstance((ast.body.body[0]),CallStmt)):
                stmt = ast.body.body[0]
                if ((stmt.name == "super") or (ast.name == "preventDefault")):
                    if (stmt.name == "super"):
                        parent = self.visit(Id(ast.inherit),env)
                        if (isinstance(parent,dict)):
                            if (len(parent["param"]) == len(stmt.args)):
                                for i in range(0,len(parent["param"])):
                                    param1 = parent["param"][i]
                                    param2 = self.visit(stmt.args[i],env)
                                    typ1 = param1.typ
                                    typ2 = param2[0]
                                    if (isinstance(typ1,AutoType)):
                                        parent["param"][i].typ = typ2
                                        typ1 = typ2
                                    if (isinstance(typ2,AutoType)):
                                        infer(stmt.args[i].name,typ1,env)
                                        typ2 = typ1
                                    if (self.check_type(typ1,typ2) == False):
                                        print(typ1,typ2)
                                        raise TypeMismatchInExpression(stmt)
                                for x in parent["param"]:
                                    if (x.inherit == True):
                                        if (env[0].get(x.name) is not None):
                                            raise Invalid(ParamDecl(),x.name)
                                        env[0][x.name] = x.typ
                            else:
                                raise TypeMismatchInExpression(stmt)
                        else:
                            raise Undeclared(Function(),ast.inherit)
                else:
                    InvalidStatementInFunction(ast.name)
            else:
                raise InvalidStatementInFunction(ast.name)    
            for x in ast.body.body[1:]:
                if (isinstance(x,VarDecl)):
                    self.visit(x,env)
                else:
                    self.visit(x,(False,o[0][ast.name]["typ"],env))
        else:
            for x in ast.body.body:
                if (isinstance(x,VarDecl)):
                    self.visit(x,env)
                else:
                    self.visit(x,(False,o[0][ast.name]["typ"],env))
        #     for x in ast.body.body[1:]:
        #         if (isinstance(x,VarDecl)):
        #             self.visit(x,env)
        #         else: 
        #             self.visit(x,(False,o[0][ast.name]["typ"],env))
        # else:
        #     for x in ast.body.body:
        #         if (isinstance(x,VarDecl)):
        #             self.visit(x,env)
        #         else: 
        #             self.visit(x,(False,o[0][ast.name]["typ"],env))
        
    def visitAssignStmt(self, ast: AssignStmt, o): 
        (in_loop,typ,env) = o
        lhs = self.visit(ast.lhs,env)
        rhs = self.visit(ast.rhs,env)

        lhs_typ = lhs[0]
        rhs_typ = rhs[0]

        print(lhs_typ,rhs_typ)
        if (isinstance(lhs_typ,ArrayType)):
            raise TypeMismatchInExpression(ast)

        if (isinstance(lhs_typ,AutoType)):
            lhs_typ = rhs_typ
            infer(ast.lhs.name,rhs_typ,env)

        if (isinstance(rhs_typ,AutoType)):
            rhs_typ = lhs_typ
            infer(ast.rhs.name,lhs_typ,env)
        
        if (self.check_type(lhs_typ,rhs_typ)==False):
            print(10)
            raise TypeMismatchInStatement(ast)
        # elif (isinstance(lhs_typ,FloatType)):
        #     if (not isinstance(rhs_typ,(IntegerType,FloatType))):
        #         raise TypeMismatchInExpression(ast)
        
        # elif (not isinstance(lhs,type(rhs))):
        #     raise TypeMismatchInExpression(ast)
    
    def visitBlockStmt(self, ast: BlockStmt, o):
        (in_loop,typ,env) = o
        inner = [{}] + env
        for x in ast.body:
            if (isinstance(x,VarDecl)):
                self.visit(x,inner)
            else:
                self.visit(x,(in_loop,typ,inner))
    
    def visitIfStmt(self, ast: IfStmt, o): 
        (in_loop,typ,env) = o
        cond = self.visit(ast.cond,env)

        if (isinstance(cond,BooleanType)):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.tstmt,(in_loop,typ,env))

        if (ast.fstmt is not None):
            self.visit(ast.fstmt,(in_loop,typ,env))
    
    def visitForStmt(self, ast: ForStmt, o):
        (in_loop,typ,env) = o
        id = self.visit(ast.init.lhs,env)
        init = self.visit(ast.init.rhs,env)
        cond = self.visit(ast.cond,env)
        upd = self.visit(ast.upd,env)
        init_typ = init[0]
        cond_typ = cond[0]
        upd_typ = upd[0]
        id_typ = id[0]

        if (isinstance(id_typ,AutoType)):
            id_typ = IntegerType()
            infer(id.name,IntegerType(),env)
        
        if (isinstance(init_typ,AutoType)):
            init_typ = IntegerType()
            infer(init.name,IntegerType(),env)
        
        if (isinstance(cond_typ,AutoType)):
            cond_typ = BooleanType()
            infer(cond.name,IntegerType(),env)
        
        if (isinstance(upd_typ,AutoType)):
            upd_typ = BooleanType()
            infer(upd.name,IntegerType(),env)

        if (not isinstance(init_typ,IntegerType) or (not isinstance(upd_typ,IntegerType)) or (not isinstance(cond_typ,BooleanType))):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.stmt,(True,typ,env))

    
    def visitWhileStmt(self, ast:WhileStmt, o): 
        (in_loop,typ,env) = o
        cond = self.visit(ast.cond,env)
        cond_typ = cond[0]

        if (isinstance(cond_typ,AutoType)):
            cond_typ = BooleanType()
            infer(cond.name,IntegerType(),env)

        if  (not isinstance(cond,BooleanType)):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt,(True,typ,env))
    
    def visitDoWhileStmt(self, ast:DoWhileStmt, o): 
        (in_loop,typ,env) = o
        cond = self.visit(ast.cond,env)
        cond_typ = cond[0]

        if (isinstance(cond_typ,AutoType)):
            cond_typ = BooleanType()
            infer(cond.name,IntegerType(),env)

        if  (not isinstance(cond,BooleanType)):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt,(True,typ,env))
    
    def visitBreakStmt(self, ast:BreakStmt, o): 
        (in_loop,typ,env) = o
        if (in_loop == False):
            raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast, o):
        (in_loop,typ,env) = o
        if (in_loop == False):
            raise MustInLoop(ast)
    
    def visitReturnStmt(self, ast, o): 
        (in_loop,typ,env) = o
        if (ast.expr is None):
            if (not isinstance(typ,VoidType)):
                raise TypeMismatchInStatement(ast)
        else:
            expr = self.visit(ast.expr,env)
            if (not isinstance(expr,type(typ))):
                raise TypeMismatchInStatement(ast)
    
    def visitCallStmt(self, ast:CallStmt, o): 
        func = None
        for x in o:
            if (x.get(ast.name) is not None):
                if (isinstance(x[ast.name],dict)):
                    func = x[ast.name]
                    break
                else:
                    raise Undeclared(Function(),ast.name)
        if (func is None):
            raise Undeclared(Function(),ast.name)
        if (len(func["param"])!=len(ast.args)):
            raise TypeMismatchInStatement(ast)
        for i in range(0,len(func["param"])):
            param1 = func["param"][i]
            param2 = self.visit(ast.args[i],o)
            typ1 = param1.typ
            typ2 = param2[0]
            if (isinstance(typ1,AutoType)):
                func["param"][i].typ = typ2
                typ1 = typ2
            if (isinstance(typ2,AutoType)):
                infer(ast.args[i].name,typ1,o)
                typ2 = typ1
            if (self.check_type(typ1,typ2) == False):
                raise TypeMismatchInStatement(ast)


    def visitBinExpr(self, ast, o): 
        left = self.visit(ast.left,o)
        right = self.visit(ast.right,o)

        left_typ = left[0]
        right_typ = right[0]

        def check_type(accept_type,return_type=None):
            # if (isinstance(left,AutoType) and isinstance(right,AutoType)):
            #     raise TypeMismatchInExpression(ast)      
            nonlocal left_typ,right_typ,left,right

            if (isinstance(left_typ,AutoType)):
                left_typ = right_typ
                infer(ast.left.name,right_typ,o)
    
            if (isinstance(right_typ,AutoType)):
                right_typ = left_typ
                infer(ast.right.name,left_typ,o)

            if (not isinstance(left_typ,accept_type) or (not isinstance(right_typ,accept_type))):
                raise TypeMismatchInExpression(ast)
            if return_type:
                return return_type

            elif isinstance(left_typ,IntegerType) and isinstance(right_typ,FloatType):
                return right_typ

            elif isinstance(left_typ,FloatType) and isinstance(right_typ,IntegerType):
                return left_typ

            elif isinstance(left_typ, type(right_typ)):
                return left_typ

            else:
                raise TypeMismatchInExpression(ast)
        if (ast.op in ['+', '-', '*', '/']):
            return [check_type((IntegerType,FloatType)),None]
        elif (ast.op == '%'):
            return [check_type(IntegerType, IntegerType()),None]

        elif ast.op in ['!=', '==']:
            return [check_type((IntegerType, BooleanType), BooleanType()),None]

        elif ast.op in ['<', '<=', '>', '>=']:
            return [check_type((IntegerType, FloatType), BooleanType()),None]

        elif ast.op in ['&&', '||']:
            return [check_type(BooleanType, BooleanType()),None]

        elif ast.op == "::":
            return [check_type(StringType,StringType()),None]

    def visitUnExpr(self, ast, o):
        (init_type,env) = o
        if ast.op == '!':
            exp = self.visit(ast.body, (BooleanType(),env))
            if (isinstance(exp,AutoType)):
                exp = BooleanType()
                infer(ast.exp.val.name,BooleanType(),o)
            if isinstance(exp, BooleanType):
                return [exp,None]
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op == '-':
            exp = self.visit(ast.body, (init_type,env))
            if isinstance(exp, (IntegerType, FloatType)):
                return [exp,None]
            else:
                raise TypeMismatchInExpression(ast)
            
    def visitId(self, ast, o): 
        for x in o:
            if (x.get(ast.name) is not None):
                if (isinstance(x[ast.name],dict)):
                    raise Undeclared(Variable(),ast.name)
                return x[ast.name]
        raise Undeclared(Variable(),ast.name)

    def visitArrayLit(self, ast: ArrayLit, o): 
        valuelst = list(map(lambda x: self.visit(x,o),ast.explist))
        
        valuelst_typ = []
        for x in valuelst:
            valuelst_typ += [x[0]]

        if (isinstance(valuelst_typ[0],ArrayType)):
            first_ele = valuelst_typ[0]
            for x in valuelst_typ:
                if (x.dimensions!=first_ele.dimensions):
                    raise IllegalArrayLiteral(ast)
                if ((isinstance(x.typ,FloatType)) and (isinstance(first_ele.typ,IntegerType))):
                    first_ele.typ = FloatType()
                if ((self.check_type(first_ele.typ,x.typ) == False) or self.illegal_array_lit):
                    raise IllegalArrayLiteral(ast)
                
            return [ArrayType([len(valuelst)]+first_ele.dimensions,first_ele.typ),None]

        first_ele_type = valuelst_typ[0]
        for ele_type in valuelst_typ:
            if (isinstance(ele_type,AutoType)):
                continue
            if (isinstance(first_ele_type,AutoType)):
                first_ele_type = ele_type
            if ((isinstance(ele_type,FloatType)) and (isinstance(first_ele_type,IntegerType))):
                first_ele_type = FloatType()
            if (self.check_type(first_ele_type,ele_type) == False):
                self.illegal_array_lit = True
        for i in range(len(valuelst_typ)):
            if (isinstance(valuelst_typ[i],AutoType)):
                infer(ast.explist[i].name,first_ele_type,o)
        return [ArrayType([len(valuelst)],first_ele_type),None]

    def visitFuncCall(self, ast:FuncCall, o):
        func = None
        for x in o:
            
            if (x.get(ast.name) is not None):
                if (isinstance(x[ast.name],dict)):
                    func = x[ast.name]
                    break
                else:
                    raise Undeclared(Function(),ast.name)
        if (func is None):
            raise Undeclared(Function(),ast.name)
        if (len(func["param"])!=len(ast.args)):
            raise TypeMismatchInExpression(ast)
        for i in range(0,len(func["param"])):
            param1 = func["param"][i]
            param2 = self.visit(ast.args[i],o)
            typ1 = param1.typ
            typ2 = param2[0]
            if (isinstance(typ1,AutoType)):
                func["param"][i].typ = typ2
                typ1 = typ2
            if (isinstance(typ2,AutoType)):
                infer(ast.args[i].name,typ1,o)
                typ2 = typ1
            if (self.check_type(typ1,typ2) == False):
                raise TypeMismatchInExpression(ast)
        return [func["typ"],None]

    def visitArrayType(self, ast, o):
        return [ast,None]

    def visitArrayCell(self, ast:ArrayCell, o):
        arr = self.visit(Id(ast.name),o)
        count = len(ast.cell)
        arr_typ = arr[0]

        if (not isinstance(arr_typ,ArrayType)):
            raise TypeMismatchInExpression(ast)
        if (len(ast.cell)>len(arr_typ.dimensions)):
            raise TypeMismatchInExpression(ast)

        if (len(ast.cell)==len(arr_typ.dimensions)):
            arr = arr_typ.typ
        else:
            arr_typ.dimensions = arr_typ.dimensions[len(ast.cell):]
            arr = arr_typ
        
        for x in ast.cell:
            typ = self.visit(x,o)
            if (not isinstance(typ[0],IntegerType)):
                raise TypeMismatchInExpression(ast)
        print(arr)
        return [arr,None] 

    def visitIntegerLit(self, ast, o):
        return [IntegerType(),None]

    def visitFloatLit(self, ast, o):
        return [FloatType(),None]
    
    def visitBooleanLit(self, ast, o):
        return [BooleanType(),None]
    
    def visitStringLit(self, ast, o):
        return [StringType(),None]

    def visitIntegerType(self, ast, o):
        return [IntegerType(),None]
    
    def visitFloatType(self, ast, o):
        return [FloatType(),None]
    
    def visitStringType(self, ast, o):
        return [StringType(),None]

    def visitAutoType(self, ast, o):
        return [AutoType(),None]
    
    def visitVoidType(self, ast, o):
        return [VoidType(),None]    
