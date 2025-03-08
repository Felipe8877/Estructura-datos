class Persona:
    def __init__(self, nombre, edad, genero):  # Constructor corregido
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


class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo=0.0):
        if not isinstance(titular, Persona):  # Verifica que el titular sea una instancia de Persona
            raise TypeError("El titular debe ser una instancia de la clase Persona.")
        self._titular = titular
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self._saldo:.2f}")
        elif cantidad > self._saldo:
            print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor a cero.")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self._saldo:.2f}")


# Ejemplo de uso
persona1 = Persona("Felipe", 18, "masculino")
persona1.presentarse()

cuenta1 = CuentaBancaria(persona1, "1234567890", 1000.0)
cuenta1.consultar_saldo()
cuenta1.depositar(500)
cuenta1.retirar(200)