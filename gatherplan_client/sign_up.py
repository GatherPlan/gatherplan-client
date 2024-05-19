import reflex as rx

from gatherplan_client.login import LoginState
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.buttons import (
    basic_button,
)
from gatherplan_client.reflex_assets.form_box import form_box, form_box_with_button
from gatherplan_client.reflex_assets.text_box import center_align_text_box
from gatherplan_client.reflex_assets.header import header


def sign_up() -> rx.Component:

    return rx.vstack(
        header("/login"),
        buffer_box("8%"),
        center_align_text_box(
            main_text="회원가입", sub_text="게더플랜에서 모임의 약속을 잡아보세요"
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    form_box_with_button(
                        explain_text="이메일",
                        placeholder_text="2~8자리",
                        form_value="email",
                    ),
                    form_box(
                        explain_text="인증번호",
                        placeholder_text="인증번호를 입력해주세요",
                        form_value="auth_number",
                        type="text",
                    ),
                    form_box(
                        explain_text="비밀번호",
                        placeholder_text="비밀번호를 입력해주세요",
                        form_value="password",
                        type="password",
                    ),
                    form_box(
                        explain_text="닉네임",
                        placeholder_text="닉네임을 입력해주세요",
                        form_value="nick_name",
                        type="password",
                    ),
                    rx.center(
                        LoginState.error_message,
                        font_size="12px",
                        color="#FF0000",
                        width="100%",
                        padding_bottom="30px",
                    ),
                    basic_button("가입"),
                    on_submit=LoginState.sign_up,
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
