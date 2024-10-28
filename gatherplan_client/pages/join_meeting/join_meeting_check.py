import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.calendar import display_select_date
from gatherplan_client.components.schema import AppColor, AppFontFamily, TextSize
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
    main_sub_text_box,
    sub_text_box,
    main_text_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting_check",
    header_url="/join_meeting_date",
    page_text="",
)
def join_meeting_check() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                main_sub_text_center_box(
                    "선택한 약속 참여 일정을 확인해주세요.",
                    "참여하기를 눌러 약속 참여를 완료주세요.",
                ),
            ),
            rx.vstack(
                main_sub_text_box(State.meeting_name, "약속이름", change_position=True),
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
                rx.box(
                    sub_text_box("선택한 일정"),
                    rx.scroll_area(
                        rx.grid(
                            rx.foreach(
                                State.display_select_date,
                                display_select_date,
                            ),
                            columns="1",
                            width="360px",
                        ),
                        type="auto",
                        scrollbars="vertical",
                        style={"height": 120, "width": 360},
                    ),
                ),
                main_button(
                    text="참여하기",
                    on_click=State.join_meeting_check_handle_result_submit,
                ),
                spacing="5",
            ),
            width="360px",
        ),
        width="100%",
    )
