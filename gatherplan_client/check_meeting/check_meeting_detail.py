import reflex as rx

from gatherplan_client.check_meeting.check_state import CheckState
from gatherplan_client.join_meeting.join_meeting_date import display_select_date
from gatherplan_client.login import LoginState
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import AppColor, AppFontFamily


def check_login(func):
    def inner():
        return rx.cond(
            LoginState.login_token != "", check_meeting_detail_not_logined(), func()
        )

    return inner


@check_login
def check_meeting_detail() -> rx.Component:
    return rx.vstack(
        header("/"),
        rx.center(
            rx.text(
                "약속 현황보기",
                font_size="20px",
                padding_top="28px",
                padding_bottom="40px",
                padding_left="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                width="360px",
            ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )


def check_meeting_detail_not_logined() -> rx.Component:
    return rx.vstack(
        header("/check_meeting"),
        rx.center(
            rx.text(
                "약속 만들기",
                # CheckState.detail_meeting_name,
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
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("약속 정보", value="tab1"),
                    rx.tabs.trigger("참여 정보", value="tab2"),
                ),
                rx.tabs.content(
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
                                    CheckState.meeting_name,
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
                                    CheckState.select_location_detail_location,
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
                                            CheckState.display_select_date,
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
                                    CheckState.meeting_memo,
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
                                            on_click=rx.set_clipboard(
                                                CheckState.meeting_code
                                            ),
                                            width="12px",
                                            height="12px",
                                            padding="0",
                                            color=AppColor.GRAY_TEXT,
                                            background_color=AppColor.WHITE,
                                        ),
                                    ),
                                    rx.box(
                                        rx.text(
                                            CheckState.meeting_code,
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
                                    CheckState.host_name,
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
                        padding_top="10px",
                    ),
                    rx.center(
                        rx.vstack(
                            rx.button(
                                "참여하기",
                                width="348px",
                                height="35px",
                                padding="20px",
                                color=AppColor.WHITE,
                                type="submit",
                                background_color=AppColor.MAIN_COLOR,
                                on_click=rx.redirect("/join_meeting_date"),
                            ),
                        ),
                        width="100%",
                    ),
                    rx.center(
                        rx.vstack(
                            rx.button(
                                "참여하기",
                                width="348px",
                                height="35px",
                                padding="20px",
                                color=AppColor.WHITE,
                                type="submit",
                                background_color=AppColor.MAIN_COLOR,
                                on_click=rx.redirect("/join_meeting_date"),
                            ),
                        ),
                        width="100%",
                        padding_top="10px",
                    ),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.text("item on tab 2"),
                    value="tab2",
                ),
                width="360px",
                default_value="tab1",
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
