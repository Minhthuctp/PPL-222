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
            if (x==env[-2]):
                if (not isinstance(x[id],AutoType)):
                    if (isinstance(x[id],dict)):
                        x[id]["typ"] = typ
                    env[-1][id]["typ"] = typ
                return
            else:
                if (isinstance(x[id],dict)):
                    x[id]["typ"] = typ
                else:
                    x[id] = typ
                return


class GetEnv(Visitor):

    def __init__(self,ast):
        self.ast = ast

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
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
        Symbol("super",MType([],VoidType())),
        Symbol("preventDefault",MType([],VoidType()))
    ]

    def change(self,o):
        for x in self.global_env:
            o[0][x.name] = {
                "typ": x.mtype.rettype,
                "param": [ParamDecl("",p,False,False) for p in x.mtype.param]
            }

    def __init__(self,ast):
        self.ast = ast
        self.is_return = False
        self.func = None
        self.illegal_array=False
        self.length = 0

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
    
    def find_func(self,func_name,o):
        for x in o:
            if (x.get(func_name) is not None):
                if (not isinstance(x[func_name],dict)):
                    if ((x == o[-2]) and (o[-1].get(func_name) is not None)):
                        return o[-1][func_name]
                    else:
                        return x[func_name]
                else:
                    return x[func_name]
        raise Undeclared(Function(),func_name)

    def visitProgram(self, ast:Program, o):
        find_main_func = False      
        o = GetEnv(ast).visit(ast,o)
        o = [{}] + o
        self.change(o)
        for x in ast.decls:
            if (isinstance(x,FuncDecl) and (x.name=="main") and (isinstance(x.return_type,VoidType)) and (len(x.params)==0) and (x.inherit is None)):
                find_main_func = True
            self.visit(x,o)
        if (find_main_func == False):
            raise NoEntryPoint()
                    
    def visitVarDecl(self, ast: VarDecl, o):
        if (o[0].get(ast.name) is not None):
            raise Redeclared(Variable(),ast.name)
        o[0][ast.name] = self.visit(ast.typ,o)
        typ = o[0][ast.name]
        if (ast.init is not None):
            init_typ = self.visit(ast.init,o)
            if (isinstance(typ,AutoType)):
                o[0][ast.name] = init_typ
                return
            if (isinstance(init_typ,AutoType)):
                init_typ = typ
                infer(ast.init.name,typ,o)
            if (self.check_type(typ,init_typ) == False):
                raise TypeMismatchInVarDecl(ast)            
        else:
            if (isinstance(o[0][ast.name],AutoType)):
                raise Invalid(Variable(), ast.name)    

    def visitParamDecl(self, ast:ParamDecl, o):
        if (o[0].get(ast.name) is not None):
            raise Redeclared(Parameter(),ast.name)
        o[0][ast.name] = ast.typ

    def check_first_stmt(self,stmt):
        if (not isinstance(stmt,CallStmt)):
            return True
        if (stmt.name!="super" and stmt.name!="preventDefault"):
            return True
        return False

    def visitFuncDecl(self, ast: FuncDecl, o):
        prototype = o[1].get(ast.name)
        if (o[0].get(ast.name)):
            raise Redeclared(Function(),ast.name)
        o[0][ast.name] = prototype
        env = [{}] + o
        for x in prototype["param"]:
            self.visit(x,env)    

        parent = None
        if (o[0][ast.name]["parent"] is not None):
            parent = o[0][ast.name]["parent"]
            if ((o[0].get(parent) is not None) and (isinstance(o[0][parent],dict))):
                parent = o[0][parent]
                for x in parent["param"]:
                    if (x.inherit == True):
                        if (env[0].get(x.name) is not None):
                            raise Invalid(Parameter(),x.name)
                        env[0][x.name] = x.typ
            elif (o[1].get(parent) is not None):
                parent = o[1][parent]
                inherit_lst = []
                for x in parent["param"]:
                    if (x.inherit == True):
                        if (x.name in inherit_lst):
                            raise Redeclared(Parameter(),x.name)
                        inherit_lst+=[x.name]
                for x in parent["param"]:
                    if (x.inherit == True):
                        if (env[0].get(x.name) is not None):
                            raise Invalid(Parameter(),x.name)
                        env[0][x.name] = x.typ
            else:
                raise Undeclared(Function(),parent)
        
        # env = [{}] + o

        # for x in o[0][ast.name]["param"]:
        #     env[0][x[0]] = x[1]
        self.is_return = False
        self.func = o[0][ast.name]
        check_first = False
        if (o[0][ast.name]["parent"] is not None):
            if ((len(ast.body.body)==0) or self.check_first_stmt(ast.body.body[0])):
                if (len(parent["param"])!=0):
                    raise InvalidStatementInFunction(ast.name)
            else:
                check_first = True
                stmt = ast.body.body[0]
                if (stmt.name == "super"):
                    if (len(parent["param"]) > len(stmt.args)):
                        raise TypeMismatchInExpression(None)
                    elif (len(parent["param"]) < len(stmt.args)):
                        raise TypeMismatchInExpression(stmt.args[len(parent["param"])])
                    for i in range(0,len(stmt.args)):
                        typ1 = parent["param"][i].typ
                        typ2 = self.visit(stmt.args[i],env)
                        if (isinstance(typ1,AutoType)):
                            parent["param"][i].typ = typ2
                            infer(parent["param"][i].name,typ2,env)
                            typ1 = typ2
                        if (isinstance(typ2,AutoType)):
                            infer(stmt.args[i].name,typ1,env)
                            typ2 = typ1
                        if (self.check_type(typ1,typ2) == False):
                            raise TypeMismatchInExpression(stmt.args[i])
                else:
                    if (len(stmt.args)!=0):
                        raise TypeMismatchInExpression(stmt.args[0])
        else:
            if (len(ast.body.body)!=0):
                if (isinstance((ast.body.body[0]),CallStmt)):
                    stmt = ast.body.body[0]
                    if ((stmt.name == "super") or (stmt.name == "preventDefault")):
                        raise InvalidStatementInFunction(ast.name)
        if (check_first == False):
            for x in ast.body.body:
                if (isinstance(x,VarDecl)):
                    self.visit(x,env)
                else:
                    self.visit(x,(False,prototype,env))
        else:
            for x in ast.body.body[1:]:
                if (isinstance(x,VarDecl)):
                    self.visit(x,env)
                else:
                    self.visit(x,(False,prototype,env))
        paramlst = []
        for x in o[0][ast.name]["param"]:
            x.typ = env[0].get(x.name)
            paramlst+=[x]

        o[0][ast.name]["param"] = paramlst

        if (parent is not None):
            param_parent = []
            for x in parent["param"]:
                if (x.inherit == True):
                    x.typ = env[0].get(x.name)
                param_parent+=[x]
            parent["param"] = param_parent

        self.func = None
        self.is_return = False
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
        (in_loop,func,env) = o
        lhs_typ = self.visit(ast.lhs,env)
        rhs_typ = self.visit(ast.rhs,env)

        if (isinstance(lhs_typ,ArrayType) or isinstance(rhs_typ,ArrayType)):
            raise TypeMismatchInStatement(ast)
        
        if (isinstance(lhs_typ,AutoType)):
            lhs_typ = rhs_typ
            infer(ast.lhs.name,rhs_typ,env)

        if (isinstance(rhs_typ,AutoType)):
            rhs_typ = lhs_typ
            infer(ast.rhs.name,lhs_typ,env)
        
        if (self.check_type(lhs_typ,rhs_typ)==False):
            raise TypeMismatchInStatement(ast)
        # elif (isinstance(lhs_typ,FloatType)):
        #     if (not isinstance(rhs_typ,(IntegerType,FloatType))):
        #         raise TypeMismatchInExpression(ast)
        
        # elif (not isinstance(lhs,type(rhs))):
        #     raise TypeMismatchInExpression(ast)
    
    def visitBlockStmt(self, ast: BlockStmt, o):
        (in_loop,func,env) = o
        inner = [{}] + env
        temp = self.is_return
        self.is_return = False
        for x in ast.body:
            if (isinstance(x,VarDecl)):
                self.visit(x,inner)
            else:
                self.visit(x,(in_loop,func,inner))
        self.is_return = temp
    
    def visitIfStmt(self, ast: IfStmt, o): 
        (in_loop,func,env) = o
        cond = self.visit(ast.cond,env)
        if (not isinstance(cond,BooleanType)):
            raise TypeMismatchInStatement(ast)
        temp = self.is_return
        self.is_return = False
        self.visit(ast.tstmt,(in_loop,func,env))
        self.is_return = temp

        temp = self.is_return
        self.is_return = False
        if (ast.fstmt is not None):
            self.visit(ast.fstmt,(in_loop,func,env))
        self.is_return = temp
    
    def visitForStmt(self, ast: ForStmt, o):
        (in_loop,func,env) = o
        id_typ = self.visit(ast.init.lhs,env)
        init_typ = self.visit(ast.init.rhs,env)

        if (isinstance(id_typ,AutoType)):
            id_typ = init_typ
            infer(ast.init.lhs.name,init_typ,env)
        
        if (isinstance(init_typ,AutoType)):
            init_typ = id_typ
            infer(ast.init.rhs.name,id_typ,env)

        if (self.check_type(id_typ,init_typ) == False):
            raise TypeMismatchInStatement(ast)

        cond_typ = self.visit(ast.cond,env)
        upd_typ = self.visit(ast.upd,env)
        
        if (isinstance(cond_typ,AutoType)):
            cond_typ = BooleanType()
            infer(ast.cond.name,IntegerType(),env)
        
        if (isinstance(upd_typ,AutoType)):
            upd_typ = BooleanType()
            infer(ast.upd.name,IntegerType(),env)

        if (not isinstance(id_typ,IntegerType)) or (not isinstance(init_typ,IntegerType) or (not isinstance(upd_typ,IntegerType)) or (not isinstance(cond_typ,BooleanType))):
            raise TypeMismatchInStatement(ast)

        temp = self.is_return
        self.is_return = False        
        self.visit(ast.stmt,(True,func,env))
        self.is_return = temp
    
    def visitWhileStmt(self, ast:WhileStmt, o): 
        (in_loop,func,env) = o
        cond_typ = self.visit(ast.cond,env)

        if (isinstance(cond_typ,AutoType)):
            cond_typ = BooleanType()
            infer(ast.cond.name,IntegerType(),env)

        if  (not isinstance(cond_typ,BooleanType)):
            raise TypeMismatchInStatement(ast)
        temp = self.is_return
        self.is_return = False 
        self.visit(ast.stmt,(True,func,env))
        self.is_return = temp
    
    def visitDoWhileStmt(self, ast:DoWhileStmt, o): 
        (in_loop,func,env) = o

        temp = self.is_return
        self.is_return = False 
        self.visit(ast.stmt,(True,func,env))
        self.is_return = temp

        cond_typ = self.visit(ast.cond,env)

        if (isinstance(cond_typ,AutoType)):
            cond_typ = BooleanType()
            infer(ast.cond.name,IntegerType(),env)

        if  (not isinstance(cond_typ,BooleanType)):
            raise TypeMismatchInStatement(ast)
        
    
    def visitBreakStmt(self, ast:BreakStmt, o): 
        (in_loop,func,env) = o
        if (in_loop == False):
            raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast, o):
        (in_loop,func,env) = o
        if (in_loop == False):
            raise MustInLoop(ast)
    
    def visitReturnStmt(self, ast, o): 
        (in_loop,func,env) = o
        if (self.is_return==True):
            return
        if (ast.expr is None):
            if (isinstance(func["typ"],AutoType)):
                func["typ"] = VoidType()
            elif (not isinstance(func["typ"],VoidType)):
                raise TypeMismatchInStatement(ast)
        else:
            expr_typ = self.visit(ast.expr,env)
            if (isinstance(func["typ"],AutoType)):
                func["typ"] = expr_typ
            if (isinstance(expr_typ,AutoType)):
                expr_typ = func["typ"]
                infer(ast.expr.name,func["typ"],env)
            elif (self.check_type(func["typ"],expr_typ) == False):
                raise TypeMismatchInStatement(ast)
        self.is_return = True

    def visitCallStmt(self, ast:CallStmt, o): 
        (in_loop,func,env) = o
        f = self.find_func(ast.name,env)
        if (not isinstance(f,dict)):
            raise TypeMismatchInStatement(ast)
        if (len(f["param"])!=len(ast.args)):
            raise TypeMismatchInStatement(ast)
        for i in range(0,min(len(f["param"]),len(ast.args))):
            typ1 = f["param"][i].typ
            typ2 = self.visit(ast.args[i],env)
            if (isinstance(typ1,AutoType)):
                f["param"][i].typ = typ2
                typ1 = typ2
            if (isinstance(typ2,AutoType)):
                infer(ast.args[i].name,typ1,env)
                typ2 = typ1
            if (self.check_type(typ1,typ2) == False):
                raise TypeMismatchInStatement(ast)
        
        if (ast.name == func["name"]):
            for x in func["param"]:
                env[-3][x.name] = x.typ

    def visitBinExpr(self, ast: BinExpr, o): 
        left_typ = self.visit(ast.left,o)
        right_typ = self.visit(ast.right,o)

        def check_type(accept_type,return_type=None):
            # if (isinstance(left,AutoType) and isinstance(right,AutoType)):
            #     raise TypeMismatchInExpression(ast)      
            nonlocal left_typ,right_typ

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
            return check_type((IntegerType,FloatType))
        elif (ast.op == '%'):
            return check_type(IntegerType, IntegerType())

        elif ast.op in ['!=', '==']:
            return check_type((IntegerType, BooleanType), BooleanType())

        elif ast.op in ['<', '<=', '>', '>=']:
            return check_type((IntegerType, FloatType), BooleanType())

        elif ast.op in ['&&', '||']:
            return check_type(BooleanType, BooleanType())

        elif ast.op == "::":
            return check_type(StringType,StringType())

    def visitUnExpr(self, ast:UnExpr, o):
        if ast.op == '!':
            exp = self.visit(ast.val, o)
            if (isinstance(exp,AutoType)):
                exp = BooleanType()
                infer(ast.val.name,BooleanType(),o)
            if isinstance(exp, BooleanType):
                return exp
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op == '-':
            exp = self.visit(ast.val, o)
            if isinstance(exp, (IntegerType, FloatType)):
                return exp
            else:
                raise TypeMismatchInExpression(ast)
            
    def visitId(self, ast, o): 
        for x in o:
            if (x.get(ast.name) is not None):
                if (isinstance(x[ast.name],dict)):
                    raise Undeclared(Identifier(),ast.name)
                return x[ast.name]
        raise Undeclared(Identifier(),ast.name)

    def visitArrayLit(self, ast: ArrayLit, o): 
        try:
            valuelst_typ = list(map(lambda x: self.visit(x,o),ast.explist))
        except IllegalArrayLiteral:
            raise IllegalArrayLiteral(ast)
        
        if (len(ast.explist) == 0):
            return ArrayType([0], None)
        if (isinstance(valuelst_typ[0],ArrayType)):
            first_ele = valuelst_typ[0]
            for x in valuelst_typ:
                if (x.dimensions!=first_ele.dimensions):
                    raise IllegalArrayLiteral(ast)
                if (not isinstance(first_ele.typ,type(x.typ))):
                    raise IllegalArrayLiteral(ast)
            return ArrayType([len(valuelst_typ)]+first_ele.dimensions,first_ele.typ)

        first_ele_type = valuelst_typ[0]
        for ele_type in valuelst_typ:
            if (isinstance(ele_type,AutoType)):
                continue
            if (isinstance(first_ele_type,AutoType)):
                first_ele_type = ele_type
            if (not isinstance(first_ele_type,type(ele_type))):
                raise IllegalArrayLiteral(ast)
        for i in range(len(valuelst_typ)):
            if (isinstance(valuelst_typ[i],AutoType)):
                infer(ast.explist[i].name,first_ele_type,o)
        return ArrayType([len(valuelst_typ)],first_ele_type)

    def visitFuncCall(self, ast:FuncCall, o):
        func = self.find_func(ast.name,o)
        if (not isinstance(func,dict)):
            raise TypeMismatchInExpression(ast)
        if (len(func["param"])!=len(ast.args)):
            raise TypeMismatchInExpression(ast)
        if (isinstance(func["typ"],VoidType)):
            raise TypeMismatchInExpression(ast)
        for i in range(0,min(len(func["param"]),len(ast.args))):
            typ1 = func["param"][i].typ
            typ2 = self.visit(ast.args[i],o)
            if (isinstance(typ1,AutoType)):
                func["param"][i].typ = typ2
                typ1 = typ2
            if (isinstance(typ2,AutoType)):
                infer(ast.args[i].name,typ1,o)
                typ2 = typ1
            if (self.check_type(typ1,typ2) == False):
                raise TypeMismatchInExpression(ast)
        if (self.func is not None):
            if (ast.name == self.func["name"]):
                for x in self.func["param"]:
                    o[-3][x.name] = x.typ
        return func["typ"]

    def visitArrayType(self, ast, o):
        return ast

    def visitArrayCell(self, ast:ArrayCell, o):
        arr_typ = self.visit(Id(ast.name),o)        
        if (not isinstance(arr_typ,ArrayType)):
            raise TypeMismatchInExpression(ast)
        if (len(ast.cell)>len(arr_typ.dimensions)):
            raise TypeMismatchInExpression(ast)

        if (len(ast.cell)==len(arr_typ.dimensions)):
            arr = arr_typ.typ
        else:
            arr = ArrayType(arr_typ.dimensions[len(ast.cell):],arr_typ.typ)
        for x in ast.cell:
            typ = self.visit(x,o)
            if (isinstance(typ,AutoType)):
                typ = IntegerType()
                infer(x.name,IntegerType(),o)
            if (not isinstance(typ,IntegerType)):
                raise TypeMismatchInExpression(x)
        return arr

    def visitIntegerLit(self, ast, o):
        return IntegerType()

    def visitFloatLit(self, ast, o):
        return FloatType()
    
    def visitBooleanLit(self, ast, o):
        return BooleanType()
    
    def visitStringLit(self, ast, o):
        return StringType()

    def visitIntegerType(self, ast, o):
        return IntegerType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitStringType(self, ast, o):
        return StringType()

    def visitAutoType(self, ast, o):
        return AutoType()
    
    def visitVoidType(self, ast, o):
        return VoidType()  

    def visitBooleanType(self, ast, o):
        return BooleanType()