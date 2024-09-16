import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import text_for_each
from gatherplan_client.pages.login.login import need_login


@need_login
def make_meeting_check() -> rx.Component:

    return rx.vstack(
        header("/make_meeting_date"),
        rx.center(
            rx.vstack(
                rx.text(
                    "선택한 약속 정보를 확인해주세요",
                    font_size="18px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    align="center",
                    width="360px",
                ),
                rx.text(
                    "약속 정보 변경은 약속 현황보기에서 가능합니다.",
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
                        State.meeting_name,
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
                        State.select_location_detail_location,
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
                            rx.foreach(State.select_data, text_for_each),
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
                        State.meeting_memo,
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
                "약속 만들기",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=State.make_meeting_check_handle_submit,
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
