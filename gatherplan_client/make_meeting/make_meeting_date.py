from typing import List, Dict

import reflex as rx
import datetime
import calendar
from dateutil.relativedelta import relativedelta


from gatherplan_client.login import need_login
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily
from gatherplan_client.reflex_assets.text_box import left_align_text_box


def location_button(display_data: List):
    return rx.cond(
        CalendarSelect.holiday_data[display_data[0]] == "prev",
        rx.button(
            display_data[0].to_string(json=False).split("-")[2],
            width="50px",
            height="36px",
            color="#000000",
            font_size="16px",
            type="button",
            background_color=AppColor.BACKGROUND_GRAY_COLOR,
            disabled=True,
            on_click=CalendarSelect.click_button(display_data[0]),
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
                on_click=CalendarSelect.click_button(display_data[0]),
            ),
            rx.button(
                display_data[0].to_string(json=False).split("-")[2],
                width="50px",
                height="36px",
                color="#000000",
                font_size="16px",
                type="button",
                background_color=AppColor.WHITE,
                on_click=CalendarSelect.click_button(display_data[0]),
            ),
        ),
    )


class CalendarSelect(rx.State):
    display_data: Dict[str, bool] = {}
    holiday_data: Dict[str, str] = {}
    select_data: List[str] = []

    setting_time = datetime.datetime.now()
    setting_time_display = setting_time.strftime("%Y-%m")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._setting_month_calendar()

    def click_button(self, click_data: List):
        if self.display_data[click_data]:
            self.select_data.remove(click_data)
            self.display_data[click_data] = False
        else:
            self.select_data.append(click_data)
            self.display_data[click_data] = True

    def month_decrement(self):
        self.setting_time = self.setting_time - relativedelta(months=1)
        self.setting_time_display = self.setting_time.strftime("%Y-%m")
        self._setting_month_calendar()

    def month_increment(self):
        self.setting_time = self.setting_time + relativedelta(months=1)
        self.setting_time_display = self.setting_time.strftime("%Y-%m")
        self._setting_month_calendar()

    def _setting_month_calendar(self):
        self.display_data = {}

        weekday = (
            datetime.date(self.setting_time.year, self.setting_time.month, 1).weekday()
            + 1
        )

        for i in range(weekday):
            temp = " " * i
            self.display_data[temp] = False
            self.holiday_data[temp] = "prev"

        for i in range(
            1,
            calendar.monthrange(self.setting_time.year, self.setting_time.month)[1] + 1,
        ):
            self.display_data[
                f"{self.setting_time.year}-{self.setting_time.month}-{i}"
            ] = False

            weekday = datetime.date(
                self.setting_time.year, self.setting_time.month, 1
            ).weekday()

            self.holiday_data[
                f"{self.setting_time.year}-{self.setting_time.month}-{i}"
            ] = ("sun" if weekday == 7 else "sat" if weekday == 6 else "normal")

        for clicked_data in self.select_data:
            if clicked_data in self.display_data.keys():
                self.display_data[clicked_data] = True


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
        rx.center(
            rx.button("<", on_click=CalendarSelect.month_decrement),
            rx.text(
                CalendarSelect.setting_time_display,
                width="100px",
                height="45px",
                align="center",
            ),
            rx.button(">", on_click=CalendarSelect.month_increment),
            color=AppColor.BLACK,
            font_size=TextSize.MEDIUM,
            font_family=AppFontFamily.DEFAULT_FONT,
            height="45px",
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
                    CalendarSelect.display_data,
                    location_button,
                ),
                columns="7",
                align="center",
                width="360px",
            ),
            width="100%",
        ),
        # TODO: Implement the date picker
        basic_button("다음"),
        spacing="0",
        height="100vh",
    )