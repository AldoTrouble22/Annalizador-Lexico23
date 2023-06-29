from lexico import analizador_lexico

while True:
    try:
        codigo = input(">>>  ")
    except:
        print("\nAdios")
        break
    tokens = analizador_lexico(codigo)
    for token, valor in tokens:
        print(f'Token: {token}, Valor: {valor}')
