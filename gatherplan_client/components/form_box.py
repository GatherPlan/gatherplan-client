import reflex as rx

from gatherplan_client.components.schema import TextSize, AppFontFamily


def form_box(
    explain_text: str = "",
    explain_text_size: TextSize = TextSize.VERY_TINY,
    placeholder_text: str = "",
    form_value: str = "",
    placeholder_text_size: TextSize = TextSize.SMALL,
    form_box_height: str = "48px",
    type: str = "text",
):
    return rx.box(
        rx.text(
            explain_text,
            font_size=explain_text_size,
            font_family=AppFontFamily.DEFAULT_FONT,
        ),
        rx.input(
            placeholder=placeholder_text,
            name=form_value,
            font_size=placeholder_text_size,
            height=form_box_height,
            border_radius="35px",
            type=type,
        ),
        padding_bottom="20px",
        width="345px",
    )


def form_box_with_value(
    explain_text: str = "",
    explain_text_size: TextSize = TextSize.VERY_TINY,
    value: str = "",
    form_value: str = "",
    placeholder_text_size: TextSize = TextSize.SMALL,
    form_box_height: str = "48px",
    type: str = "text",
):
    return rx.box(
        rx.text(
            explain_text,
            font_size=explain_text_size,
            font_family=AppFontFamily.DEFAULT_FONT,
        ),
        rx.input(
            value=value,
            name=form_value,
            font_size=placeholder_text_size,
            height=form_box_height,
            border_radius="35px",
            type=type,
        ),
        padding_bottom="20px",
        width="345px",
    )


def form_box_with_button(
    explain_text: str = "",
    explain_text_size: TextSize = TextSize.VERY_TINY,
    placeholder_text: str = "",
    form_value: str = "",
    placeholder_text_size: TextSize = TextSize.SMALL,
    form_box_height: str = "48px",
    type: str = "text",
):
    return rx.box(
        rx.text(
            explain_text,
            font_size=explain_text_size,
            font_family=AppFontFamily.DEFAULT_FONT,
        ),
        rx.hstack(
            rx.input(
                placeholder=placeholder_text,
                name=form_value,
                font_size=placeholder_text_size,
                height=form_box_height,
                border_radius="35px",
                type=type,
                width="290px",
            ),
            rx.button(
                "인증요청",
                width="50px",
                height="48px",
            ),
            padding_bottom="20px",
            width="345px",
        ),
    )


rx.box(
    rx.text(
        "이메일",
        font_size="10px",
        font_family=AppFontFamily.DEFAULT_FONT,
    ),
    rx.hstack(
        rx.input(
            placeholder="2~8자리",
            name="email",
            font_size="16px",
            height="48px",
            border_radius="35px",
            type="text",
            width="290px",
        ),
        rx.button(
            "인증요청",
            width="50px",
            height="48px",
        ),
        padding_bottom="20px",
        width="345px",
    ),
),
