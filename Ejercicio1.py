"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por 
una divisa y muestre su símbolo o un mensaje de aviso si la 
divisa no está en el diccionario."""

while True:
    dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    print(dic[input("introduce 'Euro', 'Dollar' o 'Yen': ").capitalize()])
