from typing import List

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import calendar_button_component
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import sub_text_box


def calendar_button(
    display_data: List,
    text_color: AppColor = AppColor.BLACK,
    background_color: AppColor = AppColor.WHITE,
    disable: bool = False,
):
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                display_data[0].split("-")[2],
                width="40px",
                height="32px",
                color=text_color,
                font_size="14px",
                type="button",
                disabled=disable,
                background_color=background_color,
                on_click=State.click_button(display_data[0]),
            )
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.center(
                    rx.vstack(
                        rx.text(
                            State.click_date,
                            font_size="18px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_weight="700",
                            color=AppColor.BLACK,
                            padding_left="10px",
                            width="360px",
                        ),
                        rx.box(
                            rx.text(
                                "시간 선택",
                                font_size="12px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.GRAY_TEXT,
                                padding_left="10px",
                            ),
                            rx.grid(
                                rx.foreach(
                                    State.time_data_to_button_click,
                                    time_button,
                                ),
                                columns="5",
                                align="center",
                                width="360px",
                            ),
                            width="360px",
                            height="200px",
                        ),
                        rx.center(
                            rx.drawer.close(
                                rx.button(
                                    "일정추가",
                                    width="348px",
                                    height="35px",
                                    padding="20px",
                                    color=AppColor.WHITE,
                                    type="submit",
                                    background_color=AppColor.MAIN_COLOR,
                                    on_click=State.add_meeting_schedule(
                                        State.click_date
                                    ),
                                )
                            ),
                            width="100%",
                        ),
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
                border_radius="1em 1em 0 0",
            ),
        ),
        direction="bottom",
        # on_open_change=State.init_calendar_click_button(),
    )


def time_button(time_data_to_button_click: List):
    return rx.cond(
        time_data_to_button_click[1] == 0,
        rx.button(
            time_data_to_button_click[0],
            type="button",
            background_color=AppColor.SUB_TEXT,
            color=AppColor.BLACK,
            width="60px",
            height="22px",
            font_size="8px",
            on_click=State.click_time_button(time_data_to_button_click[0]),
            margin="5px",
        ),
        rx.cond(
            time_data_to_button_click[1] == 1,
            rx.button(
                time_data_to_button_click[0],
                type="button",
                background_color=AppColor.BLUE,
                color=AppColor.WHITE,
                width="60px",
                height="22px",
                font_size="8px",
                on_click=State.click_time_button(time_data_to_button_click[0]),
                margin="5px",
            ),
            rx.button(
                time_data_to_button_click[0],
                type="button",
                background_color=AppColor.MAIN_COLOR,
                color=AppColor.WHITE,
                width="60px",
                height="22px",
                font_size="8px",
                on_click=State.click_time_button(time_data_to_button_click[0]),
                margin="5px",
            ),
        ),
    )


def display_select_date(display_select_date: str):
    return sub_text_box(display_select_date)


def calendar_header(purpose: str = "join", height: str = "35%"):
    return rx.center(
        rx.vstack(
            rx.center(
                rx.button(
                    rx.icon(tag="chevron-left"),
                    on_click=State.month_decrement,
                    width="36px",
                    height="30px",
                    color=AppColor.BLACK,
                    background_color=AppColor.WHITE,
                ),
                rx.center(
                    State.setting_time_display,
                    width="100px",
                    height="30px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="600",
                ),
                rx.button(
                    rx.icon(tag="chevron-right"),
                    on_click=State.month_increment,
                    width="36px",
                    height="30px",
                    color=AppColor.BLACK,
                    background_color=AppColor.WHITE,
                ),
                width="100%",
            ),
            rx.grid(
                rx.center("일", color=AppColor.RED, width="45px"),
                rx.center("월", width="45px"),
                rx.center("화", width="45px"),
                rx.center("수", width="45px"),
                rx.center("목", width="45px"),
                rx.center("금", width="45px"),
                rx.center("토", color=AppColor.BLUE, width="45px"),
                rx.cond(
                    purpose == "join",
                    rx.foreach(
                        State.display_data,
                        location_button_join,
                    ),
                    rx.cond(
                        purpose == "make",
                        rx.foreach(
                            State.display_data,
                            location_button_make,
                        ),
                        rx.foreach(
                            State.display_data,
                            location_button_check,
                        ),
                    ),
                ),
                columns="7",
                width="315px",
            ),
        ),
        width="100%",
        height=height,
    )


def location_button_join(display_data: List):
    return rx.cond(
        State.checked_data[display_data[0]],
        rx.cond(
            State.holiday_data[display_data[0]] == "sun",
            rx.cond(
                State.holiday_data[display_data[0]] == "prev",
                calendar_button(
                    display_data=display_data,
                    text_color=AppColor.RED,
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disable=True,
                ),
                rx.cond(
                    display_data[1],
                    calendar_button(
                        display_data=display_data,
                        text_color=AppColor.RED,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        disable=True,
                    ),
                    calendar_button(
                        display_data=display_data,
                        text_color=AppColor.RED,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        disable=True,
                    ),
                ),
            ),
            rx.cond(
                State.holiday_data[display_data[0]] == "sat",
                rx.cond(
                    State.holiday_data[display_data[0]] == "prev",
                    calendar_button(
                        display_data=display_data,
                        text_color=AppColor.BLUE,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        disable=True,
                    ),
                    rx.cond(
                        display_data[1],
                        calendar_button(
                            display_data=display_data,
                            text_color=AppColor.BLUE,
                            background_color=AppColor.BACKGROUND_GRAY_COLOR,
                            disable=True,
                        ),
                        calendar_button(
                            display_data=display_data,
                            text_color=AppColor.BLUE,
                            background_color=AppColor.BACKGROUND_GRAY_COLOR,
                            disable=True,
                        ),
                    ),
                ),
                rx.cond(
                    State.holiday_data[display_data[0]] == "prev",
                    calendar_button(
                        display_data=display_data,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        disable=True,
                    ),
                    rx.cond(
                        display_data[1],
                        calendar_button(
                            display_data=display_data,
                            background_color=AppColor.BACKGROUND_GRAY_COLOR,
                            disable=True,
                            text_color=AppColor.WHITE,
                        ),
                        calendar_button(
                            display_data=display_data,
                            background_color=AppColor.BACKGROUND_GRAY_COLOR,
                            disable=True,
                        ),
                    ),
                ),
            ),
        ),
        rx.cond(
            State.holiday_data[display_data[0]] == "sun",
            rx.cond(
                State.holiday_data[display_data[0]] == "prev",
                calendar_button(
                    display_data=display_data,
                    text_color=AppColor.RED,
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disable=True,
                ),
                rx.cond(
                    display_data[1],
                    calendar_button(
                        display_data=display_data,
                        text_color=AppColor.RED,
                        background_color=AppColor.SKY_BLUE,
                    ),
                    calendar_button(
                        display_data=display_data,
                        text_color=AppColor.RED,
                        background_color=AppColor.WHITE,
                    ),
                ),
            ),
            rx.cond(
                State.holiday_data[display_data[0]] == "sat",
                rx.cond(
                    State.holiday_data[display_data[0]] == "prev",
                    calendar_button(
                        display_data=display_data,
                        text_color=AppColor.BLUE,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        disable=True,
                    ),
                    rx.cond(
                        display_data[1],
                        calendar_button(
                            display_data=display_data,
                            text_color=AppColor.BLUE,
                            background_color=AppColor.SKY_BLUE,
                        ),
                        calendar_button(
                            display_data=display_data,
                            text_color=AppColor.BLUE,
                            background_color=AppColor.WHITE,
                        ),
                    ),
                ),
                rx.cond(
                    State.holiday_data[display_data[0]] == "prev",
                    calendar_button(
                        display_data=display_data,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        disable=True,
                    ),
                    rx.cond(
                        display_data[1],
                        calendar_button(
                            display_data=display_data,
                            background_color=AppColor.SKY_BLUE,
                            text_color=AppColor.WHITE,
                        ),
                        calendar_button(
                            display_data=display_data,
                            background_color=AppColor.WHITE,
                        ),
                    ),
                ),
            ),
        ),
    )


def location_button_make(display_data: List):
    return rx.cond(
        State.holiday_data[display_data[0]] == "sun",
        rx.cond(
            State.holiday_data[display_data[0]] == "prev",
            calendar_button_component(
                display_data[0].split("-")[2],
                color=AppColor.RED,
                background_color=AppColor.BACKGROUND_GRAY_COLOR,
                disabled=True,
                on_click=State.make_meeting_date_click_button(display_data[0]),
            ),
            rx.cond(
                display_data[1],
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color=AppColor.RED,
                    border="3px solid #4E5CDC",
                    background_color=AppColor.WHITE,
                    on_click=State.make_meeting_date_click_button(display_data[0]),
                ),
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color=AppColor.RED,
                    background_color=AppColor.WHITE,
                    on_click=State.make_meeting_date_click_button(display_data[0]),
                ),
            ),
        ),
        rx.cond(
            State.holiday_data[display_data[0]] == "sat",
            rx.cond(
                State.holiday_data[display_data[0]] == "prev",
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color=AppColor.BLUE,
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=State.make_meeting_date_click_button(display_data[0]),
                ),
                rx.cond(
                    display_data[1],
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color=AppColor.BLUE,
                        border="3px solid #4E5CDC",
                        background_color=AppColor.WHITE,
                        on_click=State.make_meeting_date_click_button(display_data[0]),
                    ),
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color=AppColor.BLUE,
                        background_color=AppColor.WHITE,
                        on_click=State.make_meeting_date_click_button(display_data[0]),
                    ),
                ),
            ),
            rx.cond(
                State.holiday_data[display_data[0]] == "prev",
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color="#000000",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=State.make_meeting_date_click_button(display_data[0]),
                ),
                rx.cond(
                    display_data[1],
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color="#000000",
                        background_color=AppColor.WHITE,
                        border="3px solid #4E5CDC",
                        on_click=State.make_meeting_date_click_button(display_data[0]),
                    ),
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color="#000000",
                        background_color=AppColor.WHITE,
                        on_click=State.make_meeting_date_click_button(display_data[0]),
                    ),
                ),
            ),
        ),
    )


def location_button_check(display_data: List):
    return rx.cond(
        State.holiday_data[display_data[0]] == "sun",
        rx.cond(
            State.holiday_data[display_data[0]] == "prev",
            calendar_button_component(
                display_data[0].split("-")[2],
                color=AppColor.RED,
                background_color=AppColor.BACKGROUND_GRAY_COLOR,
                disabled=True,
                on_click=State.check_meeting_date_click_button(display_data[0]),
            ),
            rx.cond(
                display_data[1],
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color=AppColor.RED,
                    border="3px solid #4E5CDC",
                    background_color=AppColor.WHITE,
                    on_click=State.check_meeting_date_click_button(display_data[0]),
                ),
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color=AppColor.RED,
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=State.check_meeting_date_click_button(display_data[0]),
                ),
            ),
        ),
        rx.cond(
            State.holiday_data[display_data[0]] == "sat",
            rx.cond(
                State.holiday_data[display_data[0]] == "prev",
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color=AppColor.BLUE,
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=State.check_meeting_date_click_button(display_data[0]),
                ),
                rx.cond(
                    display_data[1],
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color=AppColor.BLUE,
                        border="3px solid #4E5CDC",
                        background_color=AppColor.WHITE,
                        on_click=State.check_meeting_date_click_button(display_data[0]),
                    ),
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color=AppColor.BLUE,
                        disabled=True,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        on_click=State.check_meeting_date_click_button(display_data[0]),
                    ),
                ),
            ),
            rx.cond(
                State.holiday_data[display_data[0]] == "prev",
                calendar_button_component(
                    display_data[0].split("-")[2],
                    color="#000000",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    disabled=True,
                    on_click=State.check_meeting_date_click_button(display_data[0]),
                ),
                rx.cond(
                    display_data[1],
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color="#000000",
                        background_color=AppColor.WHITE,
                        border="3px solid #4E5CDC",
                        on_click=State.check_meeting_date_click_button(display_data[0]),
                    ),
                    calendar_button_component(
                        display_data[0].split("-")[2],
                        color="#000000",
                        disabled=True,
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                        on_click=State.check_meeting_date_click_button(display_data[0]),
                    ),
                ),
            ),
        ),
    )
