"""
Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. 
Los alumnos y alumnas se guardarán en una lista que almacena un diccionario para cada alumno/a 
en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos 
del alumno/a (nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor 
True si ha aprobado el módulo. El programa debe preguntar al usuario por una opción del siguiente menú:

(1) Añadir alumno/a, 
(2) Eliminar alumno/a, 
(3) Mostrar alumno/a, 
(4) Listar todo el alumnado, 
(5) Listar alumnado aprobado, 
(6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
Preguntar por el NIF del alumno/a y mostrar sus datos.
Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
Terminar el programa.
"""

while True:
    z=True
    alumnos={}
    aprobados={}
    def añadir_alumno():
        x = input("introduce nif de alumno: ")
        nif=x
        x = {"nombre": input("introduce nombre: ").capitalize(),
                "apellidos": input("intorduce apellidos: ").capitalize(),
                "telefono": input("introduce telefono: "),
                "correo": input("introduce correo: "),
                "aprobado": input("introduce aprobado: 'si' o 'no': ").lower()}
    
        if x["aprobado"] == "si" or x["apellidos"] == "sí":
            x["aprobado"]=True
        else:
            x["aprobado"]=False  

        alumnos[nif] = x
        print("Alumno Añadido a la base\n")
        return
        
    def eliminar_alumno():
        del alumnos[input("introduce nif del alumno a eliminar: ")]
        print("Alumno eliminado\n")
        return

    def mostrar_alumno():
        print(alumnos[input("introduce nif del alumno a mostrar: ")])
        print()
        return

    def listado_alumnado():
        print(alumnos,"\n")
        return

    def listado_aprobado():
        for payo in alumnos:
            if alumnos[payo]["aprobado"] == True:
                aprobados[payo]=alumnos[payo]
        print(aprobados,"\n")
        
        
        print()
    while z == True:
        seleccion = input("""introduzca una opcion:
            1 Añadir alumno/a. 
            2 Eliminar alumno/a. 
            3 Mostrar alumno/a. 
            4 Listar todo el alumnado. 
            5 Listar alumnado aprobado. 
            6 Terminar. (reiniciar)\n""")

        if seleccion == "":
            ""
        elif int(seleccion) == 1:
            añadir_alumno()
        elif int(seleccion) == 2:
            eliminar_alumno()
        elif int(seleccion) == 3:
            mostrar_alumno()
        elif int(seleccion) == 4:
            listado_alumnado()
        elif int(seleccion) == 5:
            listado_aprobado()
        elif int(seleccion) == 6:
            z=False
        else:
            ""


