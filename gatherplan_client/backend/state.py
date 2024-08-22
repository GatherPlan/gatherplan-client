import json
from typing import List, Dict
from dateutil.relativedelta import relativedelta

import reflex as rx
import requests
import datetime
from pytimekr import pytimekr
from gatherplan_client.backend.additional_holiday import additional_holiday
import calendar

from gatherplan_client.backend.backend_rouuter import BACKEND_URL, HEADER


class EnterCodeState(rx.State):
    @rx.var
    def meeting_code(self) -> str:
        return self.router.page.params.get("meeting_code", "")

class State(rx.State):
    form_data: dict = {}
    email: str = ""
    password: str = ""
    login_token: str = ""
    nick_name: str = ""
    auth_number: str = ""
    error_message: str = ""

    # make_meeting
    meeting_name: str = ""
    meeting_memo: str = ""
    input_location: str = ""
    search_location: List[str] = ["Loading..."]
    search_location_place: List[str] = ["Loading..."]
    select_location: str = ""
    select_location_detail_location: str = ""

    # CalendarSelect Data
    display_data: Dict[str, bool] = {}
    holiday_data: Dict[str, str] = {}
    select_data: List[str] = []

    setting_time = datetime.datetime.now()
    setting_time_display = setting_time.strftime("%Y-%m")

    # MeetingCode Data
    meeting_code: str = "오버라이딩테스트"

    host_name: str = ""
    meeting_notice: str = ""
    meeting_state: str = ""
    address: str = ""
    candidate_list: List = []
    appointment_state: str = ""
    is_participated: bool = False
    is_host: bool = False
    user_participation_info_list: List = []

    check_meeting_list: List[Dict[str, str]] = []
    check_detail_meeting_code: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

    def make_meeting_handle_submit(self, form_data: dict):
        self.meeting_name = form_data.get("meeting_name")
        self.meeting_memo = form_data.get("meeting_memo")
        return rx.redirect("/make_meeting_detail")

    def make_meeting_check_handle_submit(self, login_token):
        meeting_dates_dt = [
            datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            for date in list(self.select_data)
        ]
        header = HEADER
        header["Authorization"] = login_token

        # TODO: address 수정 필요
        data = {
            "appointmentName": self.meeting_name,
            "notice": self.meeting_memo,
            "address": {
                "locationType": "DETAIL_ADDRESS",
                "fullAddress": self.select_location,
                "placeName": "성수역 2호선 2번출구",
                "placeUrl": "http://place.map.kakao.com/7942972",
            },
            "candidateDateList": meeting_dates_dt,
        }

        response = requests.post(
            f"{BACKEND_URL}/api/v1/appointments", headers=header, json=data
        )

        if response.status_code == 200:
            return rx.redirect(
                f"/make_meeting_result/{response.json()['appointmentCode']}"
            )

        else:
            print(response.json())
            return rx.window_alert(f"error")

    def make_meeting_date_click_button(self, click_data: List):
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

    def search_location_info(self):

        params = {"keyword": self.input_location, "page": 1, "size": 10}

        response = requests.get(
            f"{BACKEND_URL}/api/v1/region/district", headers=HEADER, params=params
        )
        self.search_location = [i["address"] for i in response.json()["data"]]

        response = requests.get(
            f"{BACKEND_URL}/api/v1/region/place", headers=HEADER, params=params
        )

        self.search_location_place = [i["placeName"] for i in response.json()["data"]]

    def make_meeting_detail_handle_detail_submit(self, form_data: dict):
        return rx.redirect("/make_meeting_date")

    def make_meeting_detail_handle_location_submit(self, form_data: dict):
        """Handle the form submit."""
        self.select_location = form_data.get("input_location")

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

        if self.login():
            self.error_message = ""

            return rx.redirect(f"{self.router.page.path}")
        else:
            self.error_message = "로그인 실패"
            return None

    def handle_submit_join_meeting(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

        if self.login():
            self.error_message = ""
            return rx.redirect("/join_meeting")
        else:
            self.error_message = "로그인 실패"
            return None

    def login(self):
        data = {
            "email": self.form_data["email"],
            "password": self.form_data["password"],
        }
        response = requests.post(
            f"{BACKEND_URL}/api/v1/users/login", headers=HEADER, json=data
        )

        if response.status_code == 200:
            token = response.headers["Authorization"]
            decoded_str = json.loads(response.content.decode("utf-8"))
            self.nick_name = decoded_str["name"]
            self.login_token = token

            return True
        else:
            return False

    def sign_up(self, form_data: dict):
        """Handle the form submit."""

        data = {
            "email": form_data["email"],
            "authCode": form_data["auth_number"],
            "name": form_data["nick_name"],
            "password": form_data["password"],
        }

        response = requests.post(
            f"{BACKEND_URL}/api/v1/users/join", headers=HEADER, json=data
        )

        if response.status_code == 200:
            return rx.redirect("/login")

        else:
            print(response.json())
            self.error_message = "error"

    def start_not_member_login(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

        return rx.redirect("/join_meeting_date")

    def check_get_appointments_list(self, keyword: str = None):

        if self.login_token != "":
            header = HEADER
            header["Authorization"] = self.login_token

            data = {"page": 1, "size": 10, "keyword": keyword}


            response = requests.get(
                f"{BACKEND_URL}/api/v1/appointments/list:search", headers=header, params=data
            )
            if response.status_code == 200:
                self.check_meeting_list = []
                for data in response.json()["data"]:
                    self.check_meeting_list.append(
                        {
                            "meeting_name": data["appointmentName"],
                            "host_name": data["hostName"],
                            "meeting_code": data["appointmentCode"],
                            "meeting_state": data["appointmentState"],
                            "is_host": data["isHost"],
                            "meeting_notice": data["notice"]
                        })

    def check_get_appointments_search(self, data):
        self.check_get_appointments_list(keyword=data["keyword"])

    def check_appointments_detail(self, meeting_code: str):
        self.check_detail_meeting_code = meeting_code
        header = HEADER
        header["Authorization"] = self.login_token

        response = requests.get(
            f"{BACKEND_URL}/api/v1/appointments", headers=header, params={"appointmentCode":self.check_detail_meeting_code}
        )

        if response.status_code == 200:
            self.meeting_name = response.json()["appointmentName"]
            self.host_name = response.json()["hostName"]
            self.meeting_notice = response.json()["notice"]
            self.meeting_state = response.json()["appointmentState"]
            # self.address = response.json()["address"]
            self.address = ""
            self.candidate_list = response.json()["candidateDateList"]
            self.appointment_state = response.json()["appointmentState"]
            self.is_participated = response.json()["isParticipated"]
            self.is_host = response.json()["isHost"]
            self.user_participation_info_list = response.json()["userParticipationInfoList"]
            return rx.redirect("/check_meeting_detail")
