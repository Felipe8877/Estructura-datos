class Empleado:
    def _init_(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        return f"{self.nombre} trabaja en {self.departamento}."

class Gerente(Empleado):
    def _init_(self, nombre, salario, departamento, equipo=None):
        super()._init_(nombre, salario, departamento)
        self.equipo = equipo if equipo else []
    
    def trabajar(self):
        return f"{self.nombre} supervisa a {len(self.equipo)} empleados."

class Desarrollador(Empleado):
    def _init_(self, nombre, salario, departamento, lenguaje):
        super()._init_(nombre, salario, departamento)
        self.lenguaje = lenguaje
    
    def trabajar(self):
        return f"{self.nombre} programa en {self.lenguaje}."
    

Mario= Desarrollador("Mario", 50000, "TI", "Python")
maria = Desarrollador("Maria", 55000, "TI", "Java")
carlos = Gerente("Carlos", 70000, "TI", [andres, maria])

print(Mario.trabajar())  
print(maria.trabajar())  
print(carlos.trabajar())