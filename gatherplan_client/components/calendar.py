from typing import List

import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, AppFontFamily


def calendar_button(
    display_data: List,
    text_color: AppColor = AppColor.BLACK,
    background_color: AppColor = AppColor.WHITE,
    disable: bool = False,
):
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                display_data[0].to_string(json=False).split("-")[2],
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
                        rx.box(
                            rx.text(
                                State.click_date,
                                font_size="18px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.BLACK,
                                padding_left="10px",
                            ),
                            width="360px",
                        ),
                        rx.box(
                            rx.text(
                                "나의 일정",
                                font_size="12px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.GRAY_TEXT,
                                padding_left="10px",
                            ),
                            rx.text(
                                "TBD: xD1",
                                font_size="14px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.BLACK,
                                padding_left="12px",
                            ),
                            rx.text(
                                "TBD: xD2",
                                font_size="14px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.BLACK,
                                padding_left="12px",
                            ),
                            width="360px",
                            height="100px",
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
            )
        ),
        direction="bottom",
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
    return rx.text(
        display_select_date,
        font_size="14px",
        font_family=AppFontFamily.DEFAULT_FONT,
        font_weight="700",
        color=AppColor.BLACK,
        padding_left="10px",
    )


def location_button(display_data: List):
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
