import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor
from gatherplan_client.reflex_assets.text_box import (
    left_align_text_box,
    check_meeting_box,
    check_meeting_box_for_each,
)


@need_login
def make_meeting_check() -> rx.Component:
    return rx.vstack(
        header("약속만들기", "/make_meeting_time"),
        left_align_text_box(
            "약속 정보를 확인해주세요",
            "약속 정보 수정은 현황보기에서 진행할 수 있습니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
            height="15%",
        ),
        rx.center(
            rx.scroll_area(
                rx.center(
                    check_meeting_box("약속이름", MakeMeetingNameState.meeting_name),
                    check_meeting_box(
                        "약속장소",
                        MakeMeetingNameState.select_location,
                        MakeMeetingNameState.select_location_detail_location,
                    ),
                    check_meeting_box_for_each(
                        "약속날짜",
                        MakeMeetingNameState.select_data,
                    ),
                    check_meeting_box_for_each(
                        "약속 후보 시간",
                        MakeMeetingNameState.select_time,
                    ),
                    direction="column",
                    spacing="3",
                ),
                type="scroll",
                scrollbars="vertical",
                style={
                    "width": "360px",
                    "padding": "10px",
                },
            ),
            width="100%",
            height="60%",
        ),
        buffer_box("5%"),
        rx.center(
            rx.button(
                "약속 만들기",
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_BACKGROUND,
                on_click=MakeMeetingNameState.handle_result_submit,
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
