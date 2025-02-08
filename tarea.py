temperatura = []
for n in range(0,5):
    t = int(input("ingrese la temperatura:"))
    temperatura.append(t)
print(temperatura)

promedio = sum(temperatura)/ len(temperatura)
print(f"el promedio de todas las temperaturas es :{promedio:.2f}")

if t < 20:
    print("tiene que arreglar el aire, temperatura muy baja")
elif 20 <= t <= 30:
    print("el aire esta en excelentes condiciones")
else:
    print("el aire esta malo, temperatura muy alta")        