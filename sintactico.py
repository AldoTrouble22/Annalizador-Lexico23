from lexico import analizador_lexico
from Interprete import codigo

def match(tokenEsperado):
    global listaTokens
    if listaTokens and listaTokens[0] == tokenEsperado:
        listaTokens = listaTokens[1:]
    else:
        print("Error de sintaxis")
       
def analizador_sintactico(codigo):
    global listaTokens
    listaTokens = analizador_lexico(codigo)
    resultado = program()
    if len(listaTokens) == 0:
        print("La cadena es válida")
    else:
        print("Error de sintaxis")

def program():
    return declaration()

def declaration():
    if listaTokens[0][0] == "CLASS":
        class_decl()
        declaration()
    elif listaTokens[0] == "FUNCTION":
        fun_decl()
        declaration()
    elif listaTokens[0] == "VAR":
        var_decl()
        declaration()
    elif listaTokens[0] == "IF" or listaTokens[0] == "para" or listaTokens[0] == "imprimir" or listaTokens[0] == "retornar" or listaTokens[0] == "mientras" or listaTokens[0] == "{":
        statement()
        declaration()
    else:
        return
    return declaration()

def class_decl():
    match("clase")
    match("id")
    class_inher()
    match("{")
    functions()
    match("}")

def class_inher():
    if listaTokens[0] == "<":
        match("<")
        match("id")

def fun_decl():
    match("fun")
    functio() #se cambio el nombre para evitar errores

def var_decl():
    match("var")
    match("id")
    var_init()
    match(";")

def var_init():
    if listaTokens[0] == "=":
        match("=")
        expression()

def statement():
    if listaTokens[0] == "si":
        if_stmt()
    elif listaTokens[0] == "para":
        for_stmt()
    elif listaTokens[0] == "imprimir":
        print_stmt()
    elif listaTokens[0] == "retornar":
        return_stmt()
    elif listaTokens[0] == "mientras":
        while_stmt()
    elif listaTokens[0] == "{":
        block()
    elif listaTokens[0] == "if" or listaTokens[0] == "for" or listaTokens[0] == "print" or listaTokens[0] == "return" or listaTokens[0] == "while" or listaTokens[0] == "{":
        expr_stmt()
    else:
        expr_stmt()

def expr_stmt():
    expression()
    match(";")

def for_stmt():
    match("for")
    match("(")
    for_stmt_1()
    for_stmt_2()
    for_stmt_3()
    match(")")
    statement()

def for_stmt_1():
    if listaTokens[0] == "var":
        var_decl()
    else:
        expr_stmt()

def for_stmt_2():
    if listaTokens[0] != ";":
        expression()
    match(";")

def for_stmt_3():
    if listaTokens[0] != ")":
        expression()


