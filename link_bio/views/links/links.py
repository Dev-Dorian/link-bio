import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size, Spacing
import constants as const


def links() -> rx.Component:
    return rx.vstack(
        title("Resources"),
        link_button(
            "Projects",
            "Check my programming projects",
            "/icons/code.svg",
            const.GITHUB_URL,
            True,

        ),
        link_button(
            "LinkedIn",
            "Discovering new opportunities",
            "/icons/linkedin.svg",
            const.LINKEDIN_URL
        ),
        link_button(
            "Twitch",
            "Transmissions about programming",
            "/icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "Discord",
            "Community chat and study groups",
            "/icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "YouTube",
            "YouTube channel",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,

    )
