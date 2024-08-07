import reflex as rx

from gatherplan_client.backend.backend_rouuter import FRONTEND_URL
from gatherplan_client.pages.join_meeting.enter_meeting_code import EnterCodeState
from gatherplan_client.pages.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import (
    text_for_each,
)


def make_meeting_result() -> rx.Component:
    return rx.vstack(
        header("/make_meeting_check"),
        rx.center(
            rx.vstack(
                rx.text(
                    "정상적으로 약속이 생성되었습니다.",
                    font_size="18px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    align="center",
                    width="360px",
                ),
                rx.text(
                    "약속 정보를 확인하고 참여자들에게 공유해보세요.",
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
                        MakeMeetingNameState.meeting_name,
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
                        MakeMeetingNameState.select_location,
                        # MakeMeetingNameState.select_location_detail_location,
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
                        "약속 후보 날짜",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.box(
                        # TODO: string formating 수정 필요
                        rx.hstack(
                            rx.foreach(MakeMeetingNameState.select_data, text_for_each),
                            width="360px",
                        )
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
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
                        MakeMeetingNameState.meeting_memo,
                        # MakeMeetingNameState.select_location_detail_location,
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
                                on_click=rx.set_clipboard(EnterCodeState.meeting_code),
                                width="12px",
                                height="12px",
                                padding="0",
                                color=AppColor.GRAY_TEXT,
                                background_color=AppColor.WHITE,
                            ),
                        ),
                        rx.box(
                            rx.text(
                                EnterCodeState.meeting_code,
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
            ),
            width="100%",
            height="50%",
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
                    on_click=rx.redirect(
                        f"/enter_meeting_code/{EnterCodeState.meeting_code}"
                    ),
                ),
                rx.button(
                    "공유하기",
                    width="348px",
                    height="35px",
                    padding="20px",
                    color=AppColor.BLACK,
                    on_click=rx.set_clipboard(
                        f"{FRONTEND_URL}/enter_meeting_code/{EnterCodeState.meeting_code}"
                    ),
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    margin_top="20px",
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
