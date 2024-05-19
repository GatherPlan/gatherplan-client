import reflex as rx

from gatherplan_client.login import LoginState
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.buttons import (
    basic_button,
)
from gatherplan_client.reflex_assets.header import header

from gatherplan_client.reflex_assets.form_box import form_box
from gatherplan_client.reflex_assets.text_box import center_align_text_box


def not_member_login() -> rx.Component:

    return rx.vstack(
        header("/"),
        buffer_box("8%"),
        center_align_text_box(
            main_text="회원 정보를 입력해주세요",
            sub_text="호스트가 알아보기 쉬운 닉네임을 사용해보세요",
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    form_box(
                        explain_text="닉네임",
                        placeholder_text="인증번호를 입력해주세요",
                        form_value="nick_name",
                        type="text",
                    ),
                    form_box(
                        explain_text="비밀번호",
                        placeholder_text="비밀번호를 입력해주세요",
                        form_value="password",
                        type="password",
                    ),
                    rx.center(
                        LoginState.error_message,
                        font_size="12px",
                        color="#FF0000",
                        width="100%",
                        padding_bottom="120px",
                    ),
                    basic_button("시작하기"),
                    on_submit=LoginState.start_not_member_login,
                    reset_on_submit=True,
                    align="center",
                    width="345px",
                ),
            ),
            width="100%",
            height="80%",
        ),
        spacing="0",
        height="100vh",
    )
