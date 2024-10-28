import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                footer(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value,
                # padding="50px",
            )
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    # stylesheets=[
    #    "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    # ],
    style=styles.BASE_STYLE
)
app.add_page(index, title="< Dev. Dorian />",
             description="Hello, I am Dorian", image="avatar.jpg")
