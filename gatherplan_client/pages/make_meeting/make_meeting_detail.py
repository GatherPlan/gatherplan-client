from typing import Dict

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.components.text_box import main_sub_text_box, input_box
from gatherplan_client.templates.template import template


def location_button(button_text: Dict):
    return rx.cond(
        button_text["location_type"] == "DETAIL_ADDRESS",
        rx.drawer.close(
            rx.button(
                rx.vstack(
                    rx.text(button_text["place_name"]),
                    rx.text(button_text["address_name"], font_size="10px"),
                    spacing="0",
                    align="center",
                    width="360px",
                ),
                width="360px",
                height="48px",
                color="#A3A3A3",
                type="button",
                on_click=State.make_meeting_detail_handle_location_submit(button_text),
                background_color="#FFFFFF",
            )
        ),
        rx.drawer.close(
            rx.button(
                button_text["address_name"],
                width="360px",
                height="36px",
                color="#A3A3A3",
                type="button",
                on_click=State.make_meeting_detail_handle_location_submit(button_text),
                background_color="#FFFFFF",
            ),
        ),
    )


@template(
    route="/make_meeting_detail", page_text="약속 만들기", header_url="/make_meeting"
)
def make_meeting_detail() -> rx.Component:
    return rx.form(
        rx.center(
            rx.vstack(
                main_sub_text_box(
                    "약속 장소", "행정구역 또는 장소 이름으로 검색합니다"
                ),
                rx.hstack(
                    input_box(
                        on_blur=State.set_input_location,
                        placeholder="약속장소를 입력해주세요",
                        name="location",
                        type="text",
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
                rx.cond(
                    State.meeting_location_detail != "",
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.text(
                                    "선택한 장소",
                                    font_size="12px",
                                    font_family=AppFontFamily.DEFAULT_FONT,
                                    font_weight="700",
                                    color=AppColor.SUB_TEXT,
                                ),
                                rx.cond(
                                    State.location_type == "DISTRICT",
                                    rx.hstack(
                                        rx.text(
                                            State.meeting_location_detail,
                                            font_size="14px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color=AppColor.BLACK,
                                            width="280px",
                                        ),
                                        rx.text(
                                            "행정구역",
                                            font_size="12px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color="#6D6D6D",
                                            padding_top="2px",
                                            width="80",
                                        ),
                                    ),
                                    rx.hstack(
                                        rx.vstack(
                                            rx.text(
                                                State.meeting_location,
                                                font_size="14px",
                                                font_family=AppFontFamily.DEFAULT_FONT,
                                                font_weight="700",
                                                color=AppColor.BLACK,
                                                width="280px",
                                            ),
                                            rx.text(
                                                State.meeting_location_detail,
                                                font_size="10px",
                                                font_family=AppFontFamily.DEFAULT_FONT,
                                                font_weight="700",
                                                color=AppColor.BLACK,
                                                width="280px",
                                            ),
                                        ),
                                        rx.text(
                                            "상세주소",
                                            font_size="12px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color="#6D6D6D",
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
                    rx.box(width="100%", height="98px"),
                ),
                rx.box(width="100%", height="33vh"),
                rx.button(
                    "다음",
                    width="360px",
                    height="35px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_COLOR,
                ),
                width="360px",
            ),
        ),
        on_submit=rx.redirect("/make_meeting_date"),
        width="100%",
        align="center",
        height="100%",
    )
