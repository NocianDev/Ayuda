import reflex as rx
from Ejemplo_2.styles.styles import Size
from Ejemplo_2.styles.fonts import Font
from Ejemplo_2.styles.fonts import FontWeight

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Examples",
                margin_top=Size.SMALL.value,
                font_family=Font.LOGO.value,
                font_weight=FontWeight.SEMIBOLD.value,
                font_size=Size.BIG.value),
        rx.text("In this section, examples are shown as if they \"products\" for sale.",
                font_family=Font.SERVICES_BODY.value,
                font_weight=FontWeight.REGULAR.value,
                font_size=Size.DEFAULT.value,
                align="center"),
        rx.grid(
            rx.image(src="Grafica.png",bg="#FFE59E"),
            rx.image(src="Foco.png",bg="#A1E1D2"),
            rx.image(src="Bolsa_Ex.png",bg="#B0E4EA"),
            columns="3",
            spacing="2",
            padding_bottom=Size.MEDIUM.value 
        ),
        align="center",
        spacing="2",
        widht="100%"
    )