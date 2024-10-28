import reflex as rx
import constants as const
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
from link_bio.styles.styles import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Collaborate"),
        rx.chakra.responsive_grid(
            link_sponsor(
                "elgato.svg",
                const.ELGATO_URL,
                "ElGato logo"
            ),
            link_sponsor(
                "mvp.png",
                const.MVP_URL,
                "Microsoft Logo"
            ),
            spacing=Size.BIG.value,
            columns=[1, 2]
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )
