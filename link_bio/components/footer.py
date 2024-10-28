import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size, Spacing
from link_bio.styles.colors import TextColor, Color
import constants as const


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value),
        rx.link(
            rx.box(
                f"© 2016-{datetime.date.today().year}",
                rx.text("Dev. Dorian BY Dorian Hidalgo",
                        color=Color.PRIMARY.value),  " v3.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.DEVDORIAN_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.text(
                    "Building Software For The World",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
                is_external=True
            ),
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value,
        padding_y=Size.VERY_BIG.value
    )
