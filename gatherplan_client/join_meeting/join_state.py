import datetime
import json
from typing import List, Dict

import reflex as rx
from dateutil.relativedelta import relativedelta
from pytimekr import pytimekr

from gatherplan_client.additional_holiday import additional_holiday
import calendar
import requests

from gatherplan_client.backend_rouuter import BACKEND_URL, HEADER


class JoinState(rx.State):
    meeting_code: str = ""
    appointment_code: str = ""
    meeting_name: str = ""
    meeting_location: str = ""
    meeting_memo: str = ""
    select_location_detail_location: str = ""
    meeting_date: List[str] = []
    host_name: str = ""
    post_data: Dict = {}
    display_select_date: List = []
    display_: List[dict] = []
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

        split_date_string = date.split("-")
        display_select_date_temp = f"{date} "

        for interval in intervals:
            select_date_temp = {
                "selectedDate": f"{split_date_string[0]}-{int(split_date_string[1]):02}-{int(split_date_string[2]):02}",
                "selectedStartTime": interval["start"],
                "selectedEndTime": interval["end"],
            }
            display_select_date_temp += f" {interval['start']}-{interval['end']},"
            self.select_data.append(select_date_temp)

            self.display_select_date.append(display_select_date_temp[:-1])

        # {
        #     "appointmentCode": "abcd1234efgh",
        #     "selectedDateTimeList": [
        #         {
        #             "selectedDate": "2024-04-10",
        #             "selectedStartTime": "15:00",
        #             "selectedEndTime": "18:00"
        #         },
        #         {
        #             "selectedDate": "2024-04-10",
        #             "selectedStartTime": "19:00",
        #             "selectedEndTime": "21:00"
        #         }
        #     ],
        #     "nickname": "이재훈"
        # }

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
            if 1 <= self.setting_time.month <= 9:
                temp_month = f"0{self.setting_time.month}"

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
                if f"{self.setting_time.year}-{temp_month:02}-{i:02}"
                in self.meeting_date
                else True
            )
        for clicked_data in self.select_data:
            if clicked_data in self.display_data.keys():
                self.display_data[clicked_data] = True

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self._get_meeting_info(form_data["enter_code"])

        return rx.redirect("/join_meeting")

    def handle_result_submit(self, login_token, nick_name):
        """Handle the form submit."""
        response = self._post_join_meeting(login_token, nick_name)

        if response.status_code == 200:
            return rx.redirect(f"/join_meeting_result")
        else:
            print(response.json())
            return rx.window_alert(f"error")

    def _get_meeting_info(self, enter_code: str):
        response = requests.get(
            f"{BACKEND_URL}/api/v1/appointments/preview",
            headers={"accept": "*/*"},
            params={"appointmentCode": enter_code},
        )

        if response.status_code == 200:
            data = response.json()
            self.meeting_name = data["appointmentName"]
            self.meeting_location = data["address"]["fullAddress"]
            self.meeting_memo = data["notice"]
            self.meeting_date = data["candidateDateList"]
            self.host_name = data["hostName"]
            self.appointment_code = data["appointmentCode"]

            self._setting_month_calendar()
        else:
            print(response.json())
            return rx.window_alert(f"존재하지 않는 약속 코드입니다.")

    def _post_join_meeting(self, login_token, nick_name):

        header = HEADER
        header["Authorization"] = login_token
        response = requests.post(
            f"{BACKEND_URL}/api/v1/appointments/join",
            headers=header,
            json={
                "appointmentCode": self.appointment_code,
                "selectedDateTimeList": self.get_value(self.select_data),
                "nickname": nick_name,
            },
        )

        return response
