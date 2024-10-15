import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.calendar import calendar_header
from gatherplan_client.components.schema import AppColor
from gatherplan_client.components.text_box import main_sub_text_box
from gatherplan_client.templates.template import template


@template(
    route="/make_meeting_date",
    page_text="약속 만들기",
    header_url="/make_meeting_detail",
    on_load=State.setting_month_calendar,
)
def make_meeting_date() -> rx.Component:
    return rx.center(
        rx.vstack(
            main_sub_text_box(
                "약속 후보 날짜", "최대 10일까지 선택가능합니다.", need_start=True
            ),
            calendar_header(purpose="make"),
            rx.box(height="15vh"),
            rx.button(
                "다음",
                width="360px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=State.make_meeting_date_handle_submit,
            ),
            width="360px",
        ),
        width="100%",
    )
