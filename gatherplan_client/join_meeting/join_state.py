import datetime
from typing import List, Dict

import reflex as rx
from dateutil.relativedelta import relativedelta
from pytimekr import pytimekr

from gatherplan_client.additional_holiday import additional_holiday
import calendar


class JoinState(rx.State):
    meeting_code: str = ""
    meeting_name: str = ""
    meeting_location: str = ""
    select_location_detail_location: str = ""
    meeting_date: List[str] = ["2024-5-3", "2024-5-12"]
    meeting_time: List[str] = []
    host_name: str = ""

    # TODO: meeting state랑 같은 함수를 공유할 수는 없을까?
    # CalendarSelect Data
    display_data: Dict[str, bool] = {}
    checked_data: Dict[str, bool] = {}
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

        print(self.select_data)

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
        self.checked_data = {}

        weekday = (
            datetime.date(self.setting_time.year, self.setting_time.month, 1).weekday()
            + 1
        )

        for i in range(weekday):
            temp = " " * i
            self.display_data[temp] = False
            self.holiday_data[temp] = "prev"

        kr_holidays = pytimekr.holidays(
            year=self.setting_time.year
        ) + additional_holiday(year=self.setting_time.year)

        for i in range(
            1,
            calendar.monthrange(self.setting_time.year, self.setting_time.month)[1] + 1,
        ):
            self.display_data[
                f"{self.setting_time.year}-{self.setting_time.month}-{i}"
            ] = False

            weekday = datetime.date(
                self.setting_time.year, self.setting_time.month, i
            ).weekday()

            self.holiday_data[
                f"{self.setting_time.year}-{self.setting_time.month}-{i}"
            ] = (
                "sun"
                if weekday == 6
                or datetime.date(self.setting_time.year, self.setting_time.month, i)
                in kr_holidays
                else "sat" if weekday == 5 else "normal"
            )

            self.checked_data[
                f"{self.setting_time.year}-{self.setting_time.month}-{i}"
            ] = (
                False
                if f"{self.setting_time.year}-{self.setting_time.month}-{i}"
                in self.meeting_date
                else True
            )

        for clicked_data in self.select_data:
            if clicked_data in self.display_data.keys():
                self.display_data[clicked_data] = True

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)

        self._get_meeting_info()

        return rx.redirect("/join_meeting")

    def _get_meeting_info(self):
        self.meeting_name = "세얼간이의 점심약속"
        self.meeting_location = "서울시 강남구 역삼동"
        self.select_location_detail_location = "역삼역 3번 출구"
        self.meeting_date = ["2024-4-3", "2024-4-12"]
        self.meeting_time = ["오전", "오후"]
        self.host_name = "이재훈"
