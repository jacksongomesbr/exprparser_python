from ExprListener import *
from ExprParser import ExprParser

class ConcreteExprListener(ExprListener):
    """
    Esta classe implementa o :class:`ExprListener` fornecendo funcionalidades
    para processamento da entrada do parser
    """

    def __init__(self, *args, **kwargs):
        self.values = []

    def enterProg(self, ctx: ExprParser.ProgContext):
        ctx.values = []

    def exitProg(self, ctx: ExprParser.ProgContext):
        self.values = ctx.values

    def enterExpr(self, ctx: ExprParser.ExprContext):
        """Se o não-terminal `ctx` tiver um `INT`, então
        o valor do nó é o valor inteiro do `INT`. Caso contrário,
        o valor é `None`
        
        Arguments:
            ctx {ExprParser.ExprContext} -- o contexto do nó
        """    
        if (ctx.INT() is not None):
            ctx.value = int(ctx.INT().getText())
        else:
            ctx.value = None

    def exitExpr(self, ctx: ExprParser.ExprContext):
        """Este método obtém as informações dos nós filhos e seus valores.
        Calcula o valor do nó conforme o operador e os operandos.
        
        Arguments:
            ctx {ExprParser.ExprContext} -- o contexto do nó
        """        
        if (ctx.value is None):
            if (ctx.children and len(ctx.children) == 3):
                left = ctx.children[0]
                right = ctx.children[2]
                valor = None
                op = ctx.children[1].getText()
                operando1 = left.value
                operando2 = right.value
                if (op == '*'):
                    valor = operando1 * operando2
                elif (op == '/'):
                    valor = operando1 / operando2
                elif (op == '+'):
                    valor = operando1 + operando2
                else:
                    valor = operando1 - operando2
                ctx.value = valor
        if (ctx.value is not None and isinstance(ctx.parentCtx, ExprParser.ProgContext)):
            ctx.parentCtx.values.append({
                'expr': ctx.getText(),
                'value': ctx.value
            })
