import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
    main_sub_text_box,
    sub_text_box,
    main_text_box,
)
from gatherplan_client.pages.join_meeting.join_meeting_date import display_select_date
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting_result",
    header_url="/",
    page_text="",
)
def join_meeting_result() -> rx.Component:
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
                sub_text_box("약속장소"),
                rx.link(
                    State.meeting_location_detail,
                    href=State.place_url,
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_bottom="5px",
                ),
                rx.text(
                    State.meeting_location,
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="500",
                    color=AppColor.GRAY_TEXT,
                    margin="0",
                    padding="0",
                ),
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
                    type="always",
                    scrollbars="vertical",
                    style={"height": 70, "width": 360},
                ),
                main_sub_text_box(
                    State.meeting_notice, "공지사항", change_position=True
                ),
                rx.hstack(
                    sub_text_box("약속코드"),
                    rx.button(
                        rx.icon("copy"),
                        on_click=rx.set_clipboard(State.meeting_code),
                        width="12px",
                        height="12px",
                        padding="0",
                        color=AppColor.GRAY_TEXT,
                        background_color=AppColor.WHITE,
                    ),
                ),
                main_text_box(State.meeting_code),
                main_sub_text_box(State.host_name, "모임장", change_position=True),
                main_button(
                    text="약속 현황보기", on_click=rx.redirect("/check_meeting")
                ),
            ),
            width="360px",
        ),
        width="100%",
    )
