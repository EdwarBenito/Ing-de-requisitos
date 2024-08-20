a=float(input('ingrese el valor que desea verificar: '))
b=float(input('ingrese el segundo valor que desea verificar'))
if a > b:
    print(f'el valor de {a} es mayor que el de {b}')
elif a < b:
    print(f'el valor de {b} es mayor que el de {a}')
else:
    print(f'el valor {a} y {b} son iguales')