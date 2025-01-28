"""
Escribir un programa que pregunte al usuario su nombre, edad, 
dirección y teléfono y lo guarde en un diccionario. Después 
debe mostrar por pantalla el mensaje “<nombre> tiene <edad> 
años, vive en <dirección> y su número de teléfono es <teléfono>”.
"""

""" SINTAXIS
datos = dict([
      ('Nombre', input("Escribe Nombre")),
      ('Edad', input("Escribe edad")),
      ('Direccion', input("Escribe direccion")),
      ('Telefono', input("Introduce telefono"))
      ])
print(datos)
"""

""" SINTAXIS
datos = dict(
      Nombre = input("Escribe Nombre"),
      Edad = input("Escribe edad"),
      Direccion = input("Escribe direccion"),
      Telefono = input("Introduce telefono"))
print(datos)
"""


datos = {
"Nombre": input("Escribe Nombre: "),
"Edad": input("Escribe edad: "),
"Direccion": input("Escribe direccion: "),
"Telefono": input("Introduce telefono: ")
}
print(datos["Nombre"], "tiene", datos["Edad"], "años, vive en", 
      datos["Direccion"], "y su numero de telefono es:", datos["Telefono"])
