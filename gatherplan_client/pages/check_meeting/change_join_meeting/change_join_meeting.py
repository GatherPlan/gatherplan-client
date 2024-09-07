import reflex as rx

from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.pages.login.login import need_login


@need_login
def change_join_meeting(login_token, nick_name) -> rx.Component:
    return rx.vstack(
        header("/check_meeting_detail"),
        rx.center(
            rx.text(
                "약속 확정하기",
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
                    "약속 시간 후보 목록",
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    padding_left="10px",
                    color=AppColor.BLACK,
                    width="360px",
                ),
                rx.text(
                    "참여율, 약속 구간 길이, 날씨를 기준으로 정렬된 결과가 반환됩니다.",
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
            width="100%",
        ),
        rx.center(
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
