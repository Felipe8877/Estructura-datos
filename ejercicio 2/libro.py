class Libro:
    def __init__(self, titulo, autor, genero, año):  
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.año}")



libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)
libro.mostrar_detalles()