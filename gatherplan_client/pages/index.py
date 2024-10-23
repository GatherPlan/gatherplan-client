import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import index_button
from gatherplan_client.components.schema import AppColor, TextSize, AppFontFamily
from gatherplan_client.components.text_box import main_sub_text_box
from gatherplan_client.templates.template import template


@template(
    route="/",
    header_url="",
    page_text="",
    need_login_type="no_login",
    on_load=State.get_banner_list,
)
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
            main_sub_text_box(
                "새로운 모임을 계획해보세요",
                "서로 가능한 날짜를 선택하여 모임 날짜를 조정해보세요",
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
        rx.cond(
            State.is_hydrated,
            rx.vstack(
                rx.box(
                    rx.text(
                        "이런 모임은 어떠세요?",
                        font_size=TextSize.TINY_SMALL,
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                        padding_left="10px",
                        padding_bottom="5px",
                    ),
                    width="360px",
                ),
                rx.image(
                    src=State.banner_img,
                    width="320px",
                    height="180px",
                    border_radius="15px 50px",
                    border="5px solid #555",
                ),
                rx.text(
                    State.banner_name,
                    font_size=TextSize.TINY,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                ),
                rx.text(
                    State.banner_location,
                    font_size=TextSize.VERY_TINY,
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                ),
                width="100%",
                height="40vh",
                align="center",
                spacing="0",
            ),
            rx.spacer(height="40vh"),
        ),
        width="100%",
        height="100%",
    )


# Test Commit
