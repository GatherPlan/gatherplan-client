from typing import List

import reflex as rx


class JoinState(rx.State):
    meeting_code: str = ""
    meeting_name: str = ""
    meeting_location: str = ""
    select_location_detail_location: str = ""
    meeting_date: List[str] = []
    meeting_time: List[str] = []
    host_name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
