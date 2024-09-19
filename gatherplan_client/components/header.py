import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor


def header(back_button_url: str):

    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.button(
                    rx.icon(
                        tag="chevron-left",
                        size=24,
                        # color=AppColor.MAIN_COLOR,
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
                rx.box(width="40px"),
                rx.button("로그아웃", on_click=State.logout),
                spacing="0",
            ),
            width="360px",
        ),
        width="100%",
        height="10%",
        align="center",
        padding_top="10px",
    )
