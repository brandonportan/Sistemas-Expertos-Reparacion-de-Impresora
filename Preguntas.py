import Pregunta

p1 = Pregunta("¡PC reconoce la impresora?", 
                Pregunta("Mantenimiento",None,None),
                Pregunta("Reinstalar Controladores",None,None),)
p2 = Pregunta("¿Muestra código de error?", 
              Pregunta("Investigar codigo error",None,None),
              p1)
p3 = Pregunta("¿Cable USB conectado?",
                p2,
                Pregunta("Conectar USB",None,None))
p4 = Pregunta("El papel está atascado?",
                Pregunta("Abra la bandeja y retire el papel",None,None),
                p3)
p5 = Pregunta("Tiene papel la bandeja?",
                p4,
                Pregunta("Cargar papel",None,None))

#la otra línea de sí imprime
p6 = Pregunta("¿Hay suficiente tinta en los contenedores?",
                    Pregunta("Limpiar inyectores",None,None),
                    Pregunta("Llevar los envases",None,None))
p7 = Pregunta("¿Imprime mal?",
                p6,
                Pregunta("Todo Bien",None,None))

#imprime
p8 = Pregunta("¿Imprime?",
                p7,
                p5)

p9 = Pregunta("¿Está conectado el cable de corriente?",
                Pregunta("Considerar cambiar cable",None,None),
                Pregunta("Conectar cable",None,None))
#enciende
p10 = Pregunta("¿Enciende?",
                p8,
                p9)


def obtenerRespuesta(pregunta, respuesta):
    if respuesta == "si":
        return pregunta.si
    else:
        return pregunta.no

    
print(obtenerRespuesta(p10, "si"))