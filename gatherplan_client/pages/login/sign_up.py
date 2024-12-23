import reflex as rx

from gatherplan_client.backend.state import EmailAuth, State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.header import header
from gatherplan_client.components.footer import footer
from gatherplan_client.components.schema import AppFontFamily, TextSize
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
    input_box,
)


def sign_up_layout(content: rx.Component) -> rx.Component:
    return rx.box(
        rx.vstack(
            header(),
            rx.hstack(
                rx.box(
                    footer(is_vertical=True),
                    width="240px",
                    height="100vh",
                    position="sticky",
                    top="0",
                    display=["none", "none", "block"],
                ),
                rx.box(
                    rx.box(
                        content,
                        width="100%",
                        max_width="600px",
                        margin="0 auto",
                        bg="white",
                        border_x="1px solid #eaeaea",
                        min_height="100vh",
                        padding_top="50px",
                    ),
                    flex="1",
                    min_height="100vh",
                ),
                width="100%",
                spacing="0",
                align_items="stretch",
            ),
            rx.box(
                footer(is_vertical=False),
                width="100%",
                position="fixed",
                bottom="0",
                left="0",
                display=["block", "block", "none"],
            ),
            height="100vh",
            spacing="0",
        ),
        bg="rgb(250, 250, 250)",
    )


@rx.page("/sign_up")
def sign_up() -> rx.Component:
    return sign_up_layout(
        rx.vstack(
            main_sub_text_center_box(
                "회원가입",
                "게더플랜에서 모임의 약속을 잡아보세요",
            ),
            rx.form(
                rx.center(
                    rx.vstack(
                        rx.text(
                            "이메일",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        rx.hstack(
                            rx.input(
                                placeholder="2~8자리",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                height="35px",
                                font_size="12px",
                                width="290px",
                                name="email",
                                on_blur=EmailAuth.set_text,
                            ),
                            rx.button(
                                "인증요청",
                                width="50px",
                                height="35px",
                                font_size="12px",
                                type="button",
                                on_click=EmailAuth.sign_up_send_auth_number,
                            ),
                            padding_bottom="20px",
                            width="345px",
                        ),
                        rx.text(
                            "인증번호",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="인증번호를 입력해주세요",
                            name="auth_number",
                        ),
                        rx.box(
                            "비밀번호",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="2~8자리",
                            name="password",
                            type="password",
                        ),
                        rx.text(
                            "닉네임",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="닉네임을 입력해주세요",
                            name="nick_name",
                        ),
                        main_button("가입하기", type="submit"),
                        width="360px",
                    ),
                    width="100%",
                ),
                on_submit=State.sign_up,
                reset_on_submit=False,
                align="center",
                width="100%",
            ),
            spacing="0",
            width="100%",
            align="center",
        )
    )
