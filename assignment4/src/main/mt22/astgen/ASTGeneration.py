from functools import reduce
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decl+ EOF
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(reduce(lambda pre,curr: pre + self.visit(curr), ctx.decl(),[]))

    # decl: vardecl | funcdecl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if (ctx.vardecl()):
            return self.visit(ctx.getChild(0))
        return [self.visit(ctx.getChild(0))]

    #vardecl: vardecl_ | vardeclass;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visit(ctx.getChild(0))

    # vardecl_: ID idlist* COLON typ SEMI;
    def visitVardecl_(self, ctx: MT22Parser.Vardecl_Context):
        namelst = [] 
        ans = []
        namelst += [ctx.ID().getText()]
        for x in ctx.idlist():
            namelst += [self.visit(x)]
        vartype = self.visit(ctx.typ())
        for x in namelst:
            ans += [VarDecl(x,vartype,None)]
        
        return ans
        
    #vardeclass: ID varlist exp SEMI;
    #varlist: COMMA ID varlist exp COMMA | COLON typ ASSIGN;
    def visitVardeclass(self, ctx: MT22Parser.VardeclassContext):
        namelst = []
        explst = []
        ans = []

        namelst += [ctx.ID().getText()]
        explst += [self.visit(ctx.exp())]

        ctx = ctx.varlist()
        while ctx.typ() is None:
            namelst += [ctx.ID().getText()]
            explst += [self.visit(ctx.exp())]
            ctx = ctx.varlist()
        typ = self.visit(ctx.typ())
        explst = explst[::-1]
        for i, x in enumerate(namelst):
            ans += [VarDecl(x,typ,explst[i])]
        
        return ans
        
    
    #automic: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAutomic(self, ctx: MT22Parser.AutomicContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BooleanType()
        return StringType()

    #typ: automic | arrtype | Auto;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.automic():
            return self.visit(ctx.automic())
        if ctx.arrtype():
            return self.visit(ctx.arrtype())
        return AutoType()

    # idlist: COMMA ID;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        return ctx.ID().getText()
    
    # arrtype: Array LS INTLIT (COMMA INTLIT)* RS Of automic;
    def visitArrtype(self, ctx: MT22Parser.ArrtypeContext):
        dimen = []

        for x in ctx.INTLIT():
            dimen += [int(x.getText())]
        
        typ = self.visit(ctx.automic())
        return ArrayType(dimen,typ)

    #funcdecl: ID COLON Function (typ | Void) LB paramlist? RB (Inherit ID)? blockstate;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        namefunc = ctx.ID(0).getText()
        if (ctx.typ()):
            functype = self.visit(ctx.typ())
        else:
            functype = VoidType()
        paramlst = []
        if (ctx.paramlist()):
            paramlst += self.visit(ctx.paramlist())
        
        if (ctx.Inherit()):
            parentfunc = ctx.ID(1).getText()
        else:
            parentfunc = None
        
        body = self.visit(ctx.blockstate())

        return FuncDecl(namefunc,functype,paramlst,parentfunc,body)
    
    # paramlist: paramdecl (COMMA paramdecl)*;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        ans = []
        for x in ctx.paramdecl():
            ans += [self.visit(x)]
        return ans
    
    #paramdecl: Inherit? Out? ID COLON typ;
    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        namepara = ctx.ID().getText()
        if (ctx.Inherit()):
            inherit = True
        else:
            inherit = False
        if (ctx.Out()):
            out = True
        else:
            out = False
        paratype = self.visit(ctx.typ())

        return ParamDecl(namepara,paratype,out,inherit)

    # blockstate: LP blockstmt? RP;
    def visitBlockstate(self, ctx: MT22Parser.BlockstateContext):
        if (ctx.blockstmt()):
            return self.visit(ctx.blockstmt())
        return BlockStmt([])
    
    #stmt: assignstmt | ifstmt | forstmt | whiledostmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt | blockstate;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    #assignstmt: assign_cont SEMI;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return self.visit(ctx.assign_cont())
    
    #assign_cont: assign_lhs ASSIGN exp;
    def visitAssign_cont(self, ctx: MT22Parser.Assign_contContext):
       ass_lhs = self.visit(ctx.assign_lhs())
       ass_rhs = self.visit(ctx.exp())
       return AssignStmt(ass_lhs,ass_rhs) 

    #assign_lhs: scalar_var;
    def visitAssign_lhs(self, ctx: MT22Parser.Assign_lhsContext):
        return self.visit(ctx.scalar_var())
    
    #scalar_var: ID | elem_exp | LB (ID | elem_exp) RB;
    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        return self.visit(ctx.elem_exp())
    
    #ifstmt: If LB exp RB stmt (Else stmt)?;
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        cond = self.visit(ctx.exp())
        tstmt = self.visit(ctx.stmt(0))
        if (ctx.Else()):
            fstmt = self.visit(ctx.stmt(1))
        else:
            fstmt = None
        return IfStmt(cond,tstmt,fstmt)
    
    #forstmt: For LB assign_cont COMMA exp COMMA exp RB stmt;  
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        assign_cont = self.visit(ctx.assign_cont())
        cond = self.visit(ctx.exp(0))
        upd = self.visit(ctx.exp(1))
        stmt = self.visit(ctx.stmt())
        return ForStmt(assign_cont,cond,upd,stmt)
    
    #whiledostmt: While LB exp RB stmt;
    def visitWhiledostmt(self, ctx: MT22Parser.WhiledostmtContext):
        cond = self.visit(ctx.exp())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond,stmt)

    # dowhilestmt: Do blockstate While LB exp RB SEMI;
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        cond = self.visit(ctx.exp())
        stmt = self.visit(ctx.blockstate())
        return DoWhileStmt(cond,stmt)
    
    #breakstmt: Break SEMI;
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()
    
    #continuestmt: Continue SEMI;
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()
    
    #returnstmt: Return exp? SEMI;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        if (ctx.exp()):
            return ReturnStmt(self.visit(ctx.exp()))
        return ReturnStmt(None)

    #callstmt: func_call SEMI;
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        ctx = ctx.func_call()
        namefunc = ctx.ID().getText()
        args=[]
        if (ctx.explist()):
            args = self.visit(ctx.explist())
        return CallStmt(namefunc,args)

    #statement: stmt | vardecl;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if (ctx.stmt()):
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.vardecl())

    #blockstmt: statement+;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        ans = []
        for x in ctx.statement():
            ans+= self.visit(x)
        return BlockStmt(ans)

    # literal: INTLIT | FLOATLIT | BOOLIT | STRLIT | arraylit;
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if (ctx.INTLIT()):
            return IntegerLit(int(ctx.INTLIT().getText()))
        if (ctx.FLOATLIT()):
            return FloatLit(float("0"+ctx.FLOATLIT().getText()))
        if (ctx.BOOLIT()):
            return BooleanLit(ctx.BOOLIT().getText() == 'true')
        if (ctx.STRLIT()):
            return StringLit(ctx.STRLIT().getText())
        return self.visit(ctx.arraylit())

    #explist: exp (COMMA exp)*;
    def visitExplist(self, ctx: MT22Parser.ExplistContext):
        ans = []
        for x in ctx.exp():
            ans += [self.visit(x)]
        return ans

    #arraylit: LP explist? RP;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        if (ctx.explist()):
            return ArrayLit(self.visit(ctx.explist()))
        return ArrayLit([])

    # elem_exp: ID LS explist RS;
    def visitElem_exp(self, ctx: MT22Parser.Elem_expContext):
        IDname = ctx.ID().getText()
        idx = self.visit(ctx.explist())
        return ArrayCell(IDname,idx)
    
    #func_call: ID LB explist? RB;
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        namefunc = ctx.ID().getText()
        args=[]
        if (ctx.explist()):
            args = self.visit(ctx.explist())
        return FuncCall(namefunc,args)
    
    #operands: literal | ID;
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if (ctx.literal()):
            return self.visit(ctx.literal())
        return Id(ctx.ID().getText())
    
    #exp: exp1 STRCONCAT exp1 | exp1;
    def visitExp(self, ctx: MT22Parser.ExpContext):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp1(0))
        op = ctx.getChild(1).getText()
        lhs = self.visit(ctx.exp1(0))
        rhs = self.visit(ctx.exp1(1))
        return BinExpr(op,lhs,rhs)
    
    #exp1: exp2 (EQUAL | NOTEQUAL | SMALLER | SMALLEREQUAL | GREATER | GREATEREQUAL) exp2 | exp2;
    def visitExp1(self, ctx: MT22Parser.Exp1Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp2(0))
        op = ctx.getChild(1).getText()
        lhs = self.visit(ctx.exp2(0))
        rhs = self.visit(ctx.exp2(1))
        return BinExpr(op,lhs,rhs)
    
    #exp2: exp2 (LOGICALAND | LOGICALOR) exp3 | exp3;
    def visitExp2(self, ctx: MT22Parser.Exp2Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp3())
        op = ctx.getChild(1).getText()
        lhs = self.visit(ctx.exp2())
        rhs = self.visit(ctx.exp3())
        return BinExpr(op,lhs,rhs)
    
    #exp3: exp3 (ADDOP | SUBSTROP) exp4 | exp4;
    def visitExp3(self, ctx: MT22Parser.Exp3Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp4())
        op = ctx.getChild(1).getText()
        lhs = self.visit(ctx.exp3())
        rhs = self.visit(ctx.exp4())
        return BinExpr(op,lhs,rhs)
    
    #exp4: exp4 (MULOP | DIVOP | MODOP) exp5 | exp5;
    def visitExp4(self, ctx: MT22Parser.Exp4Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp5())
        op = ctx.getChild(1).getText()
        lhs = self.visit(ctx.exp4())
        rhs = self.visit(ctx.exp5())
        return BinExpr(op,lhs,rhs)
    
    #exp5: LOGICALNOT exp5 | exp6;
    def visitExp5(self, ctx: MT22Parser.Exp5Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp6())
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.exp5())
        return UnExpr(op,val)
    
    #exp6: SUBSTROP exp6| exp7;
    def visitExp6(self, ctx: MT22Parser.Exp6Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.exp7())
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.exp6())
        return UnExpr(op,val)
    
    #exp7: func_call | elem_exp | operands | LB exp RB;
    def visitExp7(self, ctx: MT22Parser.Exp7Context):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.exp())