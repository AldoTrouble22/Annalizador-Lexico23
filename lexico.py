import re
from tokens import reservadas, operadores, simbolos, esp_tokens

def analizador_lexico(codigo):
    tokens = []
    posicion = 0

    while posicion < len(codigo):
        encontrado = False

        # Verificar si la cadena empieza con alguna palabra reservada
        for palabra, token in reservadas.items():
            if codigo[posicion:].split(maxsplit=1)[0] == palabra:
                tokens.append((token, palabra))
                posicion += len(palabra)+1
                encontrado = True
                break

        # Verificar si la cadena coincide con algún operador
        if not encontrado:
            for patron, token in operadores.items():
                coincidencia = re.match(patron, codigo[posicion:])
                if coincidencia:
                    valor = coincidencia.group()
                    tokens.append((token, valor))
                    posicion += len(valor)
                    encontrado = True
                    break

        # Verificar si la cadena coincide con algún símbolo
        if not encontrado:
            for patron, token in simbolos.items():
                coincidencia = re.match(patron, codigo[posicion:])
                if coincidencia:
                    valor = coincidencia.group()
                    tokens.append((token, valor))
                    posicion += len(valor)
                    encontrado = True
                    break

        # Verificar si la cadena coincide con algún token especial
        if not encontrado:
            for token, patron in esp_tokens:
                coincidencia = re.match(patron, codigo[posicion:])
                if coincidencia:
                    valor = coincidencia.group()
                    tokens.append((token, valor))
                    posicion += len(valor)
                    encontrado = True
                    break

        # Si no se encontró ningún token válido, se ignora el carácter actual
        if not encontrado:
            posicion += 1

    return tokens

#uso
"""codigo = input(">>>  ")
tokens = analizador_lexico(codigo)
for token, valor in tokens:
    print(f'Token: {token}, Valor: {valor}')

nombre_archivo = input("Ingresa el nombre del archivo: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        codigo = archivo.read()
        tokens = analizador_lexico(codigo)
        for token, valor in tokens:
            print(f'Token: {token}, Valor: {valor}')
except FileNotFoundError:
    print("¡El archivo no existe!")
except IOError:
    print("Ocurrió un error al leer el archivo.")"""
