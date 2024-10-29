# Ejemplo de uso de Grids: 
#Importar Libreria
import flet as ft
import Preguntas as p    

preguntaGlobal = p.p10

#Funcion Main
def main(page:ft.Page):    
    page.title = 'Uso de Grid'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.vertical_alignment = ft.VerticalAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    def deshabilitarBotoness(boton1, boton2):
        boton1.style.bgcolor = ft.colors.GREY_400
        boton2.style.bgcolor = ft.colors.GREY_400
        boton1.disabled= True
        boton2.disabled = True


    def validarProximaPregunta(preguntaActual):
        if (preguntaActual.si is None and preguntaActual.no is None):
            return False
        else:
            return True

    def crearTarjetaFinal():
        notaFinal = ft.Container(
                 content=ft.Column(
                    controls=[
                        ft.TextField(value="La asistencia ha finalizado",multiline=True,
                        bgcolor = ft.colors.ORANGE_100,read_only=True,text_size=17)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
            height=200,
            bgcolor = ft.colors.ORANGE_100,
            border_radius=10,padding=10
            )
        Grid.controls.append(notaFinal)
        page.update()


    # Funcion Agregar Nota
    def Refresh_Note(e): #recibir el texto de la pregunta
        global preguntaGlobal
        preguntaGlobal = p.p10
        Grid.controls.clear()
        Grid.controls.append(Create_Note(preguntaGlobal.pregunta, False))
        page.update()

    def opcionSi(boton1, boton2):
        global preguntaGlobal
        if validarProximaPregunta(preguntaGlobal.si):
            New_Note = Create_Note(preguntaGlobal.si.pregunta, False)
            Grid.controls.append(New_Note)
            preguntaGlobal = preguntaGlobal.si
            print(preguntaGlobal.pregunta)
        else:
            New_Note = Create_Note(preguntaGlobal.si.pregunta, True)
            Grid.controls.append(New_Note)
            crearTarjetaFinal()
        deshabilitarBotoness(boton1, boton2)
        page.update()      

    def opcionNo(boton1, boton2):   
        global preguntaGlobal
        if validarProximaPregunta(preguntaGlobal.no):
            New_Note = Create_Note(preguntaGlobal.no.pregunta, False)
            Grid.controls.append(New_Note)
            preguntaGlobal = preguntaGlobal.no
            print(preguntaGlobal.pregunta)
        else:
            New_Note = Create_Note(preguntaGlobal.no.pregunta, True)
            Grid.controls.append(New_Note)
            crearTarjetaFinal()
        deshabilitarBotoness(boton1, boton2)
        page.update()       

    #Funcion Crear Nota
    def Create_Note(varText, deshabilitarBotones):
            Note_Content= ft.TextField(value=varText,multiline=True,
            bgcolor = ft.colors.ORANGE_100,read_only=True,text_size=17)

            btn_si = ft.ElevatedButton(text="Si", on_click=lambda _: opcionSi(btn_si, btn_no),bgcolor=ft.colors.GREEN_300,style=ft.ButtonStyle(
                            color=ft.colors.WHITE  # Cambiar color del texto a blanco
                            ))
            
            btn_no = ft.ElevatedButton(text="No", on_click=lambda _: opcionNo(btn_si, btn_no),bgcolor=ft.colors.RED_300,style=ft.ButtonStyle(
                            color=ft.colors.WHITE  
                            ))
            Note = ft.Container(
        content=ft.Column(
            controls=[
                Note_Content,
                # Agrega un Row para los botones
                ft.Row(
                    controls=[
                            btn_si,
                            btn_no
                            
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

            if deshabilitarBotones:
                deshabilitarBotoness(btn_no, btn_si)
            

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
        Grid.controls.append(Create_Note(Note, False))

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