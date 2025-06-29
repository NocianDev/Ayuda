import reflex as rx
import Ejemplo_2.Variables.Texto as V

def pro(image: str,):
    return rx.box(
        rx.image(src=image),
        border_width="3px",
        border_color="black"
    )
