import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    input_box,
)
from gatherplan_client.templates.template import template


@template(route="/make_meeting", page_text="약속 만들기", header_url="/")
def make_meeting() -> rx.Component:
    return rx.form(
        rx.center(
            rx.vstack(
                main_sub_text_box(
                    "약속 이름",
                    "상대방이 이해하기 좋은 이름으로 만들어요!",
                    need_start=True,
                ),
                input_box(
                    placeholder="약속이름을 입력해주세요",
                    name="meeting_name",
                ),
                main_sub_text_box(
                    "공지사항", "참여자에게 알려줄 내용을 간단히 작성해보세요!"
                ),
                input_box(
                    placeholder="선택사항",
                    name="meeting_memo",
                ),
                rx.text(height="28vh"),
                main_button(text="다음", type="submit"),
                width="360px",
            ),
            width="100%",
        ),
        on_submit=State.make_meeting_handle_submit,
        width="100%",
        height="100%",
        align="center",
    )
