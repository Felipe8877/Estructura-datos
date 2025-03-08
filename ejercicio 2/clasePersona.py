class Persona:
    def __init__(self, nombre, edad, genero): 
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
    
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    def get_genero(self):
        return self._genero

    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_edad(self, edad):
        self._edad = edad
    
    def set_genero(self, genero):
        self._genero = genero

    def presentarse(self):
        print(f"Hola, mi nombre es {self._nombre}, tengo {self._edad} años y soy {self._genero}.")


persona1 = Persona("felipe", 18, "masculino")
persona1.presentarse()

