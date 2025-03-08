class Rectangulo:
    def __init__(self, base, altura):  
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)



base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))


rectangulo = Rectangulo(base, altura)
print("Área:", rectangulo.calcular_area())
print("Perímetro:", rectangulo.calcular_perimetro())9