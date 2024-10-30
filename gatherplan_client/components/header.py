import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor


def header(back_button_url: str):
    return rx.box(
        rx.vstack(
            rx.box(
                rx.hstack(
                    rx.button(
                        rx.icon(
                            tag="chevron-left",
                            size=24,
                            stroke_width=3,
                        ),
                        color=AppColor.BLACK,
                        background_color=AppColor.WHITE,
                        on_click=rx.redirect(back_button_url),
                        padding="0px",
                    ),
                    rx.image(
                        src="/images/index_logo.png",
                        width="140px",
                        height="30px",
                        padding_top="2px",
                    ),
                    rx.box(width="190px"),
                    rx.button(
                        rx.icon(
                            tag="log-out",
                            size=24,
                            stroke_width=3,
                        ),
                        color=AppColor.BLACK,
                        background_color=AppColor.WHITE,
                        on_click=State.logout,
                        padding="0px",
                    ),
                    spacing="0",
                ),
                width="360px",
            ),
            width="100%",
            height="48px",
            align="center",
            padding_top="10px",
        ),
        position="fixed",
        top="0",
        width="100%",
        z_index="999",
        background_color="rgba(255, 255, 255, 0.95)",
        backdrop_filter="blur(10px)",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.1)",
        border_bottom="1px solid rgba(0, 0, 0, 0.1)",
    )
