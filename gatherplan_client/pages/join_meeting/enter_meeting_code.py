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
    need_login_type="no_login",
)
def enter_meeting_code() -> rx.Component:
    return rx.form(
        rx.vstack(
            main_sub_text_box("약속 코드", "12자리 영소문자입니다."),
            input_box(
                value=State.params_meeting_code,
                name="enter_code",
                type="text",
                on_change=State.set_meeting_code,
            ),
            rx.spacer(),
            main_button(text="다음", type="submit"),
            rx.text("test"),
            min_height="100vh",
            padding_bottom="210px",
            align="center",
        ),
        on_submit=State.enter_meeting_code_handle_submit,
        min_height="100vh",
        width="100%",
    )
