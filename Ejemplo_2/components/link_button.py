import reflex as rx
import Ejemplo_2.styles.styles as styles
from Ejemplo_2.styles.colors import Color
from Ejemplo_2.styles.styles import Size
from Ejemplo_2.styles.styles import button_title_style
from Ejemplo_2.styles.styles import button_body_style

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                rx.image(
                    src=image,
                    width="clamp(2rem, 9vw, 2.5rem)",
                    height="clamp(2rem, 9vw, 2.5rem)",
                    margin_y=styles.Size.MEDIUM.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title,
                ),
                rx.vstack(
                    rx.text(title, style=button_title_style),
                    rx.text(body, style=button_body_style),
                    spacing="0",
                    align_items="start",
                    margin=styles.Size.ZERO.value,
                    margin_top=styles.Size.SMALL.value,
                    padding_right=styles.Size.SMALL.value,
                ),
                spacing="1",
                width="100%",
                align="center",
            ),
            bg=Color.LOGO.value,
            border_radius="1.5em",
            padding="1em",
            box_shadow="0 6px 12px rgba(0, 0, 0, 0.15)",
            transition="all 0.3s ease-in-out",
            _hover={
                "transform": "scale(1.02)",
                "filter": "brightness(1.05)",
                "box_shadow": "0 8px 16px rgba(0, 0, 0, 0.25)",
            },
        ),
        href=url,
        is_external=True,
        width="100%",
        text_decoration="none",
    )