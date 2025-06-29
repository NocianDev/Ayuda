import reflex as rx
from Ejemplo_2.styles.styles import Size
from Ejemplo_2.styles.fonts import Font
from Ejemplo_2.styles.fonts import FontWeight
from Ejemplo_2.styles.colors import Color

def logo() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                rx.image(
                    src="/Logo_Def.png" 
                ),
                rx.heading("COMPANY NAME",font_family=Font.LOGO,font_weight=FontWeight.BOLD.value,),
                align_items="center",  # Aquí alineamos verticalmente
                spacing="4",           # Espacio entre logo y texto
            ),
        ),
        width="100%",
        bg=Color.HEADER.value
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.center(
            rx.flex(
                rx.link(rx.button("Home",_hover={
                "color": "#ff6b00", 
                "transition": "all 0.3s ease"
                }), href="/"),
                rx.link(rx.button("Services",_hover={
                "color": "#ff6b00", 
                "transition": "all 0.3s ease"
                }), href="/services"),
                rx.link(rx.button("Projects",_hover={
                "color": "#ff6b00", 
                "transition": "all 0.3s ease"
                }), href="/project"),
                rx.link(rx.button("Contact",_hover={
                "color": "#ff6b00", 
                "transition": "all 0.3s ease"
                }), href="/contact"),
                direction="row",
                display="flex",
                min_width="max-content",  
                gap="1rem",
                font_family=Font.LOGO,
                font_weight=FontWeight.MEDIUM.value,
                
            )
        ),
        overflow_x="auto",        
        white_space="nowrap",      
        width="100%",
        padding="0.5rem",
        z_index="1000",
        bg="linear-gradient(to right, #ffe0c0, #fff6e5)",  # Degradado durazno claro
        box_shadow="0 2px 8px rgba(0, 0, 0, 0.05)"
    )