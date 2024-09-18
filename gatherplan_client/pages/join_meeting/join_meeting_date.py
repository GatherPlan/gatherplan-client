import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.calendar import display_select_date, calendar_header
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.pages.login.login import need_login


@rx.page(
    route="/join_meeting_date",
    on_load=State.setting_month_calendar,
)
@need_login
def join_meeting_date() -> rx.Component:
    return rx.vstack(
        header("/join_meeting"),
        rx.center(
            rx.text(
                "약속 참여하기",
                font_size="20px",
                padding_top="28px",
                padding_bottom="40px",
                padding_left="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                width="360px",
            ),
            width="100%",
            height="10%",
        ),
        rx.center(
            rx.vstack(
                rx.text(
                    "약속 참여 일정",
                    font_size="14px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_left="10px",
                ),
                rx.text(
                    "참여가능한 날짜와 시간을 선택해주세요",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                    padding_left="10px",
                    padding_top="5px",
                ),
                width="360px",
            ),
            width="100%",
        ),
        calendar_header(),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.text(
                        "선택한 일정",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                        padding_left="10px",
                    ),
                    width="360px",
                ),
                rx.scroll_area(
                    rx.flex(
                        rx.foreach(
                            State.display_select_date,
                            display_select_date,
                        ),
                        direction="column",
                        spacing="4",
                    ),
                    type="always",
                    scrollbars="vertical",
                    style={"height": 140, "width": 360},
                ),
            ),
            width="100%",
            height="30%",
        ),
        rx.center(
            rx.button(
                "선택완료",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=rx.redirect("/join_meeting_check"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
