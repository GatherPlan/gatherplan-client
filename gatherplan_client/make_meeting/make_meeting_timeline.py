import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.reflex_assets.buttons import make_meeting_time_button
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize
from gatherplan_client.reflex_assets.text_box import left_align_text_box


@need_login
def make_meeting_time() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속 시간대를 골라주세요",
            "사용자 지정은 중복 선택이 불가합니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                make_meeting_time_button(main_text="오전", sub_text="06:00 ~ 12:00"),
                make_meeting_time_button(main_text="오후", sub_text="12:00 ~ 18:00"),
                make_meeting_time_button(main_text="저녁", sub_text="18:00 ~ 24:00"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
