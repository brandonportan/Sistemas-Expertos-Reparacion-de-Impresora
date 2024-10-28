# Ejemplo de uso de Grids: 
#Importar Libreria
import flet as ft
from Pregunta import Pregunta


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
        return  pregunta.si
    else:
        return pregunta.no
    

preguntaGlobal = p10

#Funcion Main
def main(page:ft.Page):    
    page.title = 'Uso de Grid'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.vertical_alignment = ft.VerticalAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    

    # Funcion Agregar Nota
    def Refresh_Note(e): #recibir el texto de la pregunta
        global preguntaGlobal
        preguntaGlobal = p10
        Grid.controls.clear()
        Grid.controls.append(Create_Note(preguntaGlobal.pregunta))
        page.update()

    def opcionSi(e):
        global preguntaGlobal
        New_Note = Create_Note(preguntaGlobal.si.pregunta)
        Grid.controls.append(New_Note)
        preguntaGlobal = obtenerRespuesta(preguntaGlobal, "si")
        print(preguntaGlobal.pregunta)
        page.update()

    def opcionNo(e):   
        global preguntaGlobal     
        New_Note = Create_Note(preguntaGlobal.no.pregunta)
        Grid.controls.append(New_Note)
        preguntaGlobal = obtenerRespuesta(preguntaGlobal, "no")
        print(preguntaGlobal.pregunta)
        page.update()

    #Funcion Crear Nota
    def Create_Note(varText):
            Note_Content= ft.TextField(value=varText,multiline=True,
            bgcolor = ft.colors.ORANGE_100,read_only=True,text_size=17)
            Note = ft.Container(
        content=ft.Column(
            controls=[
                Note_Content,
                # Agrega un Row para los botones
                ft.Row(
                    controls=[
                            ft.ElevatedButton(text="Si", on_click=lambda _: opcionSi(Note),bgcolor=ft.colors.GREEN_300,style=ft.ButtonStyle(
                            color=ft.colors.WHITE  # Cambiar color del texto a blanco
                            )),
                            ft.ElevatedButton(text="No", on_click=lambda _: opcionNo(Note),bgcolor=ft.colors.RED_300,style=ft.ButtonStyle(
                            color=ft.colors.WHITE  
                )),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                
                )
            ]
            ,alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
            height=200,
            bgcolor = ft.colors.ORANGE_100,
            border_radius=10,padding=10
            )
            return Note #La funcion debe retornar un Container...

    #Usar Lista
    Notes=[
        preguntaGlobal.pregunta
    ]
    

    #Declara GridView
    Grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=20,
        #horizontal=False
    )
    for Note in Notes:
        Grid.controls.append(Create_Note(Note))

    #Actualizar Pagina
    page.add(
            ft.Row(
                 [
                      ft.Text('Sistema Experto de Impresora',size=24,weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                      ft.IconButton(icon=ft.icons.REFRESH,on_click=Refresh_Note,icon_color=ft.colors.WHITE,icon_size=40),
                 ],
                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            Grid
         )
    
    print("Hola")
#Mostrar App
ft.app(target=main)


#preguntaGlobal = obtenerRespuesta(preguntraGlobal, "si") #!En la función sí
#preguntaGlobal = obtenerRespuesta(preguntraGlobal, "no") #?En la función no