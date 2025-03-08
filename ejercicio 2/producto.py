class Producto:
    def __init__(self, nombre, precio, stock):  
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_total(self, cantidad):
        return self.precio * cantidad if cantidad <= self.stock else "Stock insuficiente"


producto = Producto("Moto MT", 2000000, 3)
cantidad_comprada = 3


print(f"Total por {cantidad_comprada} {producto.nombre}s: ${producto.calcular_total(cantidad_comprada)}")