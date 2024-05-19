import reflex as rx


from dateutil.relativedelta import relativedelta
from pytimekr import pytimekr
import calendar

from gatherplan_client.additional_holiday import additional_holiday
import datetime
from typing import List, Dict


class MakeMeetingNameState(rx.State):
    """The app state."""

    # TODO: default value init
    form_data: dict = {}
    meeting_name: str = "세 얼간이 점심약속"
    meeting_memo: str = "점심이나 먹죵"
    input_location: str = ""
    search_location: List[str] = ["성수동1", "성수동2", "성수동3", "성수동4"]
    select_location: str = "서울숲카페거리"
    select_location_detail_location: str = "서울 성동구 성수동 1가 000-00"

    # CalendarSelect Data
    display_data: Dict[str, bool] = {}
    holiday_data: Dict[str, str] = {}
    select_data: List[str] = ["2024-4-3", "2024-4-12"]

    setting_time = datetime.datetime.now()
    setting_time_display = setting_time.strftime("%Y-%m")

    # TimeSelect Data
    select_time: List[str] = ["오전", "오후"]

    # MeetingCode Data
    meeting_code: str = "abcd efgh ijkl mnop qrst"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._setting_month_calendar()

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        self.meeting_name = form_data.get("meeting_name")
        self.meeting_memo = form_data.get("meeting_memo")
        return rx.redirect("/make_meeting_detail")

    def handle_detail_submit(self, form_data: dict):
        """Handle the form submit."""
        self.input_location = form_data.get("input_location")
        return rx.redirect("/make_meeting_date")

    def handle_location_submit(self, form_data: dict):
        """Handle the form submit."""
        self.select_location = form_data.get("input_location")

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

        for clicked_data in self.select_data:
            if clicked_data in self.display_data.keys():
                self.display_data[clicked_data] = True

    def click_time_select_button(self, click_data: List):
        if click_data in self.select_time:
            self.select_time.remove(click_data)
        else:
            self.select_time.append(click_data)

    def handle_result_submit(self):
        meeting_data = {
            "meeting_name": self.meeting_name,
            "meeting_location": self.select_location,
            "meeting_location_detail": self.select_location_detail_location,
            "meeting_date": list(self.select_data),
            "meeting_time": list(self.select_time),
        }
        print(meeting_data)

        return rx.redirect("/make_meeting_result")
