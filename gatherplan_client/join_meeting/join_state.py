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
    meeting_memo: str = ""
    select_location_detail_location: str = ""
    meeting_date: List[str] = ["2024-5-3", "2024-5-12"]
    host_name: str = ""
    post_data: Dict = {}
    display_select_date: List = []
    # display_select_date: str = ""

    # time button click
    first_click_time: str = ""
    time_data_to_button_click: Dict[str, bool] = {
        "00:00": 0,
        "01:00": 0,
        "02:00": 0,
        "03:00": 0,
        "04:00": 0,
        "05:00": 0,
        "06:00": 0,
        "07:00": 0,
        "08:00": 0,
        "09:00": 0,
        "10:00": 0,
        "11:00": 0,
        "12:00": 0,
        "13:00": 0,
        "14:00": 0,
        "15:00": 0,
        "16:00": 0,
        "17:00": 0,
        "18:00": 0,
        "19:00": 0,
        "20:00": 0,
        "21:00": 0,
        "22:00": 0,
        "23:00": 0,
        "23:59": 0,
    }

    # TODO: meeting state랑 같은 함수를 공유할 수는 없을까?
    # CalendarSelect Data
    display_data: Dict[str, bool] = {}
    checked_data: Dict[str, bool] = {}
    holiday_data: Dict[str, str] = {}
    select_data: List[str] = []
    click_date: str = ""

    setting_time = datetime.datetime.now()
    setting_time_display = setting_time.strftime("%Y-%m")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._setting_month_calendar()

    def click_button(self, click_data: List):
        self.click_date = click_data

    def add_meeting_schedule(self, date):
        intervals = []
        start_time = None
        prev_key = None

        for key, value in self.time_data_to_button_click.items():
            if value == 2:
                if start_time is None:
                    start_time = key
                prev_key = key
            else:
                if start_time is not None:
                    intervals.append({"start": start_time, "end": prev_key})
                    start_time = None

        # Handle the case where the last interval ends at the last key
        if start_time is not None:
            intervals.append({"start": start_time, "end": prev_key})

        self.post_data[date] = intervals
        self.display_data[date] = True

        display_select_date_temp = f"{date} "

        for interval in intervals:
            display_select_date_temp += f" {interval['start']}-{interval['end']},"

        self.display_select_date.append(display_select_date_temp[:-1])
        self.time_data_to_button_click = {
            "00:00": 0,
            "01:00": 0,
            "02:00": 0,
            "03:00": 0,
            "04:00": 0,
            "05:00": 0,
            "06:00": 0,
            "07:00": 0,
            "08:00": 0,
            "09:00": 0,
            "10:00": 0,
            "11:00": 0,
            "12:00": 0,
            "13:00": 0,
            "14:00": 0,
            "15:00": 0,
            "16:00": 0,
            "17:00": 0,
            "18:00": 0,
            "19:00": 0,
            "20:00": 0,
            "21:00": 0,
            "22:00": 0,
            "23:00": 0,
            "23:59": 0,
        }

    def click_time_button(self, click_time: str):
        """
        0: no click
        1: first click
        2: range
        """

        if self.time_data_to_button_click[click_time] != 0:
            self.time_data_to_button_click = {
                "00:00": 0,
                "01:00": 0,
                "02:00": 0,
                "03:00": 0,
                "04:00": 0,
                "05:00": 0,
                "06:00": 0,
                "07:00": 0,
                "08:00": 0,
                "09:00": 0,
                "10:00": 0,
                "11:00": 0,
                "12:00": 0,
                "13:00": 0,
                "14:00": 0,
                "15:00": 0,
                "16:00": 0,
                "17:00": 0,
                "18:00": 0,
                "19:00": 0,
                "20:00": 0,
                "21:00": 0,
                "22:00": 0,
                "23:00": 0,
                "23:59": 0,
            }
            self.time_data_to_button_click[click_time] = 1
            self.first_click_time = click_time
            return

        # 첫 클릭이 없을 땐
        if self.first_click_time == "":
            self.time_data_to_button_click[click_time] = 1
            self.first_click_time = click_time

        # 첫 클릭은 있고 두 번째 클릭이 없을 땐
        elif self.first_click_time != "":

            self.time_data_to_button_click[click_time] = 2

            start = datetime.datetime.strptime(self.first_click_time, "%H:%M")
            end = datetime.datetime.strptime(click_time, "%H:%M")

            if end <= start:
                self.time_data_to_button_click[click_time] = 0
                self.time_data_to_button_click[self.first_click_time] = 0
                self.first_click_time = ""
                return

            while start <= end:
                time_key = start.strftime("%H:%M")
                if time_key in self.time_data_to_button_click:
                    self.time_data_to_button_click[time_key] = 2
                start += datetime.timedelta(hours=1)

            self.first_click_time = ""

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

    def handle_result_submit(self):
        """Handle the form submit."""
        self._get_meeting_info()
        return rx.redirect("/join_meeting_result")

    def _get_meeting_info(self):
        self.meeting_name = "세얼간이의 점심약속"
        self.meeting_location = "서울시 강남구 역삼동"
        self.select_location_detail_location = "역삼역 3번 출구"
        self.meeting_date = ["2024-4-3", "2024-4-12"]
        self.host_name = "이재훈"
