"""
La instrucción else complementa la instrucción if.
La palabra clave elif es la abreviatura de "else if".
"""

x = 28

if x < 0:
    print('x < 0')
elif x == 0:
    print('x is zero')
elif x == 1:
    print('x == 1')
else:
    print('Ninguno fue True')

name = "John"

if name == 'John':
    print(True)
else:
    print(False)

n = 30

if n < 0:
    print('n < 0')
else:
    if n == 31:
        print (True)
    else:
        if 0<n<29:
            print("n esta entre 0 y 29")
        else:
            print('Ninguno fue True')


