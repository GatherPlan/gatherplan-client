import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.schema import AppColor, AppFontFamily, TextSize
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    sub_text_box,
    main_text_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting",
    header_url="/enter_meeting_code",
    page_text="약속 정보",
    need_login_type="no_login",
)
def join_meeting() -> rx.Component:
    return rx.center(
        rx.vstack(
            main_sub_text_box(State.meeting_name, "약속 이름", change_position=True),
            rx.cond(
                State.meeting_location_detail != "",
                rx.box(
                    sub_text_box("약속장소"),
                    rx.link(
                        State.meeting_location,
                        href=State.place_url,
                        font_size=TextSize.TINY_SMALL,
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.SKY_BLUE,
                    ),
                    sub_text_box(State.meeting_location_detail),
                ),
                rx.box(),
            ),
            rx.cond(
                State.meeting_notice != "",
                main_sub_text_box(
                    State.meeting_notice, "공지사항", change_position=True
                ),
                rx.box(),
            ),
            rx.box(
                sub_text_box("약속 후보 날짜"),
                rx.scroll_area(
                    rx.grid(
                        rx.foreach(State.meeting_date, main_text_box),
                        columns="3",
                        width="100%",
                    ),
                    type="auto",
                    scrollbars="vertical",
                    style={"height": 80, "width": 360},
                ),
            ),
            rx.box(
                rx.hstack(
                    sub_text_box("약속코드"),
                    rx.button(
                        rx.icon("copy"),
                        on_click=State.paste_meeting_code(State.meeting_code),
                        width="12px",
                        height="12px",
                        padding="0",
                        color=AppColor.GRAY_TEXT,
                        background_color=AppColor.WHITE,
                    ),
                ),
                main_text_box(State.meeting_code),
            ),
            main_sub_text_box(State.host_name, "모임장", change_position=True),
            main_button(
                text="참여하기",
                type="button",
                on_click=State.join_meeting_handle_submit,
            ),
            width="360px",
            spacing="5",
        ),
        width="100%",
    )
