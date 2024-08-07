import reflex as rx

from gatherplan_client.pages.join_meeting.join_meeting_date import display_select_date
from gatherplan_client.backend.join_state import JoinState
from gatherplan_client.pages.login.login import need_login
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppColor, AppFontFamily


@need_login
def join_meeting_result(login_token, nick_name) -> rx.Component:
    return rx.vstack(
        header("/"),
        rx.center(
            rx.vstack(
                rx.text(
                    "정상적으로 약속에 참여했습니다.",
                    font_size="18px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    align="center",
                    width="360px",
                ),
                rx.text(
                    "약속 참여 정보 변경은 약속 현황보기에서 가능합니다.",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                    align="center",
                    width="360px",
                ),
            ),
            width="100%",
            height="20%",
        ),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.text(
                        "약속이름",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        JoinState.meeting_name,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
                    rx.text(
                        "약속장소",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        JoinState.meeting_location,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
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
                        rx.flex(
                            rx.foreach(
                                JoinState.display_select_date,
                                display_select_date,
                            ),
                            direction="column",
                            spacing="4",
                        ),
                    ),
                    width="100%",
                ),
                rx.box(
                    rx.text(
                        "공지사항",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        JoinState.meeting_memo,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "약속코드",
                                font_size="12px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.GRAY_TEXT,
                            ),
                            rx.button(
                                rx.icon("copy"),
                                on_click=rx.set_clipboard(JoinState.appointment_code),
                                width="12px",
                                height="12px",
                                padding="0",
                                color=AppColor.GRAY_TEXT,
                                background_color=AppColor.WHITE,
                            ),
                        ),
                        rx.box(
                            rx.text(
                                JoinState.appointment_code,
                                font_size="14px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                color=AppColor.BLACK,
                                font_weight="700",
                                width="170px",
                            ),
                        ),
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
                    rx.text(
                        "모임장",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        JoinState.host_name,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
            ),
            width="100%",
            height="60%",
        ),
        rx.center(
            rx.button(
                "약속 현황보기",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=rx.redirect("/check_meeting"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
