import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting_state import MakeMeetingNameState
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.form_box import form_box
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize
from gatherplan_client.reflex_assets.text_box import left_align_text_box


@need_login
def enter_meeting_code() -> rx.Component:
    return rx.vstack(
        header("약속 참여하기"),
        left_align_text_box(
            "약속 코드를 입력해주세요",
            "약속 코드는 20자리 영소문자입니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    form_box(
                        explain_text="약속코드",
                        placeholder_text=MakeMeetingNameState.meeting_code,
                        form_value="enter_code",
                    ),
                    basic_button("다음"),
                    on_submit=MakeMeetingNameState.handle_submit,
                    align="center",
                    width="345px",
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
