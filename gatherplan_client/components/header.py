import reflex as rx

from gatherplan_client.components.schema import TextSize, AppColor, AppFontFamily


def main_header(main_text: str):
    return rx.center(
        main_text,
        color=AppColor.BLACK,
        font_size=TextSize.MEDIUM,
        font_family=AppFontFamily.DEFAULT_FONT,
        height="45px",
        width="100%",
        font_weight="600",
        background_color=AppColor.WHITE,
    )


def header(back_button_url: str):
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.button(
                    rx.icon(
                        tag="chevron-left",
                        size=24,
                        # color=AppColor.MAIN_COLOR,
                        stroke_width=3,
                    ),
                    color=AppColor.BLACK,
                    background_color=AppColor.WHITE,
                    on_click=rx.redirect(back_button_url),
                    padding="0px",
                ),
                rx.image(
                    src="/images/index_logo.png",
                    width="140px",
                    height="30px",
                    padding_top="2px",
                ),
                spacing="0",
            ),
            width="360px",
        ),
        width="100%",
        height="10%",
        align="center",
        padding_top="10px",
    )
