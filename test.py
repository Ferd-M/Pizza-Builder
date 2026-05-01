import flet as ft

def main(page: ft.Page):

    def changeImage(e):
        pepperoniImage.visible = pepperoniSwitch.value
        OnionImage.visible = onionSwitch.value
        MushroomImage.visible = mushroomSwitch.value
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Pizza"
    page.theme_mode = ft.ThemeMode.LIGHT

    baseImage = ft.Image(src="images/Pizza_cheese.png")
    pepperoniImage = ft.Image(src="images/pepperoni.png", visible=False)
    OnionImage = ft.Image(src="images/Onion.png", visible=False)
    MushroomImage = ft.Image(src="images/Mushroom.png", visible=False)

    pepperoniSwitch = ft.Switch(label="Pepperoni", on_change=changeImage)
    onionSwitch = ft.Switch(label="Onion", on_change=changeImage)
    mushroomSwitch = ft.Switch(label="Mushroom", on_change=changeImage)

    pizzaStack = ft.Stack(
        [
            baseImage,
            pepperoniImage,
            OnionImage,
            MushroomImage
        ],
        width=300,
        height=300
    )

    page.add(
        pizzaStack,
        pepperoniSwitch,
        onionSwitch,
        mushroomSwitch
    )

ft.run(main=main)