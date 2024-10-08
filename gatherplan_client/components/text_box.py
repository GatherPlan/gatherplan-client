import reflex as rx

from gatherplan_client.components.schema import TextSize, AppFontFamily, AppColor


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
            ),
            rx.center(
                sub_text,
                font_size=sub_font_size,
                font_family=AppFontFamily.DEFAULT_FONT,
                color=AppColor.GRAY_TEXT,
                font_weight="700",
            ),
            width="360px",
        ),
        width="100%",
        height="20%",
        align="center",
        padding_top="20px",
    )


def text_for_each(text: str):
    return rx.text(
        text,
        font_size="14px",
        font_family=AppFontFamily.DEFAULT_FONT,
        color=AppColor.BLACK,
        font_weight="700",
    )


def main_text_box(text: str):
    return rx.text(
        text,
        font_size=TextSize.TINY_SMALL,
        font_family=AppFontFamily.DEFAULT_FONT,
        font_weight="700",
        color=AppColor.BLACK,
    )


def main_text_box_center(text: str):
    return rx.text(
        text,
        font_size="18px",
        font_family=AppFontFamily.DEFAULT_FONT,
        font_weight="700",
        color=AppColor.BLACK,
        align="center",
        width="360px",
    )


def sub_text_box_center(text: str):
    return rx.text(
        text,
        font_size="12px",
        font_family=AppFontFamily.DEFAULT_FONT,
        color=AppColor.GRAY_TEXT,
        font_weight="700",
        align="center",
        width="360px",
    )


def sub_text_box(text: str):
    return rx.text(
        text,
        font_size=TextSize.TINY,
        font_family=AppFontFamily.DEFAULT_FONT,
        color=AppColor.GRAY_TEXT,
        font_weight="700",
    )


def main_sub_text_box(main_text: str, sub_text: str, change_position: bool = False):
    if change_position:
        return rx.vstack(
            sub_text_box(sub_text),
            main_text_box(main_text),
            width="360px",
        )
    return rx.vstack(
        main_text_box(main_text),
        sub_text_box(sub_text),
        width="360px",
    )


def main_sub_text_center_box(main_text: str, sub_text: str):
    return rx.vstack(
        main_text_box_center(main_text),
        sub_text_box_center(sub_text),
        width="360px",
    )


def main_button(text: str, sub_button: bool = False, **kwargs):
    if sub_button:
        return rx.button(
            text,
            width="360px",
            height="35px",
            color=AppColor.BLACK,
            background_color=AppColor.SUB_TEXT,
            **kwargs,
        )

    return rx.button(
        text,
        width="360px",
        height="35px",
        color=AppColor.WHITE,
        background_color=AppColor.MAIN_COLOR,
        **kwargs,
    )


def input_box(**kwargs):
    return rx.box(
        rx.input(
            font_family=AppFontFamily.DEFAULT_FONT,
            font_size="12px",
            height="35px",
            **kwargs,
        ),
        width="360px",
        height="60px",
    )
