import reflex as rx

from gatherplan_client.reflex_assets.schema import TextSize, AppFontFamily, AppColor


def left_align_text_box(
    main_text: str,
    sub_text: str,
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
        height="20%",
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
