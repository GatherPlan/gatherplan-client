from typing import Dict

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.pages.login.login import need_login


def location_button(button_text: Dict):
    return rx.drawer.close(
        rx.button(
            button_text["address_name"],
            width="340px",
            height="36px",
            color="#A3A3A3",
            type="button",
            on_click=State.make_meeting_detail_handle_location_submit(button_text),
            background_color="#FFFFFF",
        ),
    )


@need_login
def make_meeting_detail() -> rx.Component:
    return rx.vstack(
        header("/make_meeting"),
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
        rx.form(
            rx.center(
                rx.vstack(
                    rx.text(
                        "약속 장소",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        padding_left="10px",
                        color=AppColor.BLACK,
                        width="360px",
                    ),
                    rx.text(
                        "행정구역 또는 장소 이름으로 검색합니다.",
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
                            on_blur=State.set_input_location,
                            placeholder="약속장소를 입력해주세요",
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
                    rx.drawer.root(
                        rx.drawer.trigger(
                            rx.button(
                                "검색",
                                type="button",
                                height="35px",
                                width="50px",
                                background_color=AppColor.MAIN_COLOR,
                                font_size="12px",
                                on_click=State.search_location_info,
                            )
                        ),
                        rx.drawer.overlay(z_index="5"),
                        rx.drawer.portal(
                            rx.drawer.content(
                                rx.center(
                                    rx.tabs.root(
                                        rx.tabs.list(
                                            rx.tabs.trigger(
                                                "행정구역", value="tab1", width="174px"
                                            ),
                                            rx.tabs.trigger(
                                                "상세주소", value="tab2", width="174px"
                                            ),
                                            font_size="16px",
                                        ),
                                        rx.tabs.content(
                                            rx.grid(
                                                rx.foreach(
                                                    State.search_location,
                                                    location_button,
                                                ),
                                                columns="1",
                                            ),
                                            value="tab1",
                                        ),
                                        rx.tabs.content(
                                            rx.grid(
                                                rx.foreach(
                                                    State.search_location_place,
                                                    location_button,
                                                ),
                                                columns="1",
                                            ),
                                            value="tab2",
                                        ),
                                        default_value="tab1",
                                        width="360px",
                                        height="100%",
                                    ),
                                    width="100%",
                                ),
                                align="center",
                                top="auto",
                                right="auto",
                                height="60%",
                                width="100%",
                                padding="2em",
                                background_color="#FFF",
                                border_radius="2em 2em 0 0",
                            )
                        ),
                        direction="bottom",
                    ),
                    width="360px",
                ),
            ),
            rx.center(
                rx.cond(
                    State.select_location_detail_location != "",
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "선택한 장소",
                                    font_size="12px",
                                    font_family=AppFontFamily.DEFAULT_FONT,
                                    font_weight="700",
                                    color=AppColor.SUB_TEXT,
                                    padding_left="10px",
                                ),
                                rx.cond(
                                    State.location_type == "DISTRICT",
                                    rx.hstack(
                                        rx.text(
                                            State.select_location_detail_location,
                                            font_size="14px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color=AppColor.BLACK,
                                            padding_left="10px",
                                            width="280px",
                                        ),
                                        rx.text(
                                            "행정구역",
                                            font_size="12px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color="#6D6D6D",
                                            padding_left="10px",
                                            padding_top="2px",
                                            width="80",
                                        ),
                                    ),
                                    rx.hstack(
                                        rx.vstack(
                                            rx.text(
                                                State.select_location,
                                                font_size="14px",
                                                font_family=AppFontFamily.DEFAULT_FONT,
                                                font_weight="700",
                                                color=AppColor.BLACK,
                                                padding_left="10px",
                                                width="280px",
                                            ),
                                            rx.text(
                                                State.select_location_detail_location,
                                                font_size="10px",
                                                font_family=AppFontFamily.DEFAULT_FONT,
                                                font_weight="700",
                                                color=AppColor.BLACK,
                                                padding_left="10px",
                                                width="280px",
                                            ),
                                        ),
                                        rx.text(
                                            "상세주소",
                                            font_size="12px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color="#6D6D6D",
                                            padding_left="10px",
                                            padding_top="2px",
                                            width="80",
                                        ),
                                    ),
                                ),
                            ),
                            width="360px",
                        ),
                        width="100%",
                        align="center",
                        padding_top="20px",
                    ),
                    rx.box(),
                ),
                width="100%",
            ),
            rx.box(width="100%", height="50%"),
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
            on_submit=State.make_meeting_detail_handle_detail_submit,
            width="100%",
            align="center",
            height="70%",
        ),
        spacing="0",
        height="100vh",
    )
