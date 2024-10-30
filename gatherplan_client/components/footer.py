import reflex as rx
from gatherplan_client.components.schema import AppFontFamily


def footer():
    return rx.center(
        rx.center(
            rx.hstack(
                rx.link(
                    rx.vstack(
                        rx.icon(
                            tag="plus",
                            size=24,
                            color="#666666",
                        ),
                        rx.text(
                            "만들기",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_size="12px",
                            color="#666666",
                        ),
                        width="60px",
                        align="center",
                    ),
                    href="/make_meeting",
                    _hover={"text_decoration": "none"},
                ),
                rx.link(
                    rx.vstack(
                        rx.icon(
                            tag="users",
                            size=24,
                            color="#666666",
                        ),
                        rx.text(
                            "참여하기",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_size="12px",
                            color="#666666",
                        ),
                        width="60px",
                        align="center",
                    ),
                    href="/enter_meeting_code",
                    _hover={"text_decoration": "none"},
                ),
                rx.link(
                    rx.vstack(
                        rx.icon(
                            tag="calendar",
                            size=24,
                            color="#666666",
                        ),
                        rx.text(
                            "현황보기",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_size="12px",
                            color="#666666",
                        ),
                        width="60px",
                        align="center",
                    ),
                    href="/check_meeting",
                    _hover={"text_decoration": "none"},
                ),
                spacing="48px",
                justify="center",
                padding_y="12px",
            ),
            width="360px",
        ),
        position="fixed",
        bottom="0",
        width="100%",
        z_index="999",
        background_color="rgba(255, 255, 255, 0.95)",
        backdrop_filter="blur(10px)",
        box_shadow="0 -2px 4px rgba(0, 0, 0, 0.1)",
        border_top="1px solid rgba(0, 0, 0, 0.1)",
    )
