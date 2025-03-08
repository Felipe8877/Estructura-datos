class FiguraGeometrica:
    def calcular_area(self):
        pass

class Triangulo(FiguraGeometrica):
    def _init_(self, base, altura):
        self.base, self.altura = base, altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def _init_(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

triangulo, cuadrado = Triangulo(10, 5), Cuadrado(4)

print(f"Área del triángulo: {triangulo.calcular_area()}")  
print(f"Área del cuadrado: {cuadrado.calcular_area()}")