import reflex as rx

from gatherplan_client.join_meeting.join_state import JoinState
from gatherplan_client.make_meeting.make_meeting_state import MakeMeetingNameState
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.form_box import form_box, form_box_with_value
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppFontFamily, AppColor
from gatherplan_client.reflex_assets.text_box import left_align_text_box


def join_meeting_date() -> rx.Component:
    from gatherplan_client.make_meeting.make_meeting_date import location_button

    return rx.vstack(
        header("약속 참여하기", "/"),
        left_align_text_box(
            "참여할 약속 날짜를 선택해주세요",
            "호스트가 설정한 약속 날짜 중에서 참여할 날짜를 선택합니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                rx.center(
                    rx.button(
                        rx.icon(tag="chevron-left"),
                        on_click=MakeMeetingNameState.month_decrement,
                        width="48px",
                        height="40px",
                        color=AppColor.BLACK,
                        background_color=AppColor.WHITE,
                    ),
                    rx.center(
                        MakeMeetingNameState.setting_time_display,
                        width="100px",
                        height="40px",
                        align="center",
                    ),
                    rx.button(
                        rx.icon(tag="chevron-right"),
                        on_click=MakeMeetingNameState.month_increment,
                        width="48px",
                        height="40px",
                        color=AppColor.BLACK,
                        background_color=AppColor.WHITE,
                    ),
                    color=AppColor.BLACK,
                    font_size=TextSize.SMALL_MEDIUM,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    height="40px",
                    width="100%",
                    font_weight="600",
                    background_color=AppColor.WHITE,
                ),
                rx.center(
                    rx.grid(
                        rx.center("일", color=AppColor.RED, width="50px"),
                        rx.center("월", width="50px"),
                        rx.center("화", width="50px"),
                        rx.center("수", width="50px"),
                        rx.center("목", width="50px"),
                        rx.center("금", width="50px"),
                        rx.center("토", color=AppColor.BLUE, width="50px"),
                        rx.foreach(
                            MakeMeetingNameState.display_data,
                            location_button,
                        ),
                        columns="7",
                        align="center",
                        width="360px",
                    ),
                    width="100%",
                ),
                buffer_box("5%"),
                rx.center(
                    rx.button(
                        "다음",
                        width="348px",
                        height="48px",
                        padding="20px",
                        color=AppColor.WHITE,
                        type="submit",
                        background_color=AppColor.MAIN_BACKGROUND,
                        on_click=rx.redirect("/make_meeting_time"),
                    ),
                    width="100%",
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
