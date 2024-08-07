import requests
import reflex as rx

from gatherplan_client.backend.login_state import LoginState
from gatherplan_client.backend.backend_rouuter import BACKEND_URL, HEADER
from gatherplan_client.components.buffer_box import buffer_box
from gatherplan_client.components.buttons import (
    basic_button,
    small_button,
)
from gatherplan_client.components.form_box import form_box
from gatherplan_client.components.schema import AppColor
from gatherplan_client.components.text_box import center_align_text_box


def need_login(func):
    def inner():
        return rx.cond(
            LoginState.login_token == "",
            login(),
            func(LoginState.login_token, LoginState.nick_name),
        )

    return inner


class EmailAuth(rx.State):
    text: str = "temp@email"

    def sign_up_send_auth_number(self):
        data = {"email": self.text}
        response = requests.post(
            f"{BACKEND_URL}/api/v1/users/auth", headers=HEADER, json=data
        )
        if response.status_code == 200:
            return rx.window_alert(f"{self.text}로 인증번호가 전송되었습니다.")

        else:
            print(response.json())
            return rx.window_alert(f"error")


@rx.page(route="/login")
def login() -> rx.Component:
    return rx.vstack(
        buffer_box("8%"),
        center_align_text_box(
            main_text="Gather Plan", sub_text="게더플랜에서 모임의 약속을 잡아보세요"
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    form_box(
                        explain_text="이메일",
                        placeholder_text="2~8자리",
                        form_value="email",
                    ),
                    form_box(
                        explain_text="비밀번호",
                        placeholder_text="2~8자리",
                        form_value="password",
                        type="password",
                    ),
                    basic_button("로그인"),
                    rx.hstack(
                        small_button("아이디 찾기"),
                        small_button("비밀번호 찾기"),
                        small_button("회원가입", "/sign_up"),
                        padding_top="10px",
                        width="100%",
                    ),
                    on_submit=LoginState.handle_submit,
                    reset_on_submit=False,
                    align="center",
                    width="345px",
                ),
                rx.center(
                    LoginState.error_message,
                    font_size="12px",
                    color="#FF0000",
                    width="100%",
                ),
            ),
            width="100%",
            height="60%",
        ),
        rx.box(
            width="100%",
            height="15%",
        ),
        rx.center(
            rx.button(
                "비회원으로 시작하기",
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="button",
                background_color=AppColor.LIGHT_GRAY_TEXT,
                on_click=rx.redirect("/not_member_login"),
            ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )


@rx.page(route="/login_join_meeting")
def login_join_meeting() -> rx.Component:
    return rx.vstack(
        buffer_box("8%"),
        center_align_text_box(
            main_text="Gather Plan", sub_text="게더플랜에서 모임의 약속을 잡아보세요"
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    form_box(
                        explain_text="이메일",
                        placeholder_text="2~8자리",
                        form_value="email",
                    ),
                    form_box(
                        explain_text="비밀번호",
                        placeholder_text="2~8자리",
                        form_value="password",
                        type="password",
                    ),
                    basic_button("로그인"),
                    rx.hstack(
                        small_button("아이디 찾기"),
                        small_button("비밀번호 찾기"),
                        small_button("회원가입", "/sign_up"),
                        padding_top="10px",
                        width="100%",
                    ),
                    on_submit=LoginState.handle_submit_join_meeting,
                    reset_on_submit=False,
                    align="center",
                    width="345px",
                ),
                rx.center(
                    LoginState.error_message,
                    font_size="12px",
                    color="#FF0000",
                    width="100%",
                ),
            ),
            width="100%",
            height="60%",
        ),
        rx.box(
            width="100%",
            height="15%",
        ),
        rx.center(
            rx.button(
                "비회원으로 시작하기",
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="button",
                background_color=AppColor.LIGHT_GRAY_TEXT,
                on_click=rx.redirect("/not_member_login"),
            ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )
