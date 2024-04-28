import reflex as rx

from gatherplan_client.join_meeting.join_state import JoinState
from gatherplan_client.login import LoginState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor
from gatherplan_client.reflex_assets.text_box import (
    left_align_text_box,
    check_meeting_box,
    check_meeting_box_for_each,
)


def join_login(func):
    def inner():
        return rx.cond(LoginState.login_token == "", join_meeting_not_logined(), func())

    return inner


@join_login
def join_meeting() -> rx.Component:
    return rx.vstack(
        header("약속 참여하기", "/enter_meeting_code"),
        left_align_text_box(
            "참여하려는 약속 정보를 확인해주세요",
            "약속 정보 수정은 현황보기에서 진행할 수 있습니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
            height="15%",
        ),
        rx.center(
            rx.scroll_area(
                rx.center(
                    check_meeting_box("약속이름", JoinState.meeting_name),
                    check_meeting_box(
                        "약속장소",
                        JoinState.meeting_location,
                        JoinState.select_location_detail_location,
                    ),
                    check_meeting_box_for_each(
                        "약속날짜",
                        JoinState.meeting_date,
                    ),
                    check_meeting_box_for_each(
                        "약속 후보 시간",
                        JoinState.meeting_time,
                    ),
                    check_meeting_box(
                        "모임장",
                        JoinState.host_name,
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
            height="55%",
        ),
        rx.center(
            rx.vstack(
                rx.button(
                    "로그인",
                    width="348px",
                    height="48px",
                    padding="20px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_BACKGROUND,
                    on_click=rx.redirect("/login"),
                ),
                rx.button(
                    "비회원으로 시작하기",
                    width="348px",
                    height="48px",
                    padding="20px",
                    color=AppColor.BLACK,
                    type="submit",
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    on_click=rx.redirect("/not_member_login"),
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )


def join_meeting_not_logined() -> rx.Component:
    return rx.vstack(
        header("약속 참여하기", "/enter_meeting_code"),
        left_align_text_box(
            "참여하려는 약속 정보를 확인해주세요",
            "약속 정보 수정은 현황보기에서 진행할 수 있습니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
            height="15%",
        ),
        rx.center(
            rx.scroll_area(
                rx.center(
                    check_meeting_box("약속이름", JoinState.meeting_name),
                    check_meeting_box(
                        "약속장소",
                        JoinState.meeting_location,
                        JoinState.select_location_detail_location,
                    ),
                    check_meeting_box_for_each(
                        "약속날짜",
                        JoinState.meeting_date,
                    ),
                    check_meeting_box_for_each(
                        "약속 후보 시간",
                        JoinState.meeting_time,
                    ),
                    check_meeting_box(
                        "모임장",
                        JoinState.host_name,
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
            height="55%",
        ),
        rx.center(
            rx.vstack(
                rx.button(
                    "참여하기",
                    width="348px",
                    height="48px",
                    padding="20px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_BACKGROUND,
                    on_click=rx.redirect("/enter_meeting_code"),
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
