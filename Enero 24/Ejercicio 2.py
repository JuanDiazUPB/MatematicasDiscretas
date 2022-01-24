import math

primos = []  # Donde se almacenarán todos los números primos

for n in range(1000000000, 1000000101):
    raiz_entera = math.isqrt(n)  # Solo se considera la parte entera del resultado
    for i in range(2, raiz_entera):
        if n % i == 0:  # Tiene un divisor, no es primo y se continua al siguiente número
            break
    else:
        primos.append(n)  # Si no, es un primo y se añade a la lista

print(f'Se han encontrado {len(primos)} números primos entre mil millones y mil millones cien: \n{primos}')

# Adaptado de https://www.programiz.com/python-programming/examples/prime-number
