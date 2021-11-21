print("Quién eres?")
name = input("Nombre: ")
print(f"Hola, {name}")
n = int(input("Escribe un número: "))
if n > 0:
    print("Ese número es positivo")
if n < 0:
    print("Ese número es negativo")
if n == 0:
    print("Ese número es cero")
#Randomización y listas
input("Enter para continuar")

names = ["Harry", "Ron", "Hermione"]

names.append("Draco")

names.sort()

print(names)

input("Presione cualquier tecla para continuar")

for name in names:
    print(name)
input("Presione cualquier tecla para continuar")
for character in name:
    print(character)
input("Presione cualquier tecla para continuar")

houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

houses["Hermione"] = "Gryffindor"

print(houses["Hermione"])

input("Presione cualquier tecla para continuar")
# Matemática

def square(x):
    return x*x

for i in range(51):
    print(f"El cuadrado de {i} es {square(i)} ")

# No se?

input("Presione cualquier tecla para continuar")

class Point():
    def __init__(self, alto, ancho):
        self.x = ancho
        self.y = alto

p = Point(2, 8)
print(p.x)
print(p.y)

input("Presione cualquier tecla para continuar")

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Draco"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")