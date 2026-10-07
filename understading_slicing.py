players = ["peter", "charly","mercado", "Fatima", "Renata"]
print("lista original:", players)

#slicing
print(players[3:5]) #charly, mercado 



#El slicing me permite obtener una sublista de elementos de la lista original.
#slice
#players = ["peter", "charly","mercado", "Fatima", "Renata"]

print("1:4", players[1:4]) #charly, mercado, Fatima
print(":3", players[:3]) #peter, charly, mercado
print("2:", players[2:]) #mercado, Fatima, Renata
print("[-3:]", players[-3:]) #mercado, Fatima, Renata

#players = ["peter", "charly","mercado", "Fatima", "Renata"]
#caso especial del slicing
print(players[1:10]) #["juan","iancarlo","lisandro"]
