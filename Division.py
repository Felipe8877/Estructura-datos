def division_por_restas(dividendo, divisor, contador=0):
    if dividendo < divisor:
        return contador
    return division_por_restas(dividendo - divisor, divisor, contador + 1)
resultado = division_por_restas(26, 35)
print(resultado)