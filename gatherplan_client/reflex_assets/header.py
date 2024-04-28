import reflex as rx

from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily


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


def header(main_text: str, back_button_url: str):
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.button(
                    rx.icon(tag="chevron-left"),
                    color=AppColor.BLACK,
                    background_color=AppColor.WHITE,
                    on_click=rx.redirect(back_button_url),
                ),
                rx.text(
                    main_text,
                    color=AppColor.BLACK,
                    font_size=TextSize.SMALL_MEDIUM,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    height="40px",
                    font_weight="600",
                    background_color=AppColor.WHITE,
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
