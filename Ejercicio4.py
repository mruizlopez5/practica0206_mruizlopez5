"""
Escribir un programa que cree un diccionario vacío y lo vaya 
llenado con información sobre una persona (por ejemplo nombre, 
edad, sexo, teléfono, correo electrónico, etc.) que se le pida 
al usuario. Cada vez que se añada un nuevo dato debe imprimirse 
el contenido del diccionario.
"""

dic= {}
a = True
while a != False:

    categoria = input("Introduce la categoría (o enter vacio para terminar): ")
    if categoria == '':
        a = False

    else:
        valor = input(("Introduce el valor para "+categoria+": ") )
        dic[categoria] = valor
        
print(dic)