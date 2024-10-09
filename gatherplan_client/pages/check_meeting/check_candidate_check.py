import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
    main_sub_text_box,
    sub_text_box,
    main_text_box,
    main_button,
)
from gatherplan_client.templates.template import template


@template(
    route="/check_candidate_check",
    header_url="/check_candidate",
    page_text="",
)
def check_candidate_check() -> rx.Component:
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
                main_sub_text_box(
                    f"{State.confirm_date} {State.confirm_start_time} ~ {State.confirm_end_time}",
                    "선택된 약속 시간",
                    change_position=True,
                ),
            ),
            main_sub_text_box(State.meeting_notice, "공지사항", change_position=True),
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
            main_sub_text_box(
                State.meeting_confirm_display_data_user,
                "사용자 참여 목록",
                change_position=True,
            ),
            main_button("확정하기", on_click=State.check_candidate_check_handle_submit),
            width="360px",
        ),
        width="100%",
    )
