print('bienvenido al programa de calculo de pagos segun mtrs cubicos consumidos de conagua')
anchura = float(input("ponga la anchura de la alberca en mts: "))
largo_triangulo  = float(input("ponga el largo del triangulo en mts: "))
largo_rectangulo = float(input("ponga el largo del rectangulo en mts: "))
profundidad = float(input('ponga la profundidad de la alberca en mtrs: '))
area_triangulo = anchura * largo_triangulo / 2
area_rectangulo = anchura * largo_rectangulo
volumen_alberca = (area_rectangulo * profundidad) + (area_triangulo * profundidad)
print(f'el volumen de la alberca es{volumen_alberca}')