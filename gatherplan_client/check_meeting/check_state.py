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

    def handle_detail_submit(self, meeting_name: str):
        for meeting in self.meeting_list:
            if meeting["meeting_name"] == meeting_name:
                return meeting
        return None
