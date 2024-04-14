import reflex as rx

from gatherplan_client.reflex_assets.buttons import index_button
from gatherplan_client.reflex_assets.schema import AppColor
from gatherplan_client.reflex_assets.text_box import left_align_text_box
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.header import header, main_header


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        main_header("Gather Plan"),
        buffer_box("5%"),
        left_align_text_box(
            "새로운 모임을 계획해보세요",
            "서로 가능한 날짜를 선택하여 모임 날짜를 조정해보세요",
        ),
        rx.vstack(
            index_button(
                main_text="만들기",
                sub_text="새로운 약속을 생성해보세요",
                redirect_url="/make_meeting",
            ),
            index_button(
                main_text="현황보기", sub_text="누가 참석할 수 있는지 확인해보세요"
            ),
            index_button(main_text="참여하기", sub_text="약속에 참여해보세요"),
            width="100%",
            height="50%",
            align="center",
        ),
        spacing="0",
        height="100vh",
        background_color=AppColor.WHITE,
    )
