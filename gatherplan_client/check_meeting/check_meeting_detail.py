import reflex as rx

from gatherplan_client.check_meeting.check_state import CheckState
from gatherplan_client.login import LoginState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import AppColor, AppFontFamily


def check_login(func):
    def inner():
        return rx.cond(
            LoginState.login_token != "", check_meeting_detail_not_logined(), func()
        )

    return inner


@check_login
def check_meeting_detail() -> rx.Component:
    return rx.vstack(
        header("/"),
        rx.center(
            rx.text(
                "약속 현황보기",
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
        spacing="0",
        height="100vh",
    )


def check_meeting_detail_not_logined() -> rx.Component:
    return rx.vstack(
        header("/check_meeting"),
        rx.center(
            rx.text(
                CheckState.detail_meeting_name,
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
                        "약속 목록",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        padding_left="10px",
                        color=AppColor.BLACK,
                        width="360px",
                    ),
                    rx.text(
                        "약속 이름 또는 호스트 이름을 검색해보세요",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_left="10px",
                        padding_bottom="5px",
                        width="360px",
                    ),
                    align="center",
                    width="100%",
                ),
            ),
            rx.center(
                rx.hstack(
                    rx.box(
                        rx.input(
                            placeholder="홍길동",
                            name="location",
                            font_size="10px",
                            height="35px",
                            border_radius="35px",
                            type="text",
                        ),
                        padding_bottom="20px",
                        padding_left="10px",
                        width="300px",
                    ),
                    rx.button(
                        "검색",
                        height="35px",
                        width="50px",
                        background_color=AppColor.MAIN_COLOR,
                        type="submit",
                        font_size="12px",
                    ),
                    width="360px",
                )
            ),
            on_submit=CheckState.handle_detail_submit,
            width="100%",
            align="center",
            height="70%",
        ),
        spacing="0",
        height="100vh",
    )
