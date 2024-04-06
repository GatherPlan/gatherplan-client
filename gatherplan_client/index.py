import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "Gather Plan",
                font_size="24px",
                font_family="Pretendard-Regular",
                font_weight="700",
                padding="10px 0 0 20px",
            ),
            rx.text(
                "모임의 약속을 잡아보세요",
                font_size="16px",
                font_family="Pretendard-Regular",
                color="#B5B5B5",
                font_weight="700",
                padding="0 0 0 20px",
            ),
            width="100%",
            height="10%",
        ),
        rx.center(
            text_align="center",
            width="100%",
            height="40%",
        ),
        rx.vstack(
            rx.button(
                rx.vstack(
                    rx.text(
                        "만들기",
                        color="#000000",
                        font_size="24px",
                        font_family="JalnanGothic",
                    ),
                    rx.text(
                        "새로운 약속을 생성해보세요",
                        color="#B5B5B5",
                        font_size="16px",
                        font_family="JalnanGothic",
                    ),
                    width="348px",
                ),
                width="348px",
                height="96px",
                padding="20px",
                border_radius="15px",
                background_color="#F5F5F5",
                on_click=rx.redirect("/make_meeting"),
            ),
            rx.button(
                rx.vstack(
                    rx.text(
                        "참여하기",
                        color="#000000",
                        font_size="24px",
                        font_family="JalnanGothic",
                    ),
                    rx.text(
                        "약속에 참여해보세요",
                        color="#B5B5B5",
                        font_size="16px",
                        font_family="JalnanGothic",
                    ),
                    width="348px",
                ),
                width="348px",
                height="96px",
                padding="20px",
                border_radius="15px",
                background_color="#F5F5F5",
                on_click=rx.redirect("/docs/api-reference/special_events"),
            ),
            rx.button(
                rx.vstack(
                    rx.text(
                        "현황보기",
                        color="#000000",
                        font_size="24px",
                        font_family="JalnanGothic",
                    ),
                    rx.text(
                        "누가 참석할 수 있는지 확인해보세요",
                        color="#B5B5B5",
                        font_size="16px",
                        font_family="JalnanGothic",
                    ),
                    width="348px",
                ),
                width="348px",
                height="96px",
                padding="20px",
                border_radius="15px",
                background_color="#F5F5F5",
                on_click=rx.redirect("/docs/api-reference/special_events"),
            ),
            width="100%",
            height="50%",
            align="center",
            justify="end",
            padding_bottom="10px",
        ),
        spacing="0",
        height="100vh",
    )
