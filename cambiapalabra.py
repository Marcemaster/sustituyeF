import sys

argumentos = sys.argv

if len(argumentos) < 2:
    argumentos.append(input("Introduce el nombre del fichero: "))
    argumentos.append(input("Introduce la palabra original: "))
    argumentos.append(input("Introduce la nueva palabra: "))
elif len(argumentos) < 3:
    argumentos.append(input("Introduce la palabra original: "))
    argumentos.append(input("Introduce la nueva palabra: "))
elif len(argumentos) < 4:
    argumentos.append(input("Introduce la nueva palabra: "))


nombreF = argumentos[1]
original = argumentos[2]
nueva = argumentos[3]




nombreF = "fichero.txt"

f = open(nombreF, "r")

texto_original = f.read()
f.close()

texto_nuevo = texto_original.replace(original, nueva)
f = open(nombreF, "w")
f.write(texto_nuevo)
f.close()


