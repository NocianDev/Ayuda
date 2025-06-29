import reflex as rx
from Ejemplo_2.styles.styles import Size
from Ejemplo_2.styles.colors import Color
from Ejemplo_2.styles.fonts import Font
from Ejemplo_2.styles.fonts import FontWeight

def body(image: str, text: str, button: str, ref: str):
    return rx.box(
        rx.image(
            src=image,
            width="100%",
            height="auto",
            object_fit="cover",
        ),
        rx.flex(
            rx.vstack(
                rx.text(
                    text,
                    font_size="clamp(1.5rem, 5vw, 3rem)",
                    font_weight=FontWeight.SEMIBOLD.value,
                    font_family=Font.HERO.value,
                    color="white",
                    text_align="center",
                ),
                rx.link(
                    rx.button(
                        button,
                        font_size="clamp(0.5rem, 4vw, 1.5rem)",
                        color="white",
                        _hover={"bg": "#e25e5e"},
                        font_weight=FontWeight.REGULAR.value,
                        font_family=Font.BUTTON.value,
                    ),
                    href=ref,
                    bg=Color.LOGO,
                    padding_y="0.3vw",
                    padding_x="1vw",
                    border_radius="1.5em",
                ),
                spacing="4",
                align="center",
            ),
            position="absolute",
            top="13%",
            left="0",
            width="100%",
            height="100%",
            justify="center",
            align="center",
            z_index="1",
            padding_x="2",
            text_align="center",
        ),
        position="relative",
        width="100%",
        height="auto",
        overflow="hidden",
    )