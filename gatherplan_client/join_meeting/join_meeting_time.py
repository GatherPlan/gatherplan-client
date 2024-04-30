import reflex as rx

from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize
from gatherplan_client.reflex_assets.text_box import (
    left_align_text_box,
)


def join_meeting_time() -> rx.Component:
    return rx.vstack(
        header("약속 참여하기", "/join_meeting_date"),
        left_align_text_box(
            "참여할 약속 시간을 정해주세요",
            "--",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
            height="15%",
        ),
        # Time Slot 구현 필요
        spacing="0",
        height="100vh",
    )
