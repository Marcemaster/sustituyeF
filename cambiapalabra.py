original = input("Introduce la palabra que quieres cambiar: ")
nueva = input("Introduce la nueva palabra: ")

nombreF = "fichero.txt"

f = open(nombreF, "r")

texto_original = f.read()
f.close()

texto_nuevo = texto_original.replace(original, nueva)
f = open(nombreF, "w")
f.write(texto_nuevo)
f.close()

