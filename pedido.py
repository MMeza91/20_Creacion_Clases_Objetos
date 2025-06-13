from te import Te

print("Elige el sabor de té (1 = Té Negro / 2 = Té Verde / 3 = Agua de hierba)")

sabor = int(input("Elige un sabor: "))

print("Elige el formato (300 o 500) gramos: ")

formato = int(input("Elige el formato: "))

nombre, tiempo, recomendacion = Te.receta(sabor)

precio = Te.obtener_precio(formato)

duracion = Te.duracion