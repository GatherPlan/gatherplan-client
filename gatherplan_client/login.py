import reflex as rx

from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.buttons import (
    basic_button,
    small_button,
    second_basic_button,
)
from gatherplan_client.reflex_assets.form_box import form_box
from gatherplan_client.reflex_assets.text_box import center_align_text_box


def need_login(func):
    def inner():
        return rx.cond(LoginState.login_token == "", login(), func())

    return inner


class LoginState(rx.State):
    form_data: dict = {}
    email: str = ""
    password: str = ""
    login_token: str = "temp"
    nick_name: str = ""
    auth_number: str = ""
    error_message: str = "SomeThing Wrong"

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(self.form_data)
        if self.login():
            return rx.redirect(f"{self.router.page.path}")
        else:
            self.error_message = "로그인 실패"
            return None

    def login(self):

        self.email = self.form_data.get("email")
        self.password = self.form_data.get("password")

        login_state = True
        self.login_token = "temp_token"

        if login_state:
            return True
        else:
            return False

    def sign_up(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

        return rx.redirect("/")

    def start_not_member_login(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

        return rx.redirect("/join_meeting_detail")


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
                    reset_on_submit=True,
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
            # second_basic_button(
            #     "비회원으로 시작하기", redirect_url="/not_member_login"
            # ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )
