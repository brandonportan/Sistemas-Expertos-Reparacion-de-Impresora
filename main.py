# Ejemplo de uso de Grids: 
#Importar Libreria
import flet as ft

#Funcion Main
def main(page:ft.Page):
    page.title = 'Uso de Grid'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.vertical_alignment = ft.VerticalAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Funcion Agregar Nota
    def Add_Note(e):
         New_Note = Create_Note('Nueva Nota')
         Grid.controls.append(New_Note)
         page.update()

    #Funcion Borrar Nota
    def Delete_Note(Note):
        Grid.controls.remove(Note)
        page.update()
    
    #Funcion Crear Nota
    def Create_Note(varText):
            Note_Content= ft.TextField(value=varText,multiline=True,
            bgcolor = ft.colors.ORANGE_100)
            Note = ft.Container(
                content=ft.Column(
                    controls=[
                        Note_Content,ft.IconButton(icon=ft.icons.DELETE,on_click=lambda _: Delete_Note(Note))
                        ,ft.TextButton("Si")
                        ,ft.TextButton(text="No")
                    ]
                ),
                #         width=200,
            height=200,
            bgcolor = ft.colors.ORANGE_100,
            border_radius=10,padding=10
            )
            return Note #La funcion debe retornar un Container...

    #Usar Lista
    Notes=[
        '1er. Nota',
        '2da. Nota',
        '3er. Nota',
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
                      ft.Text('Mis Notas Adhesivas',size=24,weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                      ft.IconButton(icon=ft.icons.ADD,on_click=Add_Note,icon_color=ft.colors.WHITE),
                 ],
                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            Grid
         )
#Mostrar App
ft.app(target=main)