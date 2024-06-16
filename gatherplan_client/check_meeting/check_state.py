from typing import List, Dict

import reflex as rx


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

    def handle_detail_submit(self, meeting_name: str):
        print("test")
        for meeting in self.meeting_list:
            if meeting["meeting_name"] == meeting_name:
                return meeting
        return None

    def handle_meeting_detail(self, meeting_name: str):
        self.detail_meeting_name = meeting_name
        return rx.redirect("/check_meeting_detail")
