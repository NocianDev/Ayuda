import reflex as rx
from Ejemplo_2.components.nabvar import *
from Ejemplo_2.header.header import header
from Ejemplo_2.components.footer import footer
from Ejemplo_2.styles.styles import Size
import Ejemplo_2.styles.styles as styles
from Ejemplo_2.styles.colors import Color
from Ejemplo_2.components.link_button import link_button
import Ejemplo_2.Variables.Texto as V

def contact_page() -> rx.Component:
    return rx.box(
        logo(),
        navbar(),
        rx.center(
            rx.vstack(
                link_button("My email",f"{V.E}","/Email.svg",f"mailto:{V.Mail}"),
                link_button("My Whatsapp",f"{V.W}","/Whats.svg","https://wa.me/528211206567"),
                align="center",
                margin_top="2em"
            ),
        ),
        bg=Color.BACKGROUND.value,
        height="100vh"
    )
   