import reflex as rx
from Ejemplo_2.components.nabvar import *
from Ejemplo_2.header.header import header
from Ejemplo_2.components.footer import footer
from Ejemplo_2.styles.styles import Size
import Ejemplo_2.styles.styles as styles
from Ejemplo_2.styles.colors import Color
from . import pages

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        logo(),
        navbar(),
        rx.center(   
            rx.vstack(
                
                header(),
                footer(),
                align="center",
                max_width="800px",
                width="100%",
            )
        ),
        rx.box(
            width="100%",
            bg=Color.FOOTER.value,
            height="50px",
        ),
        bg=Color.BACKGROUND.value
    )

   

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    
)
app.add_page(index,
             title="TNY Web Lab: Tailoring Navigation for You ",
             image="/NYT.ico")
app.add_page(pages.contact_page
             ,route="/contact",
             title="TNY Web Lab: Tailoring Navigation for You ")
app.add_page(pages.project_page,
             route="/project",
             title="TNY Web Lab: Tailoring Navigation for You ")
app.add_page(pages.services_page,
             route="/services",
             title="TNY Web Lab: Tailoring Navigation for You ")


