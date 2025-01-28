"""
Escribir un programa que cree un diccionario de traducción 
español-inglés. El usuario introducirá las palabras en español 
e inglés separadas por dos puntos, y cada par <palabra>:<traducción> 
separados por comas, hasta que el usuario introduzca la palabra 
“terminar”. El programa debe crear un diccionario con las palabras 
y sus traducciones. Después pedirá una frase en español y utilizará 
l diccionario para traducirla palabra a palabra. Si una palabra 
no está en el diccionario debe dejarla sin traducir.
"""



while True:
    fragmento = input("intorduce palabras en español e inglés separadas por dos puntos, y cada par separados por comas (escriba terminar para terminar)\n").replace(" ","").split(",")
    dic={}
    a = True
    
    cont=0
    while a == True:
        
        
        if cont >= len(fragmento) or fragmento[cont] == "Terminar" or fragmento[cont] == "terminar" :
            a = False
            
        else:
            segundo = fragmento[cont].split(":")
            dic[segundo[0]]=segundo[1]
         
        cont+=1
    b = True
    while b == True:
        pala = input("introduce una palabra del diccionario ene español para conocer su traduccion al ingles(enter vacio para reiniciar el programa)")

        if pala == "":
            b = False
        elif pala in dic:
            print(dic[pala])
        else:
            print("introduzca entrada valida")