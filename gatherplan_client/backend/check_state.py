import datetime
from typing import List, Dict

import reflex as rx
from dateutil.relativedelta import relativedelta


class CheckState(rx.State):
    meeting_list: List[Dict[str, str]] = [
        {
            "meeting_name": "맨땅에 헤딩",
            "host_name": "박승일",
            "meeting_notice": "점심약속입니다.",
            "meeting_state": "확정",
        },
        {
            "meeting_name": "좀 보자 친구들",
            "host_name": "박정빈",
            "meeting_notice": "빨리 참여안하면 때림",
            "meeting_state": "확정",
        },
        {
            "meeting_name": "연구식 회식",
            "host_name": "이재훈",
            "meeting_notice": "점심",
            "meeting_state": "미정",
        },
    ]
    detail_meeting_name: str = ""

    meeting_name: str = "맨땅에 헤딩"
    select_location_detail_location: str = "서울특별 성동구 성수동"
    display_select_date: List = ["05/13", "05/15"]
    meeting_memo: str = "점심약속입니다~~"
    meeting_code: str = "test_code123"
    host_name: str = "이재훈"

    click_date: str = ""
    setting_time = datetime.datetime.now()
    setting_time_display = setting_time.strftime("%Y-%m")
    display_data: Dict[str, bool] = {}

    checked_data: Dict[str, bool] = {}
    holiday_data: Dict[str, str] = {}

    # test
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

    def handle_detail_submit(self, meeting_name: str):
        for meeting in self.meeting_list:
            if meeting["meeting_name"] == meeting_name:
                return meeting
        return None

    def handle_meeting_detail(self, meeting_name: str):
        self.detail_meeting_name = meeting_name
        return rx.redirect("/check_meeting_detail")

    def month_decrement(self):
        self.setting_time = self.setting_time - relativedelta(months=1)
        self.setting_time_display = self.setting_time.strftime("%Y-%m")
        self._setting_month_calendar()

    def month_increment(self):
        self.setting_time = self.setting_time + relativedelta(months=1)
        self.setting_time_display = self.setting_time.strftime("%Y-%m")
        self._setting_month_calendar()

    def click_button(self, click_data: List):
        self.click_date = click_data

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
