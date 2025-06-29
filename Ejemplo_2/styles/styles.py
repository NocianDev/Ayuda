from enum import Enum
import reflex as rx
from Ejemplo_2.styles.fonts import Font
from Ejemplo_2.styles.fonts import FontWeight
from Ejemplo_2.styles.colors import Color

STYLESHEETS= [
    "https://fonts.googleapis.com/css2?=Playfair Display:wght@600&display=swap",
    "https://fonts.googleapis.com/css2?=Roboto:wght@700&display=swap",
    "https://fonts.googleapis.com/css2?=Quicksand:wght@300&display=swap",
    "https://fonts.googleapis.com/css2?=Poppins:wght@700;500&display=swap",
    "https://fonts.googleapis.com/css2?=Oswald:wght@600&display=swap",
    "https://fonts.googleapis.com/css2?=Nunito:wght@600;400&display=swap",
    "https://fonts.googleapis.com/css2?=Merriweather:wght@700&display=swap",
    "https://fonts.googleapis.com/css2?=Open Sans:wght@400&display=swap",
]


class Size(Enum):
    ZERO="0em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    JUMBO="3em"
    VERY_JUMBO="4em"

BASE_STYLE={
    rx.text:{
        "white_space":"normal",
    },
    "*": {
        "box-sizing": "border-box",
        "padding": "0",
        "margin": "0"
    },
    "body": {
        "overflow-x": "hidden",
        "max-width": "100vw"
    },
    rx.button:{
       " background_color":"transparent",
        "border":"none",
        "_hover":{
            "bg": "none"},
        "_active":{
            "bg": "none"},
        "outline":"none",
        "color":"black"
    },
}



button_title_style = dict(
    font_family=Font.CONTACT.value,
    font_weight=FontWeight.SEMIBOLD.value,  # Más presencia visual
    font_size="clamp(1.4rem, 4.5vw, 1.7rem)",  # Ligeramente más grande
    color=Color.HEADER.value,
    letter_spacing="0.03em",  # Pequeño detalle para mejor legibilidad
)

button_body_style = dict(
    font_family=Font.CONTACT.value,
    font_weight=FontWeight.REGULAR.value,  # Mejor que LIGHT para contraste
    font_size="clamp(0.75rem, 2.5vw, 1rem)",  # Más equilibrado visualmente
    color=Color.FOOTER.value,
    line_height="1.4",  # Mejora el espaciado entre líneas
)