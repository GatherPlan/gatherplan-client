from typing import Dict

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.pages.login.login import need_login


def list_view(items: Dict):
    return rx.button(
        rx.hstack(
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
        ),
        background_color=AppColor.WHITE,
        border="1px solid #D9D9D9",
        border_radius="10px",
        height="50px",
        width="360px",
        padding="0px",
        on_click=State.check_appointments_detail(items["meeting_code"]),
    )


@need_login
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
                            name="keyword",
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
                                    rx.foreach(State.check_meeting_list, list_view),
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
            on_submit=State.check_get_appointments_search,
            width="100%",
            align="center",
            height="70%",
        ),
        spacing="0",
        height="100vh",
    )
