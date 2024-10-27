import reflex as rx

from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting_already",
    header_url="/",
    page_text="",
)
def join_meeting_already() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                main_sub_text_center_box(
                    "이미 참여한 약속입니다.",
                    "현황보기를 통해 약속 정보, 약속 참여 정보를 확인해보세요.",
                ),
            ),
            rx.vstack(
                rx.box(height="58vh"),
                main_button(
                    text="현황보기",
                    on_click=rx.redirect("/check_meeting"),
                ),
                main_button(
                    text="메인화면으로",
                    on_click=rx.redirect("/"),
                    sub_button=True,
                ),
                spacing="5",
            ),
            width="360px",
        ),
        width="100%",
    )
