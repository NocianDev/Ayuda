import reflex as rx

def popup(src: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.image(
                src=src,
                box_size="250px",   # Tamaño miniatura
                border_radius="md",
                cursor="pointer",
                
            ),
            border_width="3px",
            border_color="black",
            align="center"
        ),
        rx.dialog.content(
            rx.dialog.close(rx.button("", position="absolute", top="2", right="2")),
            rx.image(
                src=src,
                width="100vw",      # Ocupa gran parte de la pantalla
                max_height="90vh",
                object_fit="contain",
                border_radius="lg"
            ),
            padding="0",
            align="center"
        )
    )