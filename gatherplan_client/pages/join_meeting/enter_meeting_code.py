import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    input_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/enter_meeting_code",
    header_url="/",
    page_text="약속 참여하기",
    need_login_type="no_login",
)
def enter_meeting_code() -> rx.Component:
    return rx.form(
        rx.center(
            rx.vstack(
                main_sub_text_box("약속 코드", "12자리 영소문자입니다."),
                input_box(
                    value=State.params_meeting_code,
                    name="enter_code",
                    type="text",
                    on_change=State.set_meeting_code,
                ),
                rx.box(height="38vh"),
                main_button(text="다음", type="submit"),
                width="360px",
            ),
            width="100%",
        ),
        on_submit=State.enter_meeting_code_handle_submit,
        align="center",
        height="100%",
        width="100%",
    )
