def convertir_base(numero10, base):
    lista_restantes = []
    digitos_base = []

    while numero10 > 0:  # El ciclo se detendra cuando el cociente sea 0
        restante = numero10 % base
        lista_restantes.append(restante)  # El restante se almacena en la lista
        numero10 = numero10 // base  # Se divide el número y pasa a tomar el valor del cociente

    while lista_restantes:
        digitos_base.append(str(lista_restantes.pop()))
        # Los dígitos en la lista de restantes se sacan desde el último al primero, y se construye el nuevo número en
        # una lista

    return ''.join(digitos_base)  # Los dígitos en la lista se unen en una sola cadena de texto.


print('NOTA: Las bases deben ser menores que 10\n')
elegir_base = int(input('Qué desea hacer?\n1. Base 10 a cualquier base\n2. Cualquier base a base 10\n'))
if elegir_base == 1:
    n10 = int(input('Qué número desea convertir?: '))
    b = int(input('A qué base desea convertirlo?: '))
    print(f'{n10} en base {b}:', convertir_base(n10, b))  # Se ejecuta la función anterior

elif elegir_base == 2:
    nx = str(input('Qué número desea convertir?: '))
    bx = int(input('En qué base esta el número?: '))
    print('Resultado en base 10:', int(nx, base=bx))
    # Se usa un parametro nativo de la función int() llamado "base", que permite convertir una string en cualquier base
    # a base 10

# Adaptados de https://bradfieldcs.com/algos/stacks/converting-number-bases/
# https://thecodingbot.com/convert-an-octal-numberbase-8-to-its-decimalbase-10-representation-in-python/
