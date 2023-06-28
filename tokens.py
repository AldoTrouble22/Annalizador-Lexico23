import re
reservadas = {
    'y' : 'AND',
    'clase' : 'CLASS',
    'ademas' : 'ELSE',
    'falso' : 'FALSE',
    'para' : 'FOR',
    'fun' : 'FUNCTION',
    'si' : 'IF',
    'nulo' : 'NULL',
    'o' : 'OR',
    'imprimir' : 'PRINT',
    'retornar' : 'RETURN',
    'super' : 'SUPER',
    'este' : 'THIS',
    'verdadero' : 'TRUE',
    'var' : 'VAR',
    'mientras' : 'WHILE'
    } 

operadores = {
    r'\+': 'SUMA',
    r'-': 'RESTA',
    r'\*': 'MULTIP',
    r'/': 'DIVISION',
    r'!': 'NEGACION',
    #r'!=': 'DIFERENTE',
    r'=': 'ASIGNACION',
    #r'==': 'IGUAL_A',
    r'<': 'MENOR_QUE',
    #r'<=': 'MENOR_IGUAL',
    r'>': 'MAYOR_QUE',
    #r'>=': 'MAYOR_IGUAL'
    }

simbolos = {
    #COMENTARIO
    #EOF 
    r'\(' : 'PARENTESIS_IZQ',
    r'\)' : 'PARENTESIS_DER',
    r'\[' : 'CORCHETE_IZQ',
    r'\]' : 'CORCHETE_DER',
    r'\{' : 'LLAVE_IZQ',
    r'\}' : 'LLAVE_DER',
    r',' : 'COMA',
    r'\.' : 'PUNTO',
    r';' : 'PUNTO_COMA'
}

esp_tokens = [
    ('NUMERO',  r'\d+(\.\d*)?'),         # Números enteros o decimales
    ('CADENA',  r'\".*?\"'),             # Cadenas de texto entre comillas dobles
    ('IDENTIFICADOR',r'[a-zA-Z_][a-zA-Z0-9_]*'),# Identificadores
    #('COMENTARIO_SIMPLE', r'\/\/.*'),     # Comentarios simples con // al inicio de la línea
    #('COMENTARIO_MULTILINEA', r'\/\*.*?\*\/')   # Comentarios de varias líneas entre /* y */
]





   