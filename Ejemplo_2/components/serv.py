import reflex as rx
import Ejemplo_2.Variables.Texto as V
from Ejemplo_2.styles.fonts import Font
from Ejemplo_2.styles.fonts import FontWeight

def serv(title: str, body: str, bg_color: str = "#ffffff"):
    return rx.box(
        rx.vstack(
            rx.heading(title,
                       font_size="clamp(0.8rem, 3.7vw, 1.5rem)",
                       padding_top="0.3em",
                       font_weight=FontWeight.SEMIBOLD.value,
                       font_family=Font.SERVICES_TITLE.value,),
            rx.text(body, 
                    color="gray",
                    font_size="clamp(0.5rem, 3vw, 1rem)",
                    padding_x="0.4em",
                    font_weight=FontWeight.REGULAR.value,
                    font_family=Font.SERVICES_BODY.value),
            align="center",
            spacing="2",
        ),
        bg=bg_color,
        padding="4",
        border_radius="xl",
        box_shadow="md",
        height="clamp(25rem, 5vw, 30rem)",
        width="100%"
    )