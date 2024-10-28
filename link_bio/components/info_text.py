import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color
from link_bio.styles.colors import TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, body, font_weight="bold",
                color=Color.PRIMARY.value, font_size=Size.MEDIUM.value),
    )
