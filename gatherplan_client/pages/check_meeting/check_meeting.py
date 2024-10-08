from typing import Dict

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import main_sub_text_box, sub_text_box
from gatherplan_client.templates.template import template


def list_view(items: Dict):
    return rx.button(
        rx.box(
            rx.text(
                items["meeting_name"],
                font_size="14px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.BLACK,
            ),
            rx.text(
                items["host_name"],
                font_size="12px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.GRAY_TEXT,
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
        background_color=AppColor.WHITE,
        border="1px solid #D9D9D9",
        border_radius="10px",
        height="50px",
        width="360px",
        on_click=State.check_appointments_detail(items["meeting_code"]),
        margin_bottom="10px",
    )


@template(
    route="/check_meeting",
    header_url="/",
    page_text="약속 정보",
    need_login_type="check_meeting_login",
    on_load=State.check_get_appointments_list,
)
def check_meeting() -> rx.Component:
    return rx.form(
        rx.center(
            rx.vstack(
                main_sub_text_box(
                    "약속 목록", "약속 이름 또는 호스트 이름을 검색해보세요"
                ),
                rx.hstack(
                    rx.box(
                        rx.input(
                            placeholder="홍길동",
                            name="keyword",
                            font_size="10px",
                            height="35px",
                            type="text",
                        ),
                        padding_bottom="20px",
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
                ),
                sub_text_box("검색결과"),
                rx.scroll_area(
                    rx.foreach(State.check_meeting_list, list_view),
                    type="scroll",
                    scrollbars="vertical",
                    style={"height": "70%"},
                ),
                width="360px",
            ),
            width="100%",
        ),
        on_submit=State.check_get_appointments_search,
        width="100%",
        height="100%",
        align="center",
    )
