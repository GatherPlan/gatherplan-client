import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
    sub_text_box,
    text_for_each,
    main_sub_text_box,
)
from gatherplan_client.templates.template import template


@template(route="/make_meeting_check", header_url="/make_meeting_date", page_text="")
def make_meeting_check() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                main_sub_text_center_box(
                    "선택한 약속 정보를 확인해주세요",
                    "약속 정보 변경은 약속 현황보기에서 가능합니다.",
                ),
            ),
            rx.vstack(
                main_sub_text_box(State.meeting_name, "약속이름", change_position=True),
                sub_text_box("약속장소"),
                rx.link(
                    State.meeting_location,
                    href=State.place_url,
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_bottom="5px",
                ),
                sub_text_box(State.meeting_location_detail),
                sub_text_box("약속 후보 날짜"),
                rx.scroll_area(
                    rx.grid(
                        rx.foreach(State.select_data, text_for_each),
                        columns="3",
                        width="100%",
                    ),
                    type="always",
                    scrollbars="vertical",
                    style={"height": 70, "width": 360},
                ),
                main_sub_text_box(
                    State.meeting_notice, "공지사항", change_position=True
                ),
                rx.button(
                    "약속 만들기",
                    width="360px",
                    height="35px",
                    padding="20px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_COLOR,
                    on_click=State.make_meeting_check_handle_submit,
                ),
            ),
            width="360px",
        ),
        width="100%",
    )
