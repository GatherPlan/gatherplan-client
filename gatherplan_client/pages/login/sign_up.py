import reflex as rx

from gatherplan_client.backend.state import State, EmailAuth
from gatherplan_client.components.buffer_box import buffer_box
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily, AppColor
from gatherplan_client.components.text_box import center_align_text_box


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
                    rx.box(
                        rx.text(
                            "이메일",
                            font_size="10px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="2~8자리",
                                on_blur=EmailAuth.set_text,
                                font_size="16px",
                                height="48px",
                                border_radius="35px",
                                width="290px",
                                name="email",
                            ),
                            rx.button(
                                "인증요청",
                                width="50px",
                                height="48px",
                                type="button",
                                on_click=EmailAuth.sign_up_send_auth_number,
                            ),
                            padding_bottom="20px",
                            width="345px",
                        ),
                    ),
                    rx.box(
                        rx.text(
                            "인증번호",
                            font_size="10px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                        ),
                        rx.input(
                            placeholder="인증번호를 입력해주세요",
                            name="auth_number",
                            font_size="16px",
                            height="48px",
                            border_radius="35px",
                            type="text",
                        ),
                        padding_bottom="20px",
                        width="345px",
                    ),
                    rx.box(
                        rx.text(
                            "비밀번호",
                            font_size="10px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                        ),
                        rx.input(
                            placeholder="비밀번호를 입력해주세요",
                            name="password",
                            font_size="16px",
                            height="48px",
                            border_radius="35px",
                            type="password",
                        ),
                        padding_bottom="20px",
                        width="345px",
                    ),
                    rx.box(
                        rx.text(
                            "닉네임",
                            font_size="10px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                        ),
                        rx.input(
                            placeholder="닉네임을 입력해주세요",
                            name="nick_name",
                            font_size="16px",
                            height="48px",
                            border_radius="35px",
                            type="text",
                        ),
                        padding_bottom="20px",
                        width="345px",
                    ),
                    rx.center(
                        State.error_message,
                        font_size="12px",
                        color="#FF0000",
                        width="100%",
                        padding_bottom="30px",
                    ),
                    rx.button(
                        "가입하기",
                        width="348px",
                        height="48px",
                        padding="20px",
                        color=AppColor.WHITE,
                        type="submit",
                        background_color=AppColor.MAIN_COLOR,
                    ),
                    on_submit=State.sign_up,
                    reset_on_submit=False,
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
