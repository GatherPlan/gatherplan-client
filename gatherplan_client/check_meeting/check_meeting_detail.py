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
            rx.center(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger("Tab 1", value="tab1"),
                        rx.tabs.trigger("Tab 2", value="tab2"),
                    ),
                    rx.tabs.content(
                        rx.text("item on tab 1"),
                        value="tab1",
                    ),
                    rx.tabs.content(
                        rx.text("item on tab 2"),
                        value="tab2",
                    ),
                    width="100%",
                ),
                width="100%",
            ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )
