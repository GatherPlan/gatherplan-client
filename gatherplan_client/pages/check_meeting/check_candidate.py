from typing import Dict

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    sub_text_box,
)
from gatherplan_client.templates.template import template


def list_view_candidate(items: Dict):
    return rx.cond(
        items["click"],
        rx.button(
            rx.hstack(
                rx.center(
                    items["date"],
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    width="100px",
                    height="40px",
                ),
                rx.center(
                    items["start_time"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    width="50px",
                    height="40px",
                ),
                rx.center(
                    "~",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    width="15px",
                    height="40px",
                ),
                rx.center(
                    items["end_time"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    width="50px",
                    height="40px",
                ),
                rx.center(
                    items["user_count"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    height="40px",
                    width="20px",
                    padding_left="20px",
                ),
                rx.center(
                    items["weather"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    height="40px",
                    width="40px",
                    padding_left="10px",
                ),
                width="360px",
                height="40px",
            ),
            background_color=AppColor.WHITE,
            border="1px solid #0000FF",
            border_radius="10px",
            height="50px",
            width="360px",
            padding="0px",
            on_click=State.get_appointments_candidates_click_get_user(items["index"]),
        ),
        rx.button(
            rx.hstack(
                rx.center(
                    items["date"],
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    width="100px",
                    height="40px",
                ),
                rx.center(
                    items["start_time"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    width="50px",
                    height="40px",
                ),
                rx.center(
                    "~",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    width="15px",
                    height="40px",
                ),
                rx.center(
                    items["end_time"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    width="50px",
                    height="40px",
                ),
                rx.center(
                    items["user_count"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    height="40px",
                    width="20px",
                    padding_left="20px",
                ),
                rx.center(
                    items["weather"],
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.GRAY_TEXT,
                    height="40px",
                    width="40px",
                    padding_left="10px",
                ),
                width="360px",
                height="40px",
            ),
            background_color=AppColor.WHITE,
            border="1px solid #D9D9D9",
            border_radius="10px",
            height="50px",
            width="360px",
            padding="0px",
            on_click=State.get_appointments_candidates_click_get_user(items["index"]),
        ),
    )


@template(
    route="/check_candidate",
    header_url="/check_meeting_detail",
    page_text="약속 확정하기",
    on_load=State.get_appointments_candidates,
)
def check_candidate() -> rx.Component:
    return rx.center(
        rx.vstack(
            main_sub_text_box(
                "약속 후보 시간 목록",
                "참여율, 약속 구간 길이, 날씨를 기준으로 정렬된 결과가 반환됩니다.",
            ),
            sub_text_box("검색결과"),
            rx.scroll_area(
                rx.foreach(
                    State.meeting_confirm_display_data,
                    list_view_candidate,
                ),
                type="scroll",
                scrollbars="vertical",
                style={"height": "40%"},
            ),
            main_sub_text_box("참여자 목록", State.meeting_confirm_display_data_user),
            main_button("다음", on_click=rx.redirect("/check_candidate_check")),
            width="360px",
        ),
        width="100%",
    )
