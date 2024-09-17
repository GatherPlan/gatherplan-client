import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buffer_box import buffer_box
from gatherplan_client.components.buttons import (
    basic_button,
    small_button,
)
from gatherplan_client.components.form_box import form_box
from gatherplan_client.components.schema import AppColor, TextSize, AppFontFamily
from gatherplan_client.components.text_box import center_align_text_box


def need_login(func):
    def inner():
        return rx.cond(
            State.is_hydrated,
            rx.cond(
                State.login_token == "",
                rx.cond(State.not_member_login, func(), login()),
                func(),
            ),
            rx.spinner("로그인 중입니다..."),
        )

    return inner


def login() -> rx.Component:
    return rx.vstack(
        buffer_box("8%"),
        center_align_text_box(
            main_text="Gather Plan", sub_text="게더플랜에서 모임의 약속을 잡아보세요"
        ),
        rx.cond(
            State.login_not_member,
            rx.center(
                rx.vstack(
                    rx.form(
                        rx.box(
                            rx.text(
                                "이메일",
                                font_size=TextSize.VERY_TINY,
                                font_family=AppFontFamily.DEFAULT_FONT,
                            ),
                            rx.input(
                                placeholder="email@naver.com",
                                name="email",
                                font_size=TextSize.SMALL,
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
                                font_size=TextSize.VERY_TINY,
                                font_family=AppFontFamily.DEFAULT_FONT,
                            ),
                            rx.input(
                                placeholder="2~8자리",
                                name="password",
                                font_size=TextSize.SMALL,
                                height="48px",
                                border_radius="35px",
                                type="password",
                            ),
                            padding_bottom="20px",
                            width="345px",
                        ),
                        rx.button(
                            "로그인",
                            width="348px",
                            height="48px",
                            padding="20px",
                            color=AppColor.WHITE,
                            type="submit",
                            background_color=AppColor.MAIN_COLOR,
                        ),
                        rx.hstack(
                            rx.button(
                                "아이디 찾기",
                                width="110px",
                                height="36px",
                                color="#A3A3A3",
                                type="button",
                                background_color="#FFFFFF",
                                on_click=rx.toast.error(
                                    "아이디 찾기 기능은 준비 중입니다."
                                ),
                            ),
                            rx.button(
                                "비밀번호 찾기",
                                width="110px",
                                height="36px",
                                color="#A3A3A3",
                                type="button",
                                background_color="#FFFFFF",
                                on_click=rx.toast.error(
                                    "비밀번호 찾기 기능은 준비 중입니다."
                                ),
                            ),
                            small_button("회원가입", "/sign_up"),
                            padding_top="10px",
                            width="100%",
                        ),
                        on_submit=State.login_handle_submit,
                        reset_on_submit=False,
                        align="center",
                        width="345px",
                    ),
                ),
                width="100%",
                height="60%",
            ),
            rx.center(
                rx.vstack(
                    rx.form(
                        form_box(
                            explain_text="닉네임",
                            placeholder_text="닉네임을 입력해주세요",
                            form_value="nick_name",
                            type="text",
                        ),
                        form_box(
                            explain_text="비밀번호",
                            placeholder_text="비밀번호를 입력해주세요",
                            form_value="password",
                            type="password",
                        ),
                        basic_button("시작하기"),
                        on_submit=State.start_not_member_login,
                        reset_on_submit=True,
                        align="center",
                        width="345px",
                    ),
                ),
                width="100%",
                height="80%",
            ),
        ),
        rx.box(
            width="100%",
            height="15%",
        ),
        rx.center(
            rx.button(
                rx.cond(
                    State.login_not_member,
                    rx.text(
                        "비회원으로 시작하기",
                    ),
                    rx.text(
                        "회원으로 시작하기",
                    ),
                ),
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="button",
                background_color=AppColor.LIGHT_GRAY_TEXT,
                on_click=State.change_login_not_member,
            ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )
