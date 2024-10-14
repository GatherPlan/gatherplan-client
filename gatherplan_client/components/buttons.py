import reflex as rx

from gatherplan_client.components.schema import TextSize, AppColor, AppFontFamily


def index_button(main_text: str, sub_text: str = "", redirect_url: str = ""):
    return rx.button(
        rx.vstack(
            rx.text(
                main_text,
                color=AppColor.BLACK,
                font_size=TextSize.SMALL,
                font_family=AppFontFamily.JALNAN_GOTHIC,
            ),
            rx.text(
                sub_text,
                color=AppColor.GRAY_TEXT,
                font_size=TextSize.TINY,
                font_family=AppFontFamily.JALNAN_GOTHIC,
            ),
            width="360px",
        ),
        width="360px",
        height="76px",
        padding="20px",
        border_radius="15px",
        border="1px solid #F5F5F5",
        background_color=AppColor.BACKGROUND_GRAY_COLOR,
        on_click=rx.redirect(redirect_url),
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


def calendar_button_component(text: str, **kwargs):
    return rx.button(
        text, width="45px", height="36px", font_size="16px", type="button", **kwargs
    )
