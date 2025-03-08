class Electrodomestico:
    def _init_(self, marca, modelo, consumo):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo

    def encender(self):
        return f"{self.marca} {self.modelo} se ha encendido."

class Lavadora(Electrodomestico):
    def _init_(self, marca, modelo, consumo, capacidad):
        super()._init_(marca, modelo, consumo)
        self.capacidad = capacidad

    def encender(self):
        return f"La lavadora {self.marca} {self.modelo} ha iniciado su ciclo de lavado."

class Refrigerador(Electrodomestico):
    def _init_(self, marca, modelo, consumo, tiene_freezer):
        super()._init_(marca, modelo, consumo)
        self.tiene_freezer = tiene_freezer

    def encender(self):
        return f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura."

# Usando otras marcas
lavadora = Lavadora("LG", "WashMaster", "400W", "12kg")
refrigerador = Refrigerador("Samsung", "FrostFree", "280W", True)

print(lavadora.encender())
print(refrigerador.encender())