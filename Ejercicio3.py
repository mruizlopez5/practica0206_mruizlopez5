"""
Escribir un programa que guarde en un diccionario los precios 
de los artículos de la tabla, pregunte al usuario por un artículo, 
un número de unidades y muestre por pantalla el precio de esa 
cantidad de producto. Si el producto no está en el diccionario 
debe mostrar un mensaje informando de ello.
Pan: 1.40
Huevos: 2.30
Cebolla: 0.85
Aceite: 4.35
"""

datos={
'Pan': 1.40,
'Huevos': 2.30,
'Cebolla': 0.85,
'Aceite': 4.35
}
while True:
    prod = input("introduzca un producto (Pan, Huevos, Cebolla, Aceite): ").capitalize()
    if prod in datos:
        cant = int(input(("introduce numero de unidades de "+prod+": ")))
        print(cant,"unidades de",prod,"Son:",round((datos[prod]*cant),2))
    else:
        print("Ese producto no se encuentra en la lista, pruebe otra vez")


