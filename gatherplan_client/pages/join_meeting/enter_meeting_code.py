import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily, AppColor


@rx.page("/enter_meeting_code")
def enter_meeting_code() -> rx.Component:
    return rx.vstack(
        header("/"),
        rx.center(
            rx.text(
                "약속 참여하기",
                font_size="20px",
                padding_top="28px",
                padding_bottom="40px",
                padding_left="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                width="360px",
            ),
            width="100%",
            height="15%",
        ),
        rx.form(
            rx.center(
                rx.vstack(
                    rx.text(
                        "약속 코드",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                        padding_left="10px",
                    ),
                    rx.text(
                        "12자리 영소문자입니다.",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_left="10px",
                        padding_top="5px",
                    ),
                    rx.box(
                        rx.input(
                            value=State.params_meeting_code,
                            name="enter_code",
                            font_size=AppFontFamily.DEFAULT_FONT,
                            height="35px",
                            border_radius="35px",
                            type="text",
                            on_change=State.set_meeting_code,
                        ),
                        width="348px",
                        padding_top="10px",
                        padding_left="10px",
                        height="60px",
                    ),
                    width="360px",
                ),
                width="100%",
            ),
            rx.box(width="100%", height="60%"),
            rx.center(
                rx.button(
                    "다음",
                    width="348px",
                    height="35px",
                    padding_left="10px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_COLOR,
                ),
                width="100%",
            ),
            on_submit=State.join_meeting_handle_submit,
            align="center",
            height="80%",
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
