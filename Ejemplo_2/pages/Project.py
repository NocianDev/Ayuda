import reflex as rx
from Ejemplo_2.components.nabvar import *
from Ejemplo_2.header.header import header
from Ejemplo_2.components.footer import footer
from Ejemplo_2.styles.styles import Size
import Ejemplo_2.styles.styles as styles
from Ejemplo_2.styles.colors import Color
from Ejemplo_2.components.project import pro
from Ejemplo_2.components.pop import popup
from Ejemplo_2.styles.fonts import Font
from Ejemplo_2.styles.fonts import FontWeight

def project_page() -> rx.Component:
    return rx.box(
        logo(),
        navbar(),
        rx.center(   
            rx.vstack(
                rx.heading("My projects",
                        font_weight=FontWeight.BOLD.value,
                        font_family=Font.PROJECT.value,),
                rx.grid(
                    popup("/Ejemplo_Pag.png"),
                    
                    spacing="6",
                    columns="3",
                    margin_top="1em"
                ),
                align="center",
                width="100%",
                padding_x="2em"
            ),
            margin_top="2em"
        ),
        bg=Color.BACKGROUND.value,
        height="100vh"
    )
   