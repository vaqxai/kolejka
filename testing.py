from main import *

k = Kolejka()

zadania1 = KolejkasNode("Praca Domowa", 10)
zadania2 = KolejkasNode("Kupno biletów na wycieczke", 8)
zadania3 = KolejkasNode("Wycieczka Szkolna", 10)
zadania4 = KolejkasNode("Wizyta u rodziny", 5)
zadania5 = KolejkasNode("Wizyta u koleżanki", 5)

lista = []

lista.append(zadania1)
lista.append(zadania2)
lista.append(zadania3)
lista.append(zadania4)
lista.append(zadania5)

lista.sort(key=priority_key, reverse=True)

for i in lista:
    print(i.to_string())
