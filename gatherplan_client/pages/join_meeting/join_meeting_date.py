import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.calendar import display_select_date, calendar_header
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    sub_text_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting_date",
    header_url="/join_meeting",
    page_text="약속 참여하기",
)
def join_meeting_date() -> rx.Component:
    return rx.center(
        rx.vstack(
            main_sub_text_box(
                "약속 참여 일정", "참여가능한 날짜와 시간을 선택해주세요"
            ),
            calendar_header(),
            sub_text_box("선택한 일정"),
            rx.scroll_area(
                rx.flex(
                    rx.foreach(
                        State.display_select_date,
                        display_select_date,
                    ),
                    direction="column",
                    spacing="4",
                ),
                type="always",
                scrollbars="vertical",
                style={"height": 140, "width": 360},
            ),
            main_button(text="선택완료", on_click=rx.redirect("/join_meeting_check")),
            width="360px",
        ),
        width="100%",
    )
