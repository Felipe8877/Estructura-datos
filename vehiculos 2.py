class Vehiculo:
    marca: str
    color:str
    modelo:int
    cilindraje: int
    numeroRuedas: int
    combustible: str
    tipo_Vehiculo: str 
    
    def __init__(self, marca:str, combustible:int, tipo_Vehiculo:str)-> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo_Vehiculo = tipo_Vehiculo

    def __str__(self)-> str:
        return f"la marca del vehiculo es: {self.marca} y el nivel de combustible es de: {self.combustible}, tipo de vehiculo: {self.tipo_Vehiculo}"
    
    def encender(self):
        if self.combustible < 10:
            print ("Cuidado, el nivel de gasolina es bajo")
        else: 
            print ("El vehiculo esta encendido")

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def apagar(self):
        pass


class Moto(Vehiculo):
    pass

class Carro(Vehiculo):
    pass

vehiculo1 = Vehiculo('mazda',9,'carro', )
print(vehiculo1)
vehiculo1.encender()

moto1 = Moto('honda',70,'moto', )
print(moto1)
moto1.encender()

carro1 = Carro('renaul',80, 'carro', )
print(carro1) 
carro1.encender()

