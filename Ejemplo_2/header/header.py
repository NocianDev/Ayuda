import reflex as rx
from Ejemplo_2.styles.styles import Size
from Ejemplo_2.styles.colors import Color
from Ejemplo_2.components.body import body

def header() -> rx.Component:
    return body("/Land_Def.png","This is an example web page","Learn More","/services")
