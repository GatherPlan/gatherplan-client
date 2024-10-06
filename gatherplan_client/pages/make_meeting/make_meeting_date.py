import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.calendar import calendar_header
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.templates.template import template


@template(
    route="/make_meeting_date",
    page_text="약속 만들기",
    header_url="/make_meeting_detail",
    on_load=State.setting_month_calendar,
)
def make_meeting_date() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.text(
                "약속 후보 날짜",
                font_size="14px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                color=AppColor.BLACK,
                padding_left="10px",
                width="360px",
            ),
            width="100%",
        ),
        rx.center(
            rx.text(
                "최대 10일까지 선택가능합니다.",
                font_size="12px",
                font_family=AppFontFamily.DEFAULT_FONT,
                color=AppColor.GRAY_TEXT,
                font_weight="700",
                padding_left="10px",
                width="360px",
            ),
            width="100%",
        ),
        rx.box(height="30%"),
        calendar_header(purpose="make", height="55%"),
        rx.center(
            rx.button(
                "다음",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=rx.redirect("/make_meeting_check"),
            ),
            width="100%",
        ),
        width="100%",
    )
