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
