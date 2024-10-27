import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.text_box import (
    input_box,
    main_sub_text_box,
    main_sub_text_center_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting_change_nickname",
    header_url="/",
    page_text="",
)
def join_meeting_change_nickname() -> rx.Component:

    return rx.center(
        rx.vstack(
            rx.vstack(
                main_sub_text_center_box(
                    "사용할 수 없는 닉네임입니다.",
                    "약속에 참여할 새로운 닉네임을 설정해주세요.",
                ),
            ),
            rx.box(height="5vh"),
            rx.form(
                rx.vstack(
                    main_sub_text_box(
                        "닉네임",
                        "2자 이상, 6자 이하여야 합니다.",
                        need_start=True,
                    ),
                    input_box(
                        placeholder="닉네임을 입력해주세요",
                        name="nick_name",
                    ),
                    rx.box(height="35vh"),
                    main_button(
                        text="다음",
                        type="submit",
                    ),
                    spacing="5",
                ),
                on_submit=State.join_meeting_change_nickname_handle_submit,
                width="100%",
                height="100%",
                align="center",
            ),
            width="360px",
        ),
        width="100%",
    )
