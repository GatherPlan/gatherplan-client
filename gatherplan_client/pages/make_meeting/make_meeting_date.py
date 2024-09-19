import reflex as rx

from gatherplan_client.components.calendar import calendar_header
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.pages.login.login import need_login


@need_login
def make_meeting_date() -> rx.Component:
    return rx.vstack(
        header("/make_meeting_detail"),
        rx.center(
            rx.text(
                "약속 만들기",
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
        rx.center(
            rx.vstack(
                rx.text(
                    "약속 후보 날짜",
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_left="10px",
                ),
                rx.text(
                    "최대 10일까지 선택가능합니다.",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                    padding_left="10px",
                    padding_top="5px",
                ),
                width="360px",
            ),
            width="100%",
        ),
        calendar_header(purpose="make", height="55%"),
        rx.center(
            rx.button(
                "다음",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=rx.redirect("/make_meeting_check"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
