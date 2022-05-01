alto = float(input())
ancho = float(input())
profundo =  float(input())
volumen = float(alto*ancho*profundo)
costoFinal = float(volumen*5)

if (alto > 30):
    costoFinal += 2000

if (costoFinal > 10000):
    costoFinal = costoFinal * 1.19

print(volumen)
print(costoFinal)
