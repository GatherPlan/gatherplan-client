from typing import Dict

import reflex as rx

from gatherplan_client.check_meeting.check_state import CheckState
from gatherplan_client.login import LoginState
from gatherplan_client.make_meeting.make_meeting_state import MakeMeetingNameState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import AppColor, AppFontFamily


def check_login(func):
    def inner():
        return rx.cond(
            LoginState.login_token != "", check_meeting_not_logined(), func()
        )

    return inner


def list_view(items: Dict):
    return rx.hstack(
        rx.box(
            rx.text(
                items["meeting_name"],
                font_size="14px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.BLACK,
                padding_left="10px",
            ),
            rx.text(
                items["host_name"],
                font_size="12px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.GRAY_TEXT,
                padding_left="10px",
            ),
            width="140px",
            height="40px",
        ),
        rx.center(
            rx.text(
                items["meeting_notice"],
                font_size="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.GRAY_TEXT,
                padding_left="10px",
            ),
            width="160px",
            height="40px",
        ),
        rx.center(
            rx.text(
                items["meeting_state"],
                font_size="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.GREEN,
                padding_left="10px",
            ),
            height="40px",
        ),
    )


@check_login
def check_meeting() -> rx.Component:
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


def check_meeting_not_logined() -> rx.Component:
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
                        type="button",
                        height="35px",
                        width="50px",
                        background_color=AppColor.MAIN_COLOR,
                        font_size="12px",
                    ),
                    width="360px",
                )
            ),
            rx.scroll_area(
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.box(
                                rx.vstack(
                                    rx.text(
                                        "검색결과",
                                        font_size="12px",
                                        font_family=AppFontFamily.DEFAULT_FONT,
                                        font_weight="700",
                                        color=AppColor.SUB_TEXT,
                                        padding_left="10px",
                                    ),
                                    rx.foreach(CheckState.meeting_list, list_view),
                                ),
                                width="360px",
                            ),
                            width="100%",
                            align="center",
                            padding_top="20px",
                        ),
                        width="100%",
                    ),
                    direction="column",
                    spacing="4",
                ),
                type="scroll",
                scrollbars="vertical",
                style={"height": "70%"},
            ),
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
            on_submit=CheckState.handle_detail_submit,
            width="100%",
            align="center",
            height="70%",
        ),
        spacing="0",
        height="100vh",
    )
