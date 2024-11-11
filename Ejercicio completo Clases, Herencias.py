class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
        print ("Se ha creado a {} y tiene {}".format(nombre, edad))

    def hablar (self, palabras):
        print (self.nombre, ":" , palabras)


class Deportista (Persona):
    def practicardeporte(self):
        print (self.nombre,"Voy a practicar")      

Persona1 = Persona("Alma", 26)
Persona1.hablar("Hola mi nombre es Alma")

Persona1 = Deportista ("Alma", 13)
Persona1.practicardeporte()

Persona2 = Persona ("Luis", 12)
Persona2.hablar("Hola mi nombre es Luis")