from typing import List

import reflex as rx

from gatherplan_client.join_meeting.join_state import JoinState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import AppFontFamily, AppColor


def time_button(text):
    return rx.button(
        text,
        type="button",
        background_color=AppColor.SUB_TEXT,
        color=AppColor.BLACK,
        width="60px",
        height="22px",
        font_size="8px",
        on_click=JoinState.click_time_button(text),
        margin="5px",
    )


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
                on_click=JoinState.click_button(display_data[0]),
            )
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.center(
                    rx.vstack(
                        rx.box(
                            rx.text(
                                JoinState.click_date,
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
                                    [
                                        "00:00",
                                        "01:00",
                                        "02:00",
                                        "03:00",
                                        "04:00",
                                        "05:00",
                                        "06:00",
                                        "07:00",
                                        "08:00",
                                        "09:00",
                                        "10:00",
                                        "11:00",
                                        "12:00",
                                        "13:00",
                                        "14:00",
                                        "15:00",
                                        "16:00",
                                        "17:00",
                                        "18:00",
                                        "19:00",
                                        "20:00",
                                        "21:00",
                                        "22:00",
                                        "23:00",
                                        "23:59",
                                    ],
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
                            rx.button(
                                "일정추가",
                                width="348px",
                                height="35px",
                                padding="20px",
                                color=AppColor.WHITE,
                                type="submit",
                                background_color=AppColor.MAIN_COLOR,
                                on_click=rx.redirect("/join_meeting_time"),
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
                border_radius="2em 2em 0 0",
            )
        ),
        direction="bottom",
    )


def location_button(display_data: List):
    return rx.cond(
        JoinState.checked_data[display_data[0]],
        rx.cond(
            JoinState.holiday_data[display_data[0]] == "sun",
            rx.cond(
                JoinState.holiday_data[display_data[0]] == "prev",
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
                JoinState.holiday_data[display_data[0]] == "sat",
                rx.cond(
                    JoinState.holiday_data[display_data[0]] == "prev",
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
                    JoinState.holiday_data[display_data[0]] == "prev",
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
            JoinState.holiday_data[display_data[0]] == "sun",
            rx.cond(
                JoinState.holiday_data[display_data[0]] == "prev",
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
                JoinState.holiday_data[display_data[0]] == "sat",
                rx.cond(
                    JoinState.holiday_data[display_data[0]] == "prev",
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
                    JoinState.holiday_data[display_data[0]] == "prev",
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


def join_meeting_date() -> rx.Component:
    return rx.vstack(
        header("/join_meeting"),
        rx.center(
            rx.text(
                "약속 참여하기",
                font_size="20px",
                padding_top="28px",
                padding_bottom="40px",
                padding_left="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                width="360px",
            ),
            width="100%",
            height="10%",
        ),
        rx.center(
            rx.vstack(
                rx.text(
                    "약속 참여 일정",
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_left="10px",
                ),
                rx.text(
                    "참여가능한 날짜와 시간을 선택해주세요",
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
                        on_click=JoinState.month_decrement,
                        width="48px",
                        height="40px",
                        margin_left="50px",
                        color=AppColor.BLACK,
                        background_color=AppColor.WHITE,
                    ),
                    rx.center(
                        JoinState.setting_time_display,
                        width="100px",
                        height="40px",
                        align="center",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="600",
                    ),
                    rx.button(
                        rx.icon(tag="chevron-right"),
                        on_click=JoinState.month_increment,
                        width="48px",
                        height="40px",
                        color=AppColor.BLACK,
                        background_color=AppColor.WHITE,
                    ),
                    align="center",
                ),
                rx.grid(
                    rx.center("일", color=AppColor.RED, width="40px"),
                    rx.center("월", width="40px"),
                    rx.center("화", width="40px"),
                    rx.center("수", width="40px"),
                    rx.center("목", width="40px"),
                    rx.center("금", width="40px"),
                    rx.center("토", color=AppColor.BLUE, width="40px"),
                    rx.foreach(
                        JoinState.display_data,
                        location_button,
                    ),
                    columns="7",
                    align="center",
                    width="320px",
                ),
            ),
            color=AppColor.BLACK,
            font_size="14px",
            font_family=AppFontFamily.DEFAULT_FONT,
            width="100%",
            font_weight="400",
            background_color=AppColor.WHITE,
            height="35%",
        ),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.text(
                        "선택한 일정",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                        padding_left="10px",
                    ),
                    width="360px",
                ),
                rx.scroll_area(
                    rx.flex(
                        rx.text(
                            """Three fundamental aspects of typography are legibility, readability, and
                        aesthetics. Although in a non-technical sense “legible” and “readable”
                        are often used synonymously, typographically they are separate but
                        related concepts.""",
                        ),
                        rx.text(
                            """Legibility describes how easily individual characters can be
                        distinguished from one another. It is described by Walter Tracy as “the
                        quality of being decipherable and recognisable”. For instance, if a “b”
                        and an “h”, or a “3” and an “8”, are difficult to distinguish at small
                        sizes, this is a problem of legibility.""",
                        ),
                        rx.text(
                            """Typographers are concerned with legibility insofar as it is their job to
                        select the correct font to use. Brush Script is an example of a font
                        containing many characters that might be difficult to distinguish. The
                        selection of cases influences the legibility of typography because using
                        only uppercase letters (all-caps) reduces legibility.""",
                        ),
                        direction="column",
                        spacing="4",
                    ),
                    type="always",
                    scrollbars="vertical",
                    style={"height": 140, "width": 360},
                ),
            ),
            width="100%",
            height="30%",
        ),
        rx.center(
            rx.button(
                "선택완료",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=rx.redirect("/join_meeting_time"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
