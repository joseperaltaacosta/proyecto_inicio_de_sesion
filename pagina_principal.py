import flet as ft

def main(page: ft.Page):
    page.title="INICIAR SESION"

    page.bgcolor = ft.colors.GREEN_200
    page.window_left = 800
    page.window_top = 800
    page.on_resize = False

    img = ft.Image(
        src=f"/IMAGENES/inicio_de_sesion.png",
        width=225,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )


    page.add(img)

ft.app(target=main,assets_dir="IMAGENES")