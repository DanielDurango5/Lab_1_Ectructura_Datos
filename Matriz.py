import numpy as np

filas = 100_000
columnas = 100_000
nombre_archivo = "lab_1_matriz_100k.bin"

with open(nombre_archivo, "wb") as f:
    for _ in range(filas):
        fila = np.random.randint(0, 2, size=columnas, dtype=np.uint8)
        fila_comprimida = np.packbits(fila)
        f.write(fila_comprimida)

print("Archivo creado.")