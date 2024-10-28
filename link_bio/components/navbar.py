import reflex as rx
from link_bio.styles.styles import Size as Size
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color
from link_bio.styles.colors import TextColor


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            rx.chakra.span("< Dev. ", color=Color.PRIMARY.value),
            rx.chakra.span("Dorian />", color=Color.SECONDARY.value),
            font_family="Comfortaa-Medium",
            style=styles.navbar_tittle_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
