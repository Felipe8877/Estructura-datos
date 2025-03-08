class Usuario:
    def _init_(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave

    def iniciar(self, usuario, clave):
        return self.nombre == usuario and self.clave == clave

    def cambiar_clave(self, nueva_clave):
        self.clave = nueva_clave
        return "Clave actualizada correctamente."

class Admin(Usuario):
    def gestionar(self):
        return f"{self.nombre} está administrando el sistema."

class Cliente(Usuario):
    def comprar(self):
        return f"{self.nombre} ha realizado una compra."

# Instanciación de objetos con otros datos
admin = Admin("admin1", "adminClave")
cliente = Cliente("cliente1", "clienteClave")

print(admin.iniciar("admin1", "adminClave"))
print(cliente.iniciar("cliente1", "claveErronea"))
print(admin.gestionar())
print(cliente.comprar())
print(cliente.cambiar_clave("nuevaClaveCliente"))