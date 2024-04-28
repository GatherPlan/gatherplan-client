from typing import List

import reflex as rx
from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily
from gatherplan_client.reflex_assets.text_box import left_align_text_box


def location_button(display_data: List):
    return rx.cond(
        MakeMeetingNameState.holiday_data[display_data[0]] == "sun",
        rx.cond(
            MakeMeetingNameState.holiday_data[display_data[0]] == "prev",
            rx.button(
                display_data[0].to_string(json=False).split("-")[2],
                width="50px",
                height="36px",
                color=AppColor.RED,
                font_size="16px",
                type="button",
                background_color=AppColor.BACKGROUND_GRAY_COLOR,
                disabled=True,
                on_click=MakeMeetingNameState.click_button(display_data[0]),
            ),
            rx.cond(
                display_data[1],
                rx.button(
                    display_data[0].to_string(json=False).split("-")[2],
                    width="50px",
                    height="36px",
                    color=AppColor.RED,
                    font_size="16px",
                    type="button",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    on_click=MakeMeetingNameState.click_button(display_data[0]),
                ),
                rx.button(
                    display_data[0].to_string(json=False).split("-")[2],
                    width="50px",
                    height="36px",
                    color=AppColor.RED,
                    font_size="16px",
                    type="button",
                    background_color=AppColor.WHITE,
                    on_click=MakeMeetingNameState.click_button(display_data[0]),
                ),
            ),
        ),
        rx.cond(
            MakeMeetingNameState.holiday_data[display_data[0]] == "sat",
            rx.cond(
                MakeMeetingNameState.holiday_data[display_data[0]] == "prev",
                rx.button(
                    display_data[0].to_string(json=False).split("-")[2],
                    width="50px",
                    height="36px",
                    color=AppColor.BLUE,
                    font_size="16px",
                    type="button",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=MakeMeetingNameState.click_button(display_data[0]),
                ),
                rx.cond(
                    display_data[1],
                    rx.button(
                        display_data[0].to_string(json=False).split("-")[2],
                        width="50px",
                        height="36px",
                        color=AppColor.BLUE,
                        font_size="16px",
                        type="button",
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        on_click=MakeMeetingNameState.click_button(display_data[0]),
                    ),
                    rx.button(
                        display_data[0].to_string(json=False).split("-")[2],
                        width="50px",
                        height="36px",
                        color=AppColor.BLUE,
                        font_size="16px",
                        type="button",
                        background_color=AppColor.WHITE,
                        on_click=MakeMeetingNameState.click_button(display_data[0]),
                    ),
                ),
            ),
            rx.cond(
                MakeMeetingNameState.holiday_data[display_data[0]] == "prev",
                rx.button(
                    display_data[0].to_string(json=False).split("-")[2],
                    width="50px",
                    height="36px",
                    color="#000000",
                    font_size="16px",
                    type="button",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=MakeMeetingNameState.click_button(display_data[0]),
                ),
                rx.cond(
                    display_data[1],
                    rx.button(
                        display_data[0].to_string(json=False).split("-")[2],
                        width="50px",
                        height="36px",
                        color="#000000",
                        font_size="16px",
                        type="button",
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        on_click=MakeMeetingNameState.click_button(display_data[0]),
                    ),
                    rx.button(
                        display_data[0].to_string(json=False).split("-")[2],
                        width="50px",
                        height="36px",
                        color="#000000",
                        font_size="16px",
                        type="button",
                        background_color=AppColor.WHITE,
                        on_click=MakeMeetingNameState.click_button(display_data[0]),
                    ),
                ),
            ),
        ),
    )


@need_login
def make_meeting_date() -> rx.Component:
    return rx.vstack(
        header("약속만들기", "/make_meeting_detail"),
        left_align_text_box(
            "약속 날짜를 선택해 주세요",
            "최대 30일까지 선택할 수 있어요",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.button(
                rx.icon(tag="chevron-left"),
                on_click=MakeMeetingNameState.month_decrement,
                width="48px",
                height="40px",
                color=AppColor.BLACK,
                background_color=AppColor.WHITE,
            ),
            rx.center(
                MakeMeetingNameState.setting_time_display,
                width="100px",
                height="40px",
                align="center",
            ),
            rx.button(
                rx.icon(tag="chevron-right"),
                on_click=MakeMeetingNameState.month_increment,
                width="48px",
                height="40px",
                color=AppColor.BLACK,
                background_color=AppColor.WHITE,
            ),
            color=AppColor.BLACK,
            font_size=TextSize.SMALL_MEDIUM,
            font_family=AppFontFamily.DEFAULT_FONT,
            height="40px",
            width="100%",
            font_weight="600",
            background_color=AppColor.WHITE,
        ),
        rx.center(
            rx.grid(
                rx.center("일", color=AppColor.RED, width="50px"),
                rx.center("월", width="50px"),
                rx.center("화", width="50px"),
                rx.center("수", width="50px"),
                rx.center("목", width="50px"),
                rx.center("금", width="50px"),
                rx.center("토", color=AppColor.BLUE, width="50px"),
                rx.foreach(
                    MakeMeetingNameState.display_data,
                    location_button,
                ),
                columns="7",
                align="center",
                width="360px",
            ),
            width="100%",
        ),
        buffer_box("5%"),
        rx.center(
            rx.button(
                "다음",
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_BACKGROUND,
                on_click=rx.redirect("/make_meeting_time"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
