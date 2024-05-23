'''
animales.py: Programa que construye la clase animal y dos subclases: perro y gato. 
Muestra un ejemplo con los objetos firulais y michi. La clase animal tiene dos 
parámetros, nombre y edad; y un método haz_ruido. Las subclases tienen overriding
 en el método haz_ruido.

Uso:
    python animales.py

Argumentos:
    No ocupa argumentos
'''

class animal():
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    
    def haz_ruido(self):
       print("AAAAAAAAAAAAH") 

class perro(animal):
    def haz_ruido(self):
       print("GUAUUUU") 

class gato(animal):
    usa_arenero = True
    def haz_ruido(self):
       print("MIAUUU") 

firulais =  perro('Firulais',6)
michi = gato('Michi',3)

firulais.haz_ruido()
michi.haz_ruido()

print(firulais.__dict__)
print(michi.__dict__)
