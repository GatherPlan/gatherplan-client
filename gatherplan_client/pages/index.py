import reflex as rx

from gatherplan_client.components.buttons import index_button
from gatherplan_client.components.schema import AppColor, TextSize, AppFontFamily


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.image(
                src="/images/index_logo.png",
                width="300px",
                height="60px",
                margin_top="15px",
                margin_bottom="15px",
            ),
            width="100%",
            height="15%",
            align="center",
        ),
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text(
                        "새로운 모임을 계획해보세요",
                        font_size=TextSize.TINY_SMALL,
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                        padding_left="10px",
                    ),
                    rx.text(
                        "서로 가능한 날짜를 선택하여 모임 날짜를 조정해보세요",
                        font_size=TextSize.TINY,
                        font_family=AppFontFamily.DEFAULT_FONT,
                        color=AppColor.GRAY_TEXT,
                        font_weight="700",
                        padding_left="10px",
                    ),
                ),
                width="360px",
            ),
            index_button(
                main_text="만들기",
                sub_text="새로운 약속을 생성해보세요",
                redirect_url="/make_meeting",
            ),
            index_button(
                main_text="참여하기",
                sub_text="약속에 참여해보세요",
                redirect_url="/enter_meeting_code",
            ),
            index_button(
                main_text="현황보기",
                sub_text="누가 참석할 수 있는지 확인해보세요",
                redirect_url="/check_meeting",
            ),
            width="100%",
            height="50%",
            align="center",
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    "이런 모임은 어떠세요?",
                    font_size=TextSize.TINY_SMALL,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    padding_left="10px",
                ),
                width="360px",
            ),
            rx.video(
                url="https://youtu.be/yLupcG_eFag",
                width="330px",
                height="185px",
                align="center",
            ),
            width="100%",
            height="35%",
            align="center",
        ),
        spacing="0",
        height="100vh",
        background_color=AppColor.WHITE,
    )
