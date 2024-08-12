import json
from typing import List, Dict

import reflex as rx
import requests

from gatherplan_client.backend.backend_rouuter import BACKEND_URL, HEADER


class State(rx.State):
    form_data: dict = {}
    email: str = ""
    password: str = ""
    login_token: str = ""
    nick_name: str = ""
    auth_number: str = ""
    error_message: str = ""

    check_meeting_list: List[Dict[str, str]] = []
    check_detail_meeting_code: str = ""

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
        return rx.redirect("/check_meeting_detail")

