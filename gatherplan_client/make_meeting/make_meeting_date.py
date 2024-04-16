from typing import List

import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize
from gatherplan_client.reflex_assets.text_box import left_align_text_box


def location_button(button_text: int):
    return rx.cond(
        button_text == 0,
        rx.button(
            button_text,
            width="36px",
            height="36px",
            color="#000000",
            type="button",
            background_color="#FFFFFF",
            on_click=CalendarSelect.click_button(button_text),
        ),
        rx.cond(
            button_text == 1,
            rx.button(
                button_text,
                width="36px",
                height="36px",
                color="#0000FF",
                type="button",
                background_color="#FFFFFF",
                on_click=CalendarSelect.click_button(button_text),
            ),
            rx.button(
                button_text,
                width="36px",
                height="36px",
                color="#F50000",
                type="button",
                background_color="#FFFFFF",
                on_click=CalendarSelect.click_button(button_text),
            ),
        ),
    )


class CalendarSelect(rx.State):
    select_date: List[int] = [0, 1, 2] * 10
    weekday: List[int] = [0] * 30

    def click_button(self, value: int):
        self.select_date[value] = 1


@need_login
def make_meeting_date() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속 날짜를 선택해 주세요",
            "최대 30일까지 선택할 수 있어요",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.grid(
            rx.foreach(
                CalendarSelect.select_date,
                location_button,
            ),
            columns="7",
        ),
        # TODO: Implement the date picker
        basic_button("다음"),
        spacing="0",
        height="100vh",
    )
