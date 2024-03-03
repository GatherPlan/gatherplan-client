"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("회원가입", size="6"),
            rx.box(
                rx.text("일반 회원가입", size="4", width="100%", weight="bold"),
                width="100%",
            ),
            rx.form(
                rx.vstack(
                    rx.box(
                        rx.text("이메일", size="2"),
                        rx.input(
                            placeholder="example@example.com", size="3", width="100%"
                        ),
                        rx.text(
                            "중복된 이메일입니다", size="1", color="red", align="center"
                        ),
                        width="100%",
                    ),
                    rx.box(
                        rx.text("이메일 인증", size="2"),
                        rx.input(placeholder="인증 코드", size="3", width="100%"),
                        rx.text(
                            "인증 요청을 눌러주세요",
                            size="1",
                            color="red",
                            align="center",
                        ),
                        width="100%",
                    ),
                    rx.box(
                        rx.text("이름", size="2"),
                        rx.input(placeholder="", size="3", width="100%"),
                        rx.text(
                            "필수 항목을 입력해주세요",
                            size="1",
                            color="red",
                            align="center",
                        ),
                        width="100%",
                    ),
                    rx.box(
                        rx.text("비밀번호", size="2"),
                        rx.input(
                            placeholder="최소 8자 이상의 영문, 숫자, 특수문자 조합",
                            size="3",
                            width="100%",
                        ),
                        rx.text(
                            "비밀번호 형식에 맞게 입력해주세요",
                            size="1",
                            color="red",
                            align="center",
                        ),
                        width="100%",
                    ),
                    spacing="2",
                ),
                width="95%",
            ),
            rx.button(
                "다음",
                size="3",
                width="80%",
                color="white",
                bg_color="black",
                border_radius="5px",
            ),
            width="70%",
            height="80%",
            font_size="2em",
            spacing="5",
            align="center",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
