import reflex as rx

from gatherplan_client.join_meeting.join_state import JoinState
from gatherplan_client.make_meeting.make_meeting_state import MakeMeetingNameState
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppFontFamily
from gatherplan_client.reflex_assets.text_box import left_align_text_box


def enter_meeting_code() -> rx.Component:
    return rx.vstack(
        header("/"),
        left_align_text_box(
            "약속 코드를 입력해주세요",
            "약속 코드는 20자리 영소문자입니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    rx.box(
                        rx.text(
                            "약속코드",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                        ),
                        rx.input(
                            value=MakeMeetingNameState.meeting_code,
                            name="enter_code",
                            font_size=AppFontFamily.DEFAULT_FONT,
                            height="48px",
                            border_radius="35px",
                            type="text",
                            on_change=MakeMeetingNameState.set_meeting_code,
                        ),
                        padding_bottom="20px",
                        width="345px",
                    ),
                    basic_button("다음"),
                    on_submit=JoinState.handle_submit,
                    align="center",
                    width="345px",
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
