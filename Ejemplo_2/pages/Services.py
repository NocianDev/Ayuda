import reflex as rx
from Ejemplo_2.components.nabvar import *
from Ejemplo_2.header.header import header
from Ejemplo_2.components.footer import footer
from Ejemplo_2.styles.styles import Size
import Ejemplo_2.styles.styles as styles
from Ejemplo_2.styles.colors import Color
import Ejemplo_2.Variables.Texto as V
from Ejemplo_2.components.serv import serv

def services_page() -> rx.Component:
    return rx.box(
        logo(),
        navbar(),
        rx.center(
            rx.grid(
                serv("🛠️ Services",f"{V.S}","#e3f2fd"),
                serv("🌐 Responsive Web Design",f"{V.D}", "#e0f7fa"),
                serv("🛒 Online Stores",f"{V.T}", "#e8f5e9"),
                serv("🔍 Basic SEO Optimization",f"{V.O}", "#fff3e0"),
                serv("⚙️ Maintenance and Updates",f"{V.M}", "#f3e5f5"),
                serv("📱 Social Media Integration",f"{V.I}", "#e1f5fe"),
                serv("⚡ Custom Development",f"{V.D1}", "#fce4ec"),
                columns="3",
                spacing="1",
                width="100%",
                align="center",
                padding_x="1em",
                padding_top="2em"
            )
        ),
        bg=Color.BACKGROUND.value
    )
   


  

