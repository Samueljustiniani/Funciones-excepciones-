import math

def area_del_circulo(radio):
    return round(math.pi * radio ** 2, 2)

# Ejemplo de uso
radio = 5
area = area_del_circulo(radio)
print(f"El área de un círculo con radio {radio} es {area}")
