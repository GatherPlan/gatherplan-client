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
    check_meeting_box_with_clipboard,
)


@need_login
def make_meeting_result() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속이 생성되었습니다.",
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
                    check_meeting_box_with_clipboard(
                        "약속 코드", MakeMeetingNameState.meeting_code
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
            height="55%",
        ),
        rx.center(
            rx.vstack(
                rx.button(
                    "약속 만들기",
                    width="348px",
                    height="48px",
                    padding="20px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_BACKGROUND,
                    on_click=rx.redirect("/enter_meeting_code"),
                ),
                rx.button(
                    "공유하기",
                    disabled=True,
                    width="348px",
                    height="48px",
                    padding="20px",
                    color=AppColor.BLACK,
                    type="submit",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
