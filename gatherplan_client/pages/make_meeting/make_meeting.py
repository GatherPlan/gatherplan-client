import reflex as rx

from gatherplan_client.pages.login.login import need_login
from gatherplan_client.backend.make_meeting_state import MakeMeetingNameState
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily, AppColor


@need_login
def make_meeting(login_token, nick_name) -> rx.Component:
    return rx.vstack(
        header("/"),  # 5%
        rx.center(
            rx.text(
                "약속 만들기",
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
        rx.form(
            rx.center(
                rx.vstack(
                    rx.text(
                        "약속 이름",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                        padding_left="10px",
                    ),
                    rx.text(
                        "상대방이 이해하기 좋은 이름으로 만들어요!",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_left="10px",
                        padding_top="5px",
                    ),
                    rx.box(
                        rx.input(
                            placeholder="약속이름을 입력해주세요",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            name="meeting_name",
                            font_size="12px",
                            height="35px",
                            type="text",
                        ),
                        width="348px",
                        padding_top="10px",
                        padding_left="10px",
                        height="60px",
                    ),
                    width="360px",
                ),
                width="100%",
            ),
            rx.center(
                rx.vstack(
                    rx.text(
                        "공지사항",
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                        padding_left="10px",
                    ),
                    rx.text(
                        "참여자에게 알려줄 내용을 간단히 작성해보세요!",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_left="10px",
                        padding_top="5px",
                    ),
                    rx.box(
                        rx.input(
                            placeholder="선택사항",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            name="meeting_memo",
                            font_size="12px",
                            height="35px",
                            type="text",
                        ),
                        width="348px",
                        padding_top="10px",
                        padding_left="10px",
                        height="60px",
                    ),
                    width="360px",
                ),
                width="100%",
            ),
            rx.box(width="100%", height="35%"),
            rx.center(
                rx.button(
                    "다음",
                    width="348px",
                    height="35px",
                    padding_left="10px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_COLOR,
                ),
                width="100%",
            ),
            on_submit=MakeMeetingNameState.handle_submit,
            width="100%",
            height="80%",
            align="center",
        ),
        spacing="0",
        height="100vh",
    )
