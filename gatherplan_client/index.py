import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("언제볼까", size="6"),
            rx.box(
                height="30%",
            ),
            rx.button(
                "약속 만들기",
                size="4",
                width="80%",
                color="white",
                bg_color="black",
                border_radius="5px",
                on_click=rx.redirect("/sign_up"),
            ),
            rx.button(
                "약속 참여하기",
                size="4",
                width="80%",
                color="white",
                bg_color="black",
                border_radius="5px",
                on_click=rx.redirect(
                    "https://github.com/reflex-dev/reflex/",
                    external=True,
                ),
            ),
            rx.button(
                "약속 현황보기",
                size="4",
                width="80%",
                color="white",
                bg_color="black",
                border_radius="5px",
                on_click=rx.console_log("Hello World!"),
            ),
            width="70%",
            height="80%",
            font_size="2em",
            spacing="5",
            align="center",
        ),
        height="100vh",
    )
