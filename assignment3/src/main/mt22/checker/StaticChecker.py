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
            x[id] = typ
            return

class GetEnv(Visitor):

    def visitProgram(self, ast, o):
        o = [{}]
        for x in ast.decls:
            if (isinstance(x,FuncDecl)):
                self.visit(x,o)
        return o
    
    # def visitVarDecl(self, ast, o):
    #     if (o[0].get(ast.name) is not None):
    #         raise Redeclared(Variable(),ast.name)
    #     o[0][ast.name] = self.visit(ast.typ,o)

    def visitFuncDecl(self, ast, o):
        if (o[0].get(ast.name) is not None):
            return
        paramlst = []
        inheritlst = []
        env = [{}] + o
        typ = ast.return_type
        for x in ast.params:
            param = self.visit(x,env)
            paramlst += param
            if (x.inherit == True):
                inheritlst += param
        o[0][ast.name] = {
            "name": ast.name,
            "typ" : typ,
            "parent": ast.inherit,
            "param": paramlst,
            "inherit": inheritlst,
        }
        
    def visitParamDecl(self, ast, o):
        if (o[0].get(ast.name)):
            raise Redeclared(Parameter(),ast.name) 
        typ = self.visit(ast.typ)
        return [ast.name,typ]

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
        if (isinstance(typ1,type(typ2))):
            return True
        return False

    
    def check(self):
        return self.visit(self.ast, {})

    # def check_first_stmt(self,current_func,o):
    #     if (current_func["inherit"] is not None):
    #         if (isinstance(current_func["first_stmt"],CallStmt)):
    #             if (current_func["first_stmt"].name == "super"):
    #                 if ((o[1].get(current_func["parent"]) is not None) and isinstance(o[1][current_func["parent"]],dict)):
    #                     parent_func = o[1][current_func["parent"]]
    #                     if (len(current_func["first_stmt"].args) == len(parent_func["inherit"])):
    #                         for i in range(len(parent_func["inherit"])):
    #                             typ1 = self.visit(current_func["first_stmt"][i],o)
    #                             typ2 = parent_func["inherit"][i][1]
    #                             if (isinstance(typ1,AutoType)):
    #                                 raise TypeMismatchInExpression(current_func["first_stmt"][i])
    #                             if (not isinstance(typ1,typ2)):
    #                                 raise TypeMismatchInExpression()
    #                         for i in range(len(parent_func["inherit"])):
    #                             if (o[0].get(parent_func["inherit"][i][0]) is not None):
    #                                 raise Redeclared(Parameter(),parent_func["inherit"][i][0])
    #                             o[0][parent_func["inherit"][i][0]] = parent_func["inherit"][i][1]
    #                     else:
    #                         TypeMismatchInExpression(current_func["first_stmt"])
    #                     self.check_first_stmt(parent_func,o)
    #                 else:
    #                     pass
    #             elif (current_func["first_stmt"].name == "preventDefault"):
    #                 return
    #             else:
    #                 raise InvalidStatementInFunction(current_func["name"])
    #         else:
    #             raise InvalidStatementInFunction(current_func["name"])
    #     else:
    #         raise InvalidStatementInFunction(current_func["name"])


    def visitProgram(self, ast:Program, o):
        
        find_main_func = False
        for x in ast.decls:
            if (isinstance(x,FuncDecl) and (isinstance(x.return_type,VoidType)) and (len(x.params)==0)):
                find_main_func = True
        # o = GetEnv().visit(ast,o)
        o = [{}]
        for x in ast.decls:
            self.visit(x,o)
        
        if (find_main_func == False):
            raise NoEntryPoint()
        return []
                    
    def visitVarDecl(self, ast: VarDecl, o):
        if (o[0].get(ast.name) is not None):
            raise Redeclared(Variable(),ast.name)
        o[0][ast.name] = self.visit(ast.typ,o)
        if (ast.init is not None):
            init_typ = self.visit(ast.init,(o[0][ast.name],o))
            if (isinstance(o[0][ast.name],AutoType)):
                o[0][ast.name] = init_typ
                return
            if (self.check_type(o[0][ast.name],init_typ) == False):
                raise TypeMismatchInExpression(ast.init)
            if (isinstance(init_typ,AutoType)):
                infer(ast.init.name,)
        else:
            if (isinstance(o[0][ast.name],AutoType)):
                raise Invalid(Variable(), ast.name)    

    def visitFuncDecl(self, ast: FuncDecl, o):
        env = [{}] + o
        for x in o[0][ast.name]["param"]:
            env[0][x[0]] = x[1]
        
        if (o[0][ast.name]["parent"] is not None):
            self.check_first_stmt(o[0][ast.name],env)
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
        
    def visitAssignStmt(self, ast: AssignStmt, o): 
        (in_loop,typ,env) = o
        lhs = self.visit(ast.lhs,(in_loop,typ,env))
        rhs = self.visit(ast.rhs,(in_loop,typ,(lhs,env)))

        if (isinstance(rhs,AutoType)):
            infer(ast.rhs.name,lhs,env)

        elif (isinstance(lhs,FloatType)):
            if (not isinstance(rhs,(IntegerType,FloatType))):
                raise TypeMismatchInExpression(ast)
        
        elif (not isinstance(lhs,type(rhs))):
            raise TypeMismatchInExpression(ast)
    
    def visitBlockStmt(self, ast: BlockStmt, o):
        (in_loop,typ,env) = o
        inner = [{}] + env
        for x in ast.body:
            if (isinstance(x,VarDecl)):
                if inner[0].get(x.name) is not None:
                    raise Redeclared(Variable(),x.name)
                inner[0][x.name] = self.visit(x.typ)
        
        for x in ast.body:
            if (isinstance(x,VarDecl)):
                self.visit(x,inner)
            else:
                self.visit(x,(in_loop,typ,inner))
    
    def visitIfStmt(self, ast: IfStmt, o): 
        (in_loop,typ,env) = o
        cond = self.visit(ast.cond,(None,env))

        if (isinstance(cond,BooleanType)):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.tstmt,(in_loop,typ,env))

        if (ast.fstmt is not None):
            self.visit(ast.fstmt,(in_loop,typ,env))
    
    def visitForStmt(self, ast: ForStmt, o):
        (in_loop,typ,env) = o
        init = self.visit(ast.init,env)
        cond = self.visit(ast.cond,(None,env))
        upd = self.visit(ast.upd,(None,env))

        if (not isinstance(init,IntegerType) or (not isinstance(upd,IntegerType)) or (not isinstance(cond,BooleanType))):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.stmt,(True,typ,env))

    
    def visitWhileStmt(self, ast:WhileStmt, o): 
        (in_loop,typ,env) = o
        cond = self.visit(ast.cond,env)
        if  (not isinstance(cond,BooleanType)):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt,(True,typ,env))
    
    def visitDoWhileStmt(self, ast:DoWhileStmt, o): 
        (in_loop,typ,env) = o
        cond = self.visit(ast.cond,env)
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
    
    def visitCallStmt(self, ast, o): pass


    def visitBinExpr(self, ast, o): 
        (init_typ,env) = o
        left = self.visit(ast.left,(init_typ,env))
        right = self.visit(ast.right,(init_typ,env))
        def check_type(accept_type,return_type=None):
            # if (isinstance(left,AutoType) and isinstance(right,AutoType)):
            #     raise TypeMismatchInExpression(ast)      
            nonlocal left,right
            if (isinstance(left,AutoType) and isinstance(right,AutoType)):
                left = init_typ
                right = init_typ
                infer(ast.left.name,init_typ,env)
                infer(ast.right.name,init_typ,env)

            if (isinstance(left,AutoType)):
                left = right
                infer(ast.left.name,right,env)
    
            if (right == AutoType()):
                right = left
                infer(ast.right.name,left,env)

            if (not isinstance(left,accept_type) or (not isinstance(right,accept_type))):
                raise TypeMismatchInExpression(ast)
            if return_type:
                return return_type

            elif isinstance(left,IntegerType) and isinstance(right,FloatType):
                return right

            elif isinstance(left,FloatType) and isinstance(right,IntegerType):
                return left

            elif isinstance(left, type(right)):
                return left

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

    def visitUnExpr(self, ast, o):
        (init_type,env) = o
        if ast.op == '!':
            exp = self.visit(ast.body, (BooleanType(),env))
            if (isinstance(exp,AutoType)):
                exp = BooleanType
                infer(ast.exp.val.name,BooleanType(),o)
            if isinstance(exp, BooleanType):
                return exp
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op == '-':
            exp = self.visit(ast.body, (init_type,env))
            if isinstance(exp, (IntegerType, FloatType)):
                return exp
            else:
                raise TypeMismatchInExpression(ast)
            
    def visitId(self, ast, o):
        for x in o:
            if (x.get(ast.name) is not None):
                if (isinstance(x[ast.name],dict)):
                    raise Undeclared(Variable(),ast.name)
                return x[ast.name]
        raise Undeclared(Variable(),ast.name)

    def visitArrayLit(self, ast, o): 
        (init_type,env) = o
        valuelst = list(map(lambda x: self.visit(x,(init_type,env)),ast.explist))
        
        if (isinstance(valuelst[0],ArrayType)):
            first_ele = valuelst[0]
            for x in valuelst:
                if (x.dimensions!=first_ele.dimensions):
                    raise IllegalArrayLiteral(ast)
                if ((isinstance(x.typ,FloatType)) and (isinstance(first_ele.typ,IntegerType))):
                    first_ele.typ = FloatType()
                if ((self.check_type(first_ele.typ,x.typ) == False) or self.illegal_array_lit):
                    raise IllegalArrayLiteral(ast)
                
            return ArrayType([len(valuelst)],first_ele)

        first_ele_type = valuelst[0]
        for ele_type in valuelst:
            if (isinstance(first_ele_type,AutoType)):
                first_ele_type = ele_type
            if ((isinstance(ele_type,FloatType)) and (isinstance(first_ele_type,IntegerType))):
                first_ele_type = FloatType()
            if (self.check_type(first_ele_type,ele_type) == False):
                print(ele_type,first_ele_type)
                self.illegal_array_lit = True
        return ArrayType([len(valuelst)],first_ele_type)

    def visitFuncCall(self, ast, o): pass

    def visitArrayType(self, ast, o):
        return ast

    def visitArrayCell(self, ast, o):
        (init_typ,env) = o
        arr = self.visit(Id(ast.name),env)
        count = len(ast.cell)

        if (not isinstance(arr,ArrayType)):
            raise TypeMismatchInExpression(ast)
        if (len(ast.cell)>len(arr.dimensions)):
            raise TypeMismatchInExpression(ast)

        if (len(ast.cell)==len(arr.dimensions)):
            arr = arr.typ
        else:
            arr.dimensions = arr.dimensions[len(ast.cell):]
        
        for x in ast.cell:
            typ = self.visit(x,env)
            if (not isinstance(typ,IntegerType)):
                raise TypeMismatchInExpression(ast)
        
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
