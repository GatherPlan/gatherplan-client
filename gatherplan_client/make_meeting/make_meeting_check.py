import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.make_meeting.make_meeting_date import CalendarSelect
from gatherplan_client.make_meeting.make_meeting_timeline import TimeSelect
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor, AppFontFamily
from gatherplan_client.reflex_assets.text_box import (
    left_align_text_box,
    check_meeting_box,
    check_meeting_box_for_each,
)


class MakeMeeting(rx.State):
    """The app state."""

    meeting_name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meeting_name = MakeMeetingNameState.meeting_name.to_string()

    def handle_submit(self):
        meeting_data = {
            "meeting_name": self.meeting_name,
            # "meeting_location": MakeMeetingNameState.select_location.to_string(),
            # "meeting_location_detail": MakeMeetingNameState.select_location_detail_location.to_string(),
            # "meeting_date": CalendarSelect.select_data.to_string(),
            # "meeting_time": TimeSelect.select_time.to_string(),
        }
        print(meeting_data)

        return rx.redirect("/")


@need_login
def make_meeting_check() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속 정보를 확인해주세요",
            "약속 정보 수정은 현황보기에서 진행할 수 있습니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
            height="15%",
        ),
        rx.center(
            rx.scroll_area(
                rx.center(
                    check_meeting_box("약속이름", MakeMeetingNameState.meeting_name),
                    check_meeting_box(
                        "약속장소",
                        MakeMeetingNameState.select_location,
                        MakeMeetingNameState.select_location_detail_location,
                    ),
                    check_meeting_box_for_each(
                        "약속날짜",
                        CalendarSelect.select_data,
                    ),
                    check_meeting_box_for_each(
                        "약속 후보 시간",
                        TimeSelect.select_time,
                    ),
                    direction="column",
                    spacing="3",
                ),
                type="scroll",
                scrollbars="vertical",
                style={
                    "width": "360px",
                    "padding": "10px",
                },
            ),
            width="100%",
            height="60%",
        ),
        buffer_box("5%"),
        rx.center(
            rx.button(
                "다음",
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_BACKGROUND,
                on_click=CalendarSelect.handle_submit,
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
