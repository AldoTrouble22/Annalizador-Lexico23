import re
import tokenize
import Token

reservadas = {
    "y": "Y",
    "clase": "CLASE",
    "falso": "FALSO",
    "parar": "PARAR",
    "funcion": "FUNCION",
    "si": "SI",
    "nulo": "NULO",
    "o": "O",
    "imprimir": "IMPRIMIR",
    "retornar": "RETORNAR",
    "super": "SUPER",
    "este": "ESTE",
    "verdadero": "VERDADERO",
    "variable": "VARIABLE",
    "mientras": "MIENTRAS"
}

operadores = {
    "+" : "SUMA",
    "-" : "RESTA",
    "*" : "PRODUCTO",
    "/" : "DIVISION",
    "!=" : "DIFERENTE_DE",
    "=" : "ASIGNACION",
    "==" : "IGUAL_A",
    "<=" : "MENOR_IGUAL_A",
    ">=" : "MAYOR_IGUAL_A",
    "<" : "MENOR_A",
    ">" : "MAYOR_A",
}


def obtenerCodigo(lineas_python):
    # Apertura y lectura del archivo txt
    codigo_python = open("textoIdentificar.txt", mode ="r") # Abrimos el txt
    for linea_actual in codigo_python:
        lineas_python.append(linea_actual.strip("\t, \n"))
        # De la linea leida, eliminamos las tabulaciones y los saltos de linea con la
        # funcion STRIP.
    codigo_python.close()
# Final de la funcion obtenerArchivo

def imprimirLineas(lineas):
    # Impresion de la lista con las lineas del archivo txt
    for linea_actual in lineas:
        print(linea_actual)
# Final de la funcion imprimirLineas

def identificarTokens(nombre_archivo,lista_tokens):
    with tokenize.open(nombre_archivo) as archivo:
        tokens = tokenize.generate_tokens(archivo.readline)
        for token in tokens:
            lista_tokens.append(token)
# Final de la funcion identificarTokens

def getTypeToken(lista_tokens):
    token = Token
    for token_actual in lista_tokens:
        print("El token es: ",token.tok_name[token_actual.exact_type], token_actual.string)
# Fin de la funcion getTypeToken

def tabulaciones(archivo_tokens, contador_indents):
    num_tabulaciones = contador_indents
    control = 0
    while control < num_tabulaciones:
        archivo_tokens.write("\t")
        control = control + 1
    """if(contador_indents > 0 and contador_dedents == 0):
        while control < contador_indents:
            archivo_tokens.write("\t")
            control = control + 1
    elif(contador_indents > 0 and contador_dedents > 0):
        while control < contador_indents - 1:
            archivo_tokens.write("\t")
            control = control + 1
    elif(contador_indents == 0 and contador_dedents > 0):
        while control < contador_indents - 1"""

def escribirArchivo(lista_tokens):
    archivo_tokens = open("Archivo_Tokens.txt", mode = "x")
    token = Token
    #contador_indents = 0
    #contador_dedents = 0
    for token_actual in lista_tokens:
        if(token.tok_name[token_actual.exact_type] == 'NAME'):
            if(token_actual.string in reservadas):
                archivo_tokens.write("<reservada>")
            else:
                archivo_tokens.write("<identificador>")
        elif(token.tok_name[token_actual.exact_type] == 'NEWLINE'):
            archivo_tokens.write("\n")
            #tabulaciones(archivo_tokens, contador_indents - 1)
        elif(token.tok_name[token_actual.exact_type] == 'INDENT'):
            archivo_tokens.write("<indent>")
            #archivo_tokens.write("\t")
            #contador_indents = contador_indents + 1 
            #tabulaciones(archivo_tokens, contador_indents)
        elif(token.tok_name[token_actual.exact_type] == 'OP'):
            if(token_actual.string in operadores): 
                archivo_tokens.write("<operador>")
            else:
                archivo_tokens.write(token_actual.string)
        elif(token.tok_name[token_actual.exact_type] == 'DEDENT'):
            archivo_tokens.write("<dedent>")
            #contador_indents = contador_indents - 1 
            #tabulaciones(archivo_tokens, contador_indents)
        elif(token.tok_name[token_actual.exact_type] == 'NL'):
            archivo_tokens.write("Linea Vacia\n")
        else:
            archivo_tokens.write("<" + token.tok_name[token_actual.exact_type] +">")
    archivo_tokens.close

# Main 
nombre_archivo = "textoIdentificar.txt"
#lineas_python = []
lista_tokens = []

identificarTokens(nombre_archivo,lista_tokens)
getTypeToken(lista_tokens)
escribirArchivo(lista_tokens)