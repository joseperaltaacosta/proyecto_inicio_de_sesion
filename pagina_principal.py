import flet as ft

def main(page: ft.Page):
    page.title="INICIAR SESION"

    page.bgcolor = ft.colors.GREEN_200
    page.window_height = 550
    page.window_width = 800
    page.on_resize = False
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    page.update()


    img = ft.Image(src=f"/IMAGENES/inicio_de_sesion.png",
    width=225,
    height=200)

    tb1 = ft.TextField(label="Usuario",width=400)
    tb2 = ft.TextField(label="Contraseña", password=True, can_reveal_password=True,width=400)
    colDatos = ft.Column(controls=[tb1,tb2],spacing=20)
    conDatos = ft.Container(content=colDatos,padding=ft.padding.only(bottom=25))
    usuario=tb1.value
    contraseña=tb2.value 


    def comprobar_login(e):
        vDatos=[]
        f = open("usu.txt","r")
        contador=0
        for linea in f:
            l = linea.split(sep=";")
            vDatos.append(l)
        print(vDatos)
        if contador<=3:
            if vDatos.count(tb1.value)==0:
                dlg = ft.AlertDialog(title=ft.Text("Usuaruio correcto"))
                page.dialog = dlg
                dlg.open = True
            f.close


    boton=ft.ElevatedButton("INICIAR SESION", icon="settings",bgcolor=ft.colors.GREEN_100,on_click=comprobar_login)

    page.add(img,conDatos,boton)

ft.app(target=main,assets_dir="IMAGENES")