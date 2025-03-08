class Estudiante:
    def __init__(self, nombre, edad, curso):  
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def determinar_estado(self):
        return "Aprobado" if self.calcular_promedio() > 3 else "aprobado"  
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Curso: {self.curso}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        print(f"Estado: {self.determinar_estado()}")


estudiante = Estudiante("Felipe", 18, "Física Mecánica")
estudiante.agregar_calificacion(4)
estudiante.agregar_calificacion(3)
estudiante.agregar_calificacion(2)
estudiante.mostrar_detalles()
