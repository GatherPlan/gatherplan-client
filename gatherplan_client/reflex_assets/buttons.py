import reflex as rx

from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily


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
            width="340px",
        ),
        width="340px",
        height="76px",
        padding="20px",
        border_radius="15px",
        border="1px solid #F5F5F5",
        background_color=AppColor.BACKGROUND_GRAY_COLOR,
        on_click=rx.redirect(redirect_url),
    )


def basic_button(button_text: str = "", type: str = "submit"):
    return rx.button(
        button_text,
        width="348px",
        height="48px",
        padding="20px",
        color=AppColor.WHITE,
        type=type,
        background_color=AppColor.MAIN_BACKGROUND,
    )


def second_basic_button(button_text: str = "", type: str = "submit"):
    return rx.button(
        button_text,
        width="348px",
        height="48px",
        padding="20px",
        color=AppColor.WHITE,
        type=type,
        background_color=AppColor.LIGHT_GRAY_TEXT,
    )


def small_button(button_text: str = ""):
    return rx.button(
        button_text,
        width="110px",
        height="36px",
        color="#A3A3A3",
        type="button",
        background_color="#FFFFFF",
    )
