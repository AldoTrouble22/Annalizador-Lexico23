from scanner import analizador_lexico

codigo = input(">>>  ")
tokens = analizador_lexico(codigo)
for token, valor in tokens:
    print(f'Token: {token}, Valor: {valor}')