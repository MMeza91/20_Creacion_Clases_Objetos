
class Te:
    duracion = 365

    sabores = {
        1 : {"Nombre" : "Té Negro", "Tiempo" : 3, "Recomendacion" : "Desayuno"},
        2 : {"Nombre" : "Té Verde", "Tiempo" : 5, "Recomendacion" : "Almuerzo"},
        3 : {"Nombre" : "Agua de Hierbas", "Tiempo" : 6, "Recomendacion" : "Once"}
    }

    precios = {
        300 : 3000,
        500 : 5000

    }


    @staticmethod
    def receta(sabor:int):
        #Retorna el tiempo de preparación en min y recomendacion segun sabor ingresado
        pedido = Te.sabores[sabor]
        
        return pedido["nombre"], pedido["Tiempo"], pedido["Recomendacion"]

    @staticmethod
    def obtener_precio(formato:int):
        #Retorna precio segun formato indicado

        return Te.precios[formato]