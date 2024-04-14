import reflex as rx

from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily


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
