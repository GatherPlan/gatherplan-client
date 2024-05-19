from typing import List

import reflex as rx
from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily


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
                    border="3px solid #4E5CDC",
                    background_color=AppColor.WHITE,
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
                        border="3px solid #4E5CDC",
                        background_color=AppColor.WHITE,
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
                        background_color=AppColor.WHITE,
                        border="3px solid #4E5CDC",
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
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.button(
                        rx.icon(tag="chevron-left"),
                        on_click=MakeMeetingNameState.month_decrement,
                        width="48px",
                        height="40px",
                        margin_left="74px",
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
                    align="center",
                ),
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
            ),
            color=AppColor.BLACK,
            font_size=TextSize.SMALL_MEDIUM,
            font_family=AppFontFamily.DEFAULT_FONT,
            width="100%",
            font_weight="600",
            background_color=AppColor.WHITE,
            height="55%",
        ),
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
