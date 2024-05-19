from typing import Dict, List

import reflex as rx

from gatherplan_client.join_meeting.join_state import JoinState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppFontFamily, AppColor
from gatherplan_client.reflex_assets.text_box import (
    left_align_text_box,
)


def join_meeting_time() -> rx.Component:
    return rx.vstack(
        header("/join_meeting_date"),
        left_align_text_box(
            "참여할 약속 시간을 정해주세요",
            "--",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
            height="15%",
        ),
        # Time Slot 구현 필요
        rx.center(
            rx.scroll_area(
                rx.center(
                    rx.hstack(
                        rx.center(
                            "약속날짜",
                            width="180px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_size=TextSize.SMALL,
                            font_weight="700",
                        ),
                        rx.center(
                            "약속 시간",
                            width="180px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_size=TextSize.SMALL,
                            font_weight="700",
                        ),
                        spacing="0",
                    ),
                    rx.box(
                        rx.foreach(
                            JoinState.joiner_set_meeting_time,
                            text_for_each,
                        ),
                        border_bottom="1px solid #E0E0E0",
                        width="360px",
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
            width="360px",
            height="60%",
        ),
        spacing="0",
        height="100vh",
    )


def text_for_each(dict_data: Dict[str, List[str]]):
    return rx.hstack(
        rx.center(
            dict_data[0],
            width="180px",
            font_family=AppFontFamily.DEFAULT_FONT,
            font_size=TextSize.SMALL,
            font_weight="700",
        ),
        rx.vstack(rx.foreach(dict_data[1], custom_button), width="180px"),
    )


def custom_button(text: str):
    return rx.button(
        text,
        width="180px",
        height="30px",
        font_size=TextSize.SMALL,
        font_family=AppFontFamily.DEFAULT_FONT,
        color=AppColor.GRAY_TEXT,
        font_weight="700",
        padding_bottom="20px",
        align="center",
    )
