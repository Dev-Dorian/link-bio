import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.title import title
from link_bio.styles.styles import Size, Spacing
from link_bio.styles.colors import TextColor
from link_bio.styles.colors import Color
import constants as const
import datetime


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.chakra.avatar(name="Dorian Hidalgo", size="xl", src="avatar.jpg",
                                 color=TextColor.BODY.value, bg=Color.CONTENT.value, padding="2px", border="4px", border_color=Color.PRIMARY.value),
                position="relative"
            ),
            rx.hstack(
                rx.heading("Dorian Hidalgo", size=Spacing.BIG.value,
                           color=TextColor.HEADER.value),
                rx.text("@Dev. Dorian", margin_top=Size.ZERO.value,
                        color=Color.PRIMARY.value),

                rx.box(
                    link_icon("icons/github.svg",
                              const.GITHUB_URL, "GitHub"),
                ),
                padding_bottom="10px",
                spacing=Spacing.ZERO.value,
                align_items="start",

            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.hstack(
                rx.flex(
                    info_text("+7", " years of experience"),
                    info_text("+10", " projects"),
                    width="100%",
                    flex_wrap="wrap",
                    spacing="2",
                    padding_bottom="10px",
                ),
                rx.text("Software engineer with 5+ years of experience in full-stack development and quality assurance, focused on delivering high-quality software solutions. Proven ability to design, develop, and execute automated test scripts to ensure software functionality and reliability. Proficient in various programming languages and frameworks, including JavaScript, React, C# and Java.",
                        font_size=Size.DEFAULT.value, color=TextColor.BODY.value),
                width="100%",
                spacing=Spacing.BIG.value
            ),
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
    )
