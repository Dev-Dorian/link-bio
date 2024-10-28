import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Spacing


def link_button(title: str, body: str, image: str, url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:
    # return rx.link(
    #
    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
                alt=title
            ),
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.SMALL.value,
                    style=styles.button_tittle_style
                ),
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value,
                    style=styles.button_body_style
                ),
                spacing=Spacing.VERY_SMALL.value,
                align_items="start",
                # padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value,
            ),

            align="center",
            width="100%",
        ),
        margin_bottom="20px",
        border=f"{'2px' if highlight_color !=
                  None else '0px'} solid {highlight_color}",
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        on_click=rx.redirect(path=url, external=is_external)
    )
    # )
