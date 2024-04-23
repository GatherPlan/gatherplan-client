from typing import Any

import reflex as rx

from gatherplan_client.reflex_assets.schema import TextSize, AppFontFamily, AppColor


def left_align_text_box(
    main_text: str,
    sub_text: str,
    height: str = "20%",
    main_font_size: TextSize = TextSize.MEDIUM,
    sub_font_size: TextSize = TextSize.SMALL,
):
    return rx.vstack(
        rx.box(
            rx.vstack(
                rx.text(
                    main_text,
                    font_size=main_font_size,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_left="10px",
                ),
                rx.text(
                    sub_text,
                    font_size=sub_font_size,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                    padding_left="10px",
                ),
            ),
            width="360px",
        ),
        width="100%",
        height=height,
        align="center",
        padding_top="20px",
    )


def center_align_text_box(
    main_text: str,
    sub_text: str,
    main_font_size: TextSize = TextSize.MEDIUM,
    sub_font_size: TextSize = TextSize.TINY,
):
    return rx.vstack(
        rx.box(
            rx.center(
                main_text,
                font_size=main_font_size,
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.BLACK,
                padding_left="10px",
            ),
            rx.center(
                sub_text,
                font_size=sub_font_size,
                font_family=AppFontFamily.DEFAULT_FONT,
                color=AppColor.GRAY_TEXT,
                font_weight="700",
                padding_left="10px",
            ),
            width="360px",
        ),
        width="100%",
        height="20%",
        align="center",
        padding_top="20px",
    )


def check_meeting_box(text1: str, text2: Any, text3: Any = ""):
    return rx.box(
        rx.hstack(
            rx.text(
                text1,
                font_size=TextSize.SMALL,
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.BLACK,
                padding_left="10px",
                width="120px",
            ),
            rx.box(
                rx.vstack(
                    rx.text(
                        text2,
                        font_size=TextSize.SMALL,
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_right="20px",
                        align="right",
                        width="230px",
                    ),
                    rx.text(
                        text3,
                        font_size=TextSize.SMALL,
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_right="20px",
                        align="right",
                        width="230px",
                    ),
                ),
            ),
        ),
        border_bottom="1px solid #E0E0E0",
        padding="5px",
        width="360px",
    )


def check_meeting_box_for_each(text1: str, text2: Any):
    return rx.box(
        rx.hstack(
            rx.text(
                text1,
                font_size=TextSize.SMALL,
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.BLACK,
                padding_left="10px",
                width="120px",
            ),
            rx.box(
                rx.vstack(rx.foreach(text2, text_for_each)),
            ),
        ),
        border_bottom="1px solid #E0E0E0",
        padding="5px",
        width="360px",
    )


def text_for_each(text: str):
    return rx.text(
        text,
        font_size=TextSize.SMALL,
        font_family=AppFontFamily.DEFAULT_FONT,
        color=AppColor.GRAY_TEXT,
        font_weight="700",
        padding_right="20px",
        align="right",
        width="230px",
    )
