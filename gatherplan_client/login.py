import reflex as rx


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def login() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.center(
                "Gather Plan",
                font_size="24px",
                font_family="Pretendard-Regular",
                font_weight="700",
                color="#000000",
                padding_top="8%",
            ),
            rx.center(
                "게더플랜에서 모임의 약속을 잡아보세요",
                font_size="12px",
                font_family="Pretendard-Regular",
                font_weight="500",
                color="#737373",
            ),
            width="100%",
            height="20%",
            align="center",
        ),
        rx.center(
            rx.form(
                rx.box(
                    rx.text(
                        "이메일",
                        font_size="10px",
                        font_family="Pretendard-Regular",
                    ),
                    rx.input(
                        placeholder="2~8자리",
                        name="email",
                        font_size="16px",
                        height="48px",
                        border_radius="35px",
                    ),
                    padding_bottom="20px",
                ),
                rx.box(
                    rx.text(
                        "비밀번호",
                        font_size="10px",
                        font_family="Pretendard-Regular",
                    ),
                    rx.input(
                        placeholder="2~8자리",
                        name="password",
                        font_size="16px",
                        height="48px",
                    ),
                    padding_bottom="30px",
                ),
                rx.button(
                    "로그인",
                    width="348px",
                    height="48px",
                    padding="20px",
                    color="#FFFFFF",
                    type="submit",
                    background_color="#3A7DFF",
                ),
                rx.hstack(
                    rx.button(
                        "아이디 찾기",
                        width="110px",
                        height="36px",
                        color="#A3A3A3",
                        background_color="#FFFFFF",
                    ),
                    rx.button(
                        "비밀번호 찾기",
                        width="110px",
                        height="36px",
                        color="#A3A3A3",
                        background_color="#FFFFFF",
                    ),
                    rx.button(
                        "회원가입",
                        width="110px",
                        height="36px",
                        color="#A3A3A3",
                        background_color="#FFFFFF",
                    ),
                    padding_top="10px",
                    width="100%",
                ),
                on_submit=FormState.handle_submit,
                align="center",
                width="345px",
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
                color="#FFFFFF",
                type="submit",
                background_color="#D1D1D1",
            ),
            width="100%",
            height="15%",
        ),
        spacing="0",
        height="100vh",
    )
