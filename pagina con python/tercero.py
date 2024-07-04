import math

def volumen_del_cilindro(radio, altura):
    return round(math.pi * radio ** 2 * altura, 2)

# Ejemplo de uso
radio = 3
altura = 7
volumen = volumen_del_cilindro(radio, altura)
print(f"El volumen de un cilindro con radio {radio} y altura {altura} es {volumen}")
