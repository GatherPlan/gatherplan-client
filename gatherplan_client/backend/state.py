import base64
import calendar
import copy
import datetime
import json
import os
from typing import List, Dict, Any

import reflex as rx
import requests
from dateutil.relativedelta import relativedelta

DEFAULT_TIME_SETTING = {f"{hour:02}:00": 0 for hour in range(24)}
DEFAULT_TIME_SETTING["23:59"] = 0

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "https://www.gatherplan.site",
)


ADDITIONAL_HOLIDAYS = {
    2024: [
        datetime.date(2024, 2, 12),
        datetime.date(2024, 4, 10),
        datetime.date(2024, 5, 6),
    ],
    2025: [
        datetime.date(2025, 3, 3),
        datetime.date(2025, 5, 6),
    ],
    2026: [
        datetime.date(2026, 3, 2),
        datetime.date(2026, 5, 25),
        datetime.date(2026, 6, 8),
        datetime.date(2026, 8, 17),
        datetime.date(2026, 10, 5),
    ],
}


def additional_holiday(year: int) -> List[datetime.date]:
    return ADDITIONAL_HOLIDAYS.get(year, [])


def meeting_state_change(state: str):
    if state == "CONFIRMED":
        return "확정"
    elif state == "UNCONFIRMED":
        return "미확정"
    else:
        return "기타"


class State(rx.State):
    login_token: str = ""
    not_member_login: bool = False
    not_member_login_button: bool = True

    password: str = ""
    nick_name: str = ""
    auth_number: str = ""

    meeting_name: str = ""
    meeting_notice: str = ""
    meeting_code: str = ""
    input_location: str = ""

    search_location: List[Dict[str, str]] = [
        {"address_name": "", "location_type": ""}
    ]  # 백엔드로부터 받아온 데이터 ( 행정구역 )
    search_location_place: List[Dict[str, str]] = [
        {"address_name": "", "location_type": "", "place_name": "", "place_url": ""}
    ]  # 백엔드로부터 받아온 데이터 ( 상세주소 )

    meeting_location: str = ""
    meeting_location_detail: str = ""
    location_type: str = ""
    place_url: str = ""

    @rx.var
    def params_meeting_code(self) -> str:
        return self.router.page.params.get("meeting_code_params", "")

    # CalendarSelect Data
    display_data: Dict[str, bool] = {}
    holiday_data: Dict[str, str] = {}
    select_data: List[str] = []
    checked_data: Dict[str, bool] = {}
    click_date: str = ""

    setting_time = ""
    setting_time_display = ""

    host_name: str = ""
    meeting_state: str = ""

    candidate_list: List = []
    appointment_state: str = ""
    is_participated: bool = False
    is_host: bool = False
    user_participation_info_list: List = []

    check_meeting_list: List[Dict[str, str]] = []
    check_detail_meeting_code: str = ""

    meeting_date: List[str] = []
    display_select_date: List = []

    first_click_time: str = ""
    time_data_to_button_click: Dict[str, bool] = copy.copy(DEFAULT_TIME_SETTING)

    check_meeting_participants_data: List[Dict] = []
    check_meeting_participants_data_per_date: Dict = {}
    check_meeting_detail_display_clicked_date: str = ""
    check_meeting_detail_display_clicked_date_data: List[str] = []

    meeting_confirm_display_data: List[Dict[str, Any]] = []
    meeting_confirm_display_data_user: str = ""
    meeting_confirm_display_data_not_attend_user: str = ""

    confirm_date: str = ""
    confirm_start_time: str = ""
    confirm_end_time: str = ""

    def reset_location_info(self):
        self.meeting_location = ""
        self.meeting_location_detail = ""
        self.location_type = ""
        self.place_url = ""

    def change_login_not_member(self):
        self.not_member_login_button = not self.not_member_login_button

    def check_meeting_date_click_button(self, click_data: List):
        self.check_meeting_detail_display_clicked_date_data = []
        click_data_split = click_data.split("-")
        click_data_adjust = f"{click_data_split[0]}-{int(click_data_split[1]):02}-{int(click_data_split[2]):02}"

        self.check_meeting_detail_display_clicked_date = click_data_adjust
        if click_data_adjust in self.check_meeting_participants_data_per_date.keys():
            temp_data = self.check_meeting_participants_data_per_date[click_data_adjust]
            for data in temp_data:
                for key, value in data.items():
                    start_time, end_time = value.split("~")
                    start_time = start_time[:5]
                    end_time = end_time[:5]
                    result = f"{key}: {start_time}~{end_time}"
                    self.check_meeting_detail_display_clicked_date_data.append(result)
        else:
            self.check_meeting_detail_display_clicked_date_data = ["참여자가 없습니다."]

    def setting_month_calendar_and_get_check_meeting(self):
        self.check_meeting_participants_data = []
        self.check_meeting_participants_data_per_date = {}
        self.check_meeting_detail_display_clicked_date = ""
        self.check_meeting_detail_display_clicked_date_data = []
        self.setting_month_calendar()

        for date in self.candidate_list:
            temp_y, temp_m, temp_d = date.split("-")

            full_date = f"{temp_y}-{int(temp_m)}-{int(temp_d)}"
            self.display_data[full_date] = True

        if self.not_member_login:
            data = {
                "appointmentCode": self.check_detail_meeting_code,
                "tempUserInfo.nickname": self.nick_name,
                "tempUserInfo.password": self.password,
            }
            response = requests.get(
                f"{BACKEND_URL}/api/v1/temporary/appointments/participants",
                headers=HEADER,
                params=data,
            )
        else:
            data = {"appointmentCode": self.check_detail_meeting_code}
            header = HEADER
            header["Authorization"] = self.login_token
            response = requests.get(
                f"{BACKEND_URL}/api/v1/appointments/participants",
                headers=header,
                params=data,
            )

        if response.status_code == 200:
            self.check_meeting_participants_data = response.json()["data"]

            for participants in self.check_meeting_participants_data:

                for selected_date in participants["participationInfo"][
                    "selectedDateTimeList"
                ]:
                    if (
                        selected_date["selectedDate"]
                        in self.check_meeting_participants_data_per_date.keys()
                    ):
                        temp = {
                            participants["participationInfo"][
                                "nickname"
                            ]: f"{selected_date['selectedStartTime']}~{selected_date['selectedEndTime']}"
                        }
                        self.check_meeting_participants_data_per_date[
                            selected_date["selectedDate"]
                        ].append(temp)
                    else:
                        self.check_meeting_participants_data_per_date[
                            selected_date["selectedDate"]
                        ] = [
                            {
                                participants["participationInfo"][
                                    "nickname"
                                ]: f"{selected_date['selectedStartTime']}~{selected_date['selectedEndTime']}"
                            }
                        ]

    def setting_month_calendar(self, init_setting_time: bool = True):
        from pytimekr import pytimekr

        if init_setting_time:
            self.setting_time = datetime.datetime.now()
            self.setting_time_display = self.setting_time.strftime("%Y-%m")
            self.select_data = []

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
            else:
                temp_month = self.setting_time.month

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

            if type(clicked_data) == str:
                if clicked_data in self.display_data.keys():
                    self.display_data[clicked_data] = True
            else:
                if clicked_data["selectedDate"] in self.display_data.keys():
                    self.display_data[clicked_data["selectedDate"]] = True

    def make_meeting_handle_submit(self, form_data: dict):

        if len(form_data["meeting_name"]) < 2 or len(form_data["meeting_name"]) > 20:
            return rx.toast.error(
                "약속 이름은 2자 이상 20자 이하로 입력해주세요.", position="top-right"
            )

        self.meeting_name = form_data["meeting_name"]
        self.meeting_notice = form_data["meeting_memo"]

        return rx.redirect("/make_meeting_detail")

    def make_meeting_check_handle_submit(self):
        meeting_dates_dt = [
            datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            for date in list(self.select_data)
        ]

        header = HEADER
        data = {
            "appointmentName": self.meeting_name,
            "notice": self.meeting_notice,
            "address": {
                "locationType": self.location_type,
                "fullAddress": self.meeting_location_detail,
                "placeName": self.meeting_location,
                "placeUrl": self.place_url,
            },
            "candidateDateList": meeting_dates_dt,
        }

        if self.meeting_location_detail == "":
            data.pop("address")

        if self.not_member_login:
            data["tempUserInfo"] = {
                "nickname": self.nick_name,
                "password": self.password,
            }

            if self.meeting_code != "":
                data["appointmentCode"] = self.meeting_code
                response = requests.put(
                    f"{BACKEND_URL}/api/v1/temporary/appointments",
                    headers=header,
                    json=data,
                )
                return rx.redirect(f"/check_meeting_detail")

            else:
                response = requests.post(
                    f"{BACKEND_URL}/api/v1/temporary/appointments",
                    headers=header,
                    json=data,
                )
        else:
            header["Authorization"] = self.login_token

            if self.meeting_code != "":
                data["appointmentCode"] = self.meeting_code
                response = requests.put(
                    f"{BACKEND_URL}/api/v1/appointments",
                    headers=header,
                    json=data,
                )
                return rx.redirect(f"/check_meeting_detail")
            else:
                response = requests.post(
                    f"{BACKEND_URL}/api/v1/appointments", headers=header, json=data
                )

        if response.status_code == 200:
            return rx.redirect(
                f"/make_meeting_result/{response.json()['appointmentCode']}"
            )
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def make_meeting_date_click_button(self, click_data: List):
        if self.display_data[click_data]:
            self.select_data.remove(click_data)
            self.display_data[click_data] = False
        else:
            self.select_data.append(click_data)
            self.display_data[click_data] = True

    def make_meeting_date_handle_submit(self):
        if len(self.select_data) == 0:
            return rx.toast.error("날짜를 선택해주세요.", position="top-right")
        return rx.redirect("/make_meeting_check")

    def month_change_common(self, is_increment: bool):
        if is_increment:
            self.setting_time = self.setting_time + relativedelta(months=1)
        else:
            self.setting_time = self.setting_time - relativedelta(months=1)

        self.setting_time_display = self.setting_time.strftime("%Y-%m")
        self.setting_month_calendar(init_setting_time=False)

    def month_decrement(self):
        self.month_change_common(is_increment=False)

    def month_increment(self):
        self.month_change_common(is_increment=True)

    def search_location_info(self):
        params = {"keyword": self.input_location, "page": 1, "size": 10}

        if self.input_location == "":
            return rx.toast.info("검색어를 입력해주세요.", position="top-right")

        self.search_location = [
            {
                "address_name": "Loading...",
                "location_type": "INFO",
            }
        ]
        self.search_location_place = [
            {
                "place_name": "Loading...",  # {'place_name': '건대입구역 2호선'
                "place_url": "",
                "address_name": "Loading...",  # 'address_name': '서울 광진구 화양동 1',
                "location_type": "INFO",
            }
        ]
        yield

        response = requests.get(
            f"{BACKEND_URL}/api/v1/region/district", headers=HEADER, params=params
        )
        self.search_location = []

        for i in response.json()["data"]:
            data = {
                "address_name": i["addressName"],
                "location_type": i["locationType"],
            }
            self.search_location.append(data)

        if len(self.search_location) == 0:
            self.search_location = [
                {
                    "address_name": "검색 결과가 없습니다.",
                    "location_type": "INFO",
                }
            ]
            yield rx.toast.info("행정구역 검색 결과가 없습니다.", position="top-right")

        response = requests.get(
            f"{BACKEND_URL}/api/v1/region/place", headers=HEADER, params=params
        )

        self.search_location_place = []

        for i in response.json()["data"]:
            data = {
                "place_name": i["placeName"],
                "place_url": i["placeUrl"],
                "address_name": i["addressName"],
                "location_type": i["locationType"],
            }
            self.search_location_place.append(data)

        if len(self.search_location_place) == 0:
            self.search_location_place = [
                {
                    "place_name": "검색 결과가 없습니다.",  # {'place_name': '건대입구역 2호선'
                    "place_url": "",
                    "address_name": "검색 결과가 없습니다.",  # 'address_name': '서울 광진구 화양동 1',
                    "location_type": "INFO",
                }
            ]
            yield rx.toast.info("상세주소 검색 결과가 없습니다.", position="top-right")

    def make_meeting_detail_handle_location_submit(self, form_data: dict):

        if form_data["location_type"] == "INFO":
            return

        elif form_data["location_type"] == "DISTRICT":
            self.meeting_location = ""
            self.meeting_location_detail = form_data["address_name"]
            self.place_url = ""
            self.location_type = form_data["location_type"]
        else:
            self.location_type = form_data["location_type"]
            self.meeting_location = form_data["place_name"]
            self.place_url = form_data["place_url"]
            self.meeting_location_detail = form_data["address_name"]

        return

    def join_meeting_handle_submit(self, form_data: dict):
        enter_code = form_data["enter_code"]
        response = requests.get(
            f"{BACKEND_URL}/api/v1/appointments/preview",
            headers={"accept": "*/*"},
            params={"appointmentCode": enter_code},
        )
        if response.status_code == 200:
            data = response.json()
            self.meeting_name = data["appointmentName"]
            self.meeting_location = (
                data["address"]["fullAddress"] if data["address"] else ""
            )
            self.meeting_notice = data["notice"]
            self.meeting_date = data["candidateDateList"]
            self.host_name = data["hostName"]
            self.meeting_code = data["appointmentCode"]
            self.setting_month_calendar()
            self.display_select_date = []
            return rx.redirect("/join_meeting")

        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def login_handle_submit(self, form_data: dict):
        """Handle the form submit."""

        data = {
            "email": form_data["email"],
            "password": form_data["password"],
        }
        if data["email"] == "" or data["password"] == "":
            return rx.toast.error(
                "이메일과 비밀번호를 입력해주세요.", position="top-right"
            )

        response = requests.post(
            f"{BACKEND_URL}/api/v1/users/login", headers=HEADER, json=data
        )
        if response.status_code == 200:
            token = response.headers["Authorization"]
            decoded_str = json.loads(response.content.decode("utf-8"))
            self.nick_name = decoded_str["name"]
            self.login_token = token
            return (
                rx.redirect(f"{self.router.page.path}")
                if self.router.page.path != "/login"
                else rx.redirect("/")
            )
        elif response.status_code == 401:
            return rx.toast.error("로그인 실패", position="top-right")
        else:
            return rx.toast.error(response.json()["message"], position="top-right")

    def logout(self):
        self.login_token = ""
        self.nick_name = ""
        self.password = ""
        self.not_member_login = False

        self.meeting_location_detail = ""
        return [
            rx.redirect("/"),
            rx.toast.info("로그아웃 되었습니다.", position="top-right"),
        ]

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
            return [
                rx.redirect("/login"),
                rx.toast.info("회원가입이 완료되었습니다.", position="top-right"),
            ]

        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def start_not_member_login(self, form_data: dict):
        """Handle the form submit."""

        if len(form_data["nick_name"]) < 2 or len(form_data["nick_name"]) > 6:
            return rx.toast.error(
                "닉네임은 2자 이상 6자 이하로 입력해주세요.", position="top-right"
            )

        if len(form_data["password"]) < 4 or len(form_data["password"]) > 12:
            return rx.toast.error(
                "비밀번호는 4자 이상 12자 이하로 입력해주세요.", position="top-right"
            )

        self.nick_name = form_data["nick_name"]
        self.password = form_data["password"]
        self.not_member_login = True
        return (
            rx.redirect(f"{self.router.page.path}")
            if self.router.page.path != "/login"
            else rx.redirect("/")
        )

    def start_not_member_login_check_meeting(self, form_data: dict):
        """Handle the form submit."""

        if len(form_data["nick_name"]) < 2 or len(form_data["nick_name"]) > 6:
            return rx.toast.error(
                "닉네임은 2자 이상 6자 이하로 입력해주세요.", position="top-right"
            )

        if len(form_data["password"]) < 4 or len(form_data["password"]) > 12:
            return rx.toast.error(
                "비밀번호는 4자 이상 12자 이하로 입력해주세요.", position="top-right"
            )

        params = {
            "tempUserInfo.nickname": form_data["nick_name"],
            "tempUserInfo.password": form_data["password"],
            "appointmentCode": form_data["meeting_code"],
        }

        response = requests.get(
            f"{BACKEND_URL}/api/v1/temporary/appointments",
            headers=HEADER,
            params=params,
        )

        if response.status_code == 200:
            self.check_detail_meeting_code = form_data["meeting_code"]
            self.nick_name = form_data["nick_name"]
            self.password = form_data["password"]
            self.not_member_login = True
            data = response.json()
            self.meeting_name = data["appointmentName"]
            self.host_name = data["hostName"]
            self.meeting_notice = data["notice"]
            self.meeting_state = data["appointmentState"]

            self.meeting_location_detail = (
                data["address"]["fullAddress"] if data["address"] else ""
            )
            self.meeting_location = (
                data["address"]["placeName"] if data["address"] else ""
            )
            self.place_url = data["address"]["placeUrl"] if data["address"] else ""

            self.candidate_list = data["candidateDateList"]
            self.appointment_state = data["appointmentState"]
            self.is_participated = data["isParticipated"]
            self.is_host = data["isHost"]
            self.user_participation_info_list = data["userParticipationInfoList"]
            return rx.redirect("/check_meeting_detail")
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def check_get_appointments_list(self, keyword: str = None):
        if self.login_token != "":
            header = HEADER
            header["Authorization"] = self.login_token

            data = {"page": 1, "size": 15, "keyword": keyword}

            response = requests.get(
                f"{BACKEND_URL}/api/v1/appointments/list:search",
                headers=header,
                params=data,
            )
            if response.status_code == 200:
                self.check_meeting_list = []
                for data in response.json()["data"]:
                    self.check_meeting_list.append(
                        {
                            "meeting_name": data["appointmentName"],
                            "host_name": data["hostName"],
                            "meeting_code": data["appointmentCode"],
                            "meeting_state": meeting_state_change(
                                data["appointmentState"]
                            ),
                            "is_host": data["isHost"],
                            "meeting_notice": data["notice"],
                        }
                    )
            else:
                if response.status_code == 401:
                    self.login_token = ""
                else:
                    print(response.json())
                    return rx.window_alert(f"error")

    def check_get_appointments_search(self, data):
        self.check_get_appointments_list(keyword=data["keyword"])

    def check_appointments_detail(self, meeting_code: str):
        self.check_detail_meeting_code = meeting_code
        header = HEADER
        header["Authorization"] = self.login_token

        response = requests.get(
            f"{BACKEND_URL}/api/v1/appointments",
            headers=header,
            params={"appointmentCode": self.check_detail_meeting_code},
        )

        if response.status_code == 200:
            data = response.json()
            self.meeting_name = data["appointmentName"]
            self.host_name = data["hostName"]
            self.meeting_notice = data["notice"]
            self.meeting_state = data["appointmentState"]
            self.meeting_location_detail = (
                data["address"]["fullAddress"] if data["address"] else ""
            )
            self.meeting_location = (
                data["address"]["placeName"] if data["address"] else ""
            )
            self.place_url = data["address"]["placeUrl"] if data["address"] else ""
            self.candidate_list = data["candidateDateList"]
            self.appointment_state = data["appointmentState"]
            self.is_participated = data["isParticipated"]
            self.is_host = data["isHost"]
            self.user_participation_info_list = data["userParticipationInfoList"]

            return rx.redirect("/check_meeting_detail")

        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def click_time_button(self, click_time: str):
        """
        0: no click
        1: first click
        2: range
        """

        if self.time_data_to_button_click[click_time] != 0:
            self.time_data_to_button_click = copy.copy(DEFAULT_TIME_SETTING)
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

    def click_button(self, click_data: List):
        self.click_date = click_data

        self.first_click_time = ""
        self.time_data_to_button_click = copy.copy(DEFAULT_TIME_SETTING)

        for dispplay_select_date_time in self.display_select_date:
            split_data = dispplay_select_date_time.split(" ")
            if click_data == split_data[0]:
                result = [item.strip(",") for item in split_data[1:] if item]

                for time_range in result:
                    start_time, end_time = time_range.split("-")

                    temp_time = start_time

                    while temp_time <= end_time:
                        self.time_data_to_button_click[temp_time] = 2
                        temp_time = (
                            datetime.datetime.strptime(temp_time, "%H:%M")
                            + datetime.timedelta(hours=1)
                        ).strftime("%H:%M")

                        if temp_time == "00:00":
                            self.time_data_to_button_click["23:59"] = 2
                            break

        yield

    def add_meeting_schedule(self, date):
        for temp_display_select_date in self.display_select_date:
            if date in temp_display_select_date.split(" ")[0]:
                self.display_select_date.pop(
                    self.display_select_date.index(temp_display_select_date)
                )
                self.display_data[date] = False

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

        if start_time is not None:
            intervals.append({"start": start_time, "end": prev_key})

        self.display_data[date] = True

        display_select_date_temp = f"{date} "

        if len(intervals) == 0:
            self.display_data[date] = False
            return

        for interval in intervals:
            display_select_date_temp += f" {interval['start']}-{interval['end']},"

        self.display_select_date.append(display_select_date_temp[:-1])

    def join_meeting_check_handle_result_submit(self):
        header = HEADER
        for display_select_date_time in self.display_select_date:
            split_data = display_select_date_time.split(" ")
            date = split_data[0]
            result = [item.strip(",") for item in split_data[1:] if item]

            for time_range in result:
                start_time, end_time = time_range.split("-")
                select_date_temp = {
                    "selectedDate": date,
                    "selectedStartTime": start_time,
                    "selectedEndTime": end_time,
                }
                self.select_data.append(select_date_temp)

        data = {
            "appointmentCode": self.meeting_code,
            "selectedDateTimeList": self.get_value(self.select_data),
        }

        if self.not_member_login:
            data["tempUserInfo"] = {
                "nickname": self.nick_name,
                "password": self.password,
            }

            response = requests.post(
                f"{BACKEND_URL}/api/v1/temporary/appointments/join",
                headers=header,
                json=data,
            )

            if "code" in response.json().keys() and response.json()["code"] == 4001:
                response = requests.put(
                    f"{BACKEND_URL}/api/v1/temporary/appointments/join",
                    headers=header,
                    json=data,
                )
        else:
            header["Authorization"] = self.login_token
            _, jwt_nickname, _ = self.decode_jwt_payload(self.login_token)
            data["nickname"] = jwt_nickname
            response = requests.post(
                f"{BACKEND_URL}/api/v1/appointments/join",
                headers=header,
                json=data,
            )
            if "code" in response.json().keys() and response.json()["code"] == 4001:
                response = requests.put(
                    f"{BACKEND_URL}/api/v1/appointments/join",
                    headers=header,
                    json=data,
                )

        if response.status_code == 200:
            return rx.redirect(f"/join_meeting_result")
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def check_meeting_detail_delete_appointment(self):

        header = HEADER
        header["Authorization"] = self.login_token

        response = requests.delete(
            f"{BACKEND_URL}/api/v1/appointments",
            headers=header,
            params={"appointmentCode": self.check_detail_meeting_code},
        )

        if response.status_code == 200:
            return rx.redirect("/check_meeting")
        else:
            print(response.json())
            return rx.window_alert(f"error")

    def get_appointments_candidates(self):
        self.meeting_confirm_display_data = []
        self.meeting_confirm_display_data_user = ""
        self.meeting_confirm_display_data_not_attend_user = ""
        header = HEADER
        data = {
            "appointmentCode": self.check_detail_meeting_code,
            "page": 1,
            "size": 10,
        }
        if self.not_member_login:
            data["tempUserInfo.nickname"] = self.nick_name
            data["tempUserInfo.password"] = self.password

            response = requests.get(
                f"{BACKEND_URL}/api/v1/temporary/appointments/candidates",
                headers=header,
                params=data,
            )
        else:
            header["Authorization"] = self.login_token
            response = requests.get(
                f"{BACKEND_URL}/api/v1/appointments/candidates",
                headers=header,
                params=data,
            )

        if response.status_code == 200:
            data = response.json()["data"]
            for index, item in enumerate(data):

                user_list = []
                not_attend_list = []
                for user_data in item["userParticipationInfoList"]:
                    if user_data["isAvailable"]:
                        user_list.append(user_data["nickname"])
                    else:
                        not_attend_list.append(user_data["nickname"])

                temp = {
                    "index": index,
                    "date": item["candidateDate"],
                    "start_time": item["startTime"][:5],
                    "end_time": item["endTime"][:5],
                    "user_count": len(user_list),
                    "user_list": user_list,
                    "not_attend_list": not_attend_list,
                    "weather": "not_yet",
                    "click": False,
                }
                self.meeting_confirm_display_data.append(temp)
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def get_appointments_candidates_click_get_user(self, index: int):
        for item in self.meeting_confirm_display_data:
            if item["index"] == index:
                item["click"] = True
                self.meeting_confirm_display_data_user = ", ".join(item["user_list"])
                self.meeting_confirm_display_data_not_attend_user = ", ".join(
                    [""] + item["not_attend_list"]
                )
                self.confirm_date = item["date"]
                self.confirm_start_time = item["start_time"]
                self.confirm_end_time = item["end_time"]
            else:
                item["click"] = False

    def check_candidate_check_handle_submit(self):
        header = HEADER
        data = {
            "appointmentCode": self.check_detail_meeting_code,
            "confirmedDateTime": {
                "confirmedDate": self.confirm_date,
                "confirmedStartTime": self.confirm_start_time,
                "confirmedEndTime": self.confirm_end_time,
            },
        }

        if self.not_member_login:
            data["tempUserInfo"] = {
                "nickname": self.nick_name,
                "password": self.password,
            }
            response = requests.post(
                f"{BACKEND_URL}/api/v1/temporary/appointments/candidates:confirm",
                headers=header,
                data=json.dumps(data),
            )
        else:
            header["Authorization"] = self.login_token
            response = requests.post(
                f"{BACKEND_URL}/api/v1/appointments/candidates:confirm",
                headers=header,
                data=json.dumps(data),
            )

        if response.status_code == 200:
            return rx.redirect("/check_candidate_result")
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def decode_jwt_payload(self, jwt_token: str) -> tuple[str, str, str]:
        payload = jwt_token.split(".")[1]
        decoded_payload = base64.urlsafe_b64decode(payload + "==").decode("utf-8")
        data = json.loads(decoded_payload)

        id = data["id"]
        nickname = data["nickname"]
        email = data["email"]
        return id, nickname, email

    def change_join_meeting(self):
        header = HEADER
        data = {"appointmentCode": self.check_detail_meeting_code}

        if self.not_member_login:
            data["tempUserInfo.nickname"] = self.nick_name
            data["tempUserInfo.password"] = self.password
            response = requests.get(
                f"{BACKEND_URL}/api/v1/temporary/appointments/participants",
                headers=header,
                params=data,
            )
        else:
            header["Authorization"] = self.login_token
            response = requests.get(
                f"{BACKEND_URL}/api/v1/appointments/participants",
                headers=header,
                params=data,
            )

        if response.status_code == 200:
            # TODO: default value add
            self.setting_month_calendar()
            self.meeting_code = self.check_detail_meeting_code
            return rx.redirect("/make_meeting")
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def change_meeting_delete_join(self):
        header = HEADER
        data = {"appointmentCode": self.check_detail_meeting_code}

        if self.not_member_login:
            data["tempUserInfo.nickname"] = self.nick_name
            data["tempUserInfo.password"] = self.password

            response = requests.delete(
                f"{BACKEND_URL}/api/v1/temporary/appointments/join",
                headers=header,
                params=data,
            )
        else:
            header["Authorization"] = self.login_token
            response = requests.delete(
                f"{BACKEND_URL}/api/v1/appointments/join",
                headers=header,
                params=data,
            )

        if response.status_code == 200:
            return [
                rx.redirect("/"),
                rx.toast.info("약속 참여가 취소되었습니다."),
            ]
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def check_candidate_result_click_check_button(self):
        header = HEADER
        data = {"appointmentCode": self.check_detail_meeting_code}

        if self.not_member_login:
            data["tempUserInfo.nickname"] = self.nick_name
            data["tempUserInfo.password"] = self.password

            response = requests.get(
                f"{BACKEND_URL}/api/v1/temporary/appointments",
                headers=header,
                params=data,
            )
        else:
            header["Authorization"] = self.login_token
            response = requests.get(
                f"{BACKEND_URL}/api/v1/appointments",
                headers=header,
                params=data,
            )

        if response.status_code == 200:
            data = response.json()
            self.meeting_name = data["appointmentName"]
            self.host_name = data["hostName"]
            self.meeting_notice = data["notice"]
            self.meeting_state = data["appointmentState"]
            self.meeting_location_detail = (
                data["address"]["fullAddress"] if data["address"] else ""
            )
            self.meeting_location = (
                data["address"]["placeName"] if data["address"] else ""
            )
            self.place_url = data["address"]["placeUrl"] if data["address"] else ""

            self.candidate_list = data["candidateDateList"]
            self.appointment_state = data["appointmentState"]
            self.is_participated = data["isParticipated"]
            self.is_host = data["isHost"]
            self.user_participation_info_list = data["userParticipationInfoList"]
            return rx.redirect("/check_meeting_detail")
        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")

    def index_page_load(self):
        self.meeting_code = ""


class EmailAuth(rx.State):
    text: str = ""

    def sign_up_send_auth_number(self):
        response = requests.post(
            f"{BACKEND_URL}/api/v1/users/auth",
            headers=HEADER,
            json={"email": self.text},
        )
        if response.status_code == 200:
            return rx.toast.info(
                f"{self.text}로 인증번호가 전송되었습니다.", position="top-right"
            )

        else:
            print(response.json())
            return rx.toast.error(response.json()["message"], position="top-right")


# class IndexBanner(rx.State):
#     banner_list: List[Dict[str, str]] = []
#
#     def get_banner_list(self):
#         response = requests.get(
#             f"{BACKEND_URL}/api/v1/region/festivals", headers=HEADER
#         )
#         if response.status_code == 200:
#             self.banner_list = response.json()["data"]
#         else:
#             print(response.json())
#             return rx.toast.error(response.json()["message"], position="top-right")


# import asyncio
#
#
# class CallHandlerState(rx.State):
#     count: int = 0
#     progress: int = 0
#
#     async def run(self):
#         # Reset the count.
#         self.set_progress(0)
#         yield
#
#         # Count to 10 while showing progress.
#         for i in range(10):
#             # Wait and increment.
#             await asyncio.sleep(0.5)
#             self.count += 1
#
#             # Update the progress.
#             self.set_progress(i + 1)
#
#             # Yield to send the update.
#             yield

HEADER = {
    "accept": "*/*",
    "Content-Type": "application/json",
}
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://test-backed.gatherplan.site",
)
