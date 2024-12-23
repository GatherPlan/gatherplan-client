import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    input_box,
)
from gatherplan_client.templates.template import template
from gatherplan_client.components.make_meeting_detail_location import location_button
from gatherplan_client.components.schema import AppColor
from gatherplan_client.components.calendar import calendar_header
from gatherplan_client.components.text_box import sub_text_box, main_text_box


@template(
    route="/make_meeting",
    need_login_type="need_login_check_meeting",
    on_load=State.setting_month_calendar,
)
def make_meeting() -> rx.Component:
    return rx.form(
        rx.center(
            rx.vstack(
                main_sub_text_box(
                    "약속 이름",
                    "상대방이 이해하기 좋은 이름으로 만들어요!",
                    need_start=True,
                ),
                input_box(
                    placeholder="약속이름을 입력해주세요",
                    name="meeting_name",
                ),
                main_sub_text_box(
                    "공지사항", "참여자에게 알려줄 내용을 간단히 작성해보세요!"
                ),
                input_box(
                    placeholder="선택사항",
                    name="meeting_memo",
                ),
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
                                    font_weight="700",
                                    color=AppColor.SUB_TEXT,
                                ),
                                rx.cond(
                                    State.location_type == "DISTRICT",
                                    rx.hstack(
                                        rx.text(
                                            State.meeting_location_detail,
                                            font_size="14px",
                                            font_weight="700",
                                            color=AppColor.BLACK,
                                            width="280px",
                                        ),
                                        rx.text(
                                            "행정구역",
                                            font_size="12px",
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
                                                font_weight="700",
                                                color=AppColor.BLACK,
                                                width="280px",
                                            ),
                                            rx.text(
                                                State.meeting_location_detail,
                                                font_size="10px",
                                                font_weight="700",
                                                color=AppColor.BLACK,
                                                width="280px",
                                            ),
                                        ),
                                        rx.text(
                                            "상세주소",
                                            font_size="12px",
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
                ),
                main_sub_text_box(
                    "약속 후보 날짜",
                    "최대 10일까지 선택가능합니다.",
                    need_start=True,
                ),
                calendar_header(purpose="make"),
                rx.box(
                    sub_text_box("약속 후보 날짜"),
                    rx.scroll_area(
                        rx.grid(
                            rx.foreach(State.select_data, main_text_box),
                            columns="3",
                            width="100%",
                        ),
                        type="auto",
                        scrollbars="vertical",
                        style={"height": 170, "width": 360},
                    ),
                ),
                main_button(text="다음", type="submit"),
                width="360px",
            ),
            width="100%",
        ),
        on_submit=State.make_meeting_handle_submit,
        width="100%",
        height="100%",
        align="center",
    )
