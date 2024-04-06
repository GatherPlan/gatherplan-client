import reflex as rx


def make_meeting() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.center(
                "약속 만들기",
                font_size="32px",
                font_family="Pretendard-Regular",
                font_weight="700",
            ),
            width="100%",
            align="center",
            padding_top="10px",
            padding_bottom="50px",
        ),
        rx.box(
            rx.center(
                "약속 이름을 정해주세요",
                font_weight="500",
                font_size="24px",
            ),
            rx.center(
                "약속이름은 1~15자이여야 합니다.",
                font_size="16px",
                color="#B5B5B5",
            ),
            width="100%",
        ),
        rx.vstack(
            rx.button(
                "회원가입",
                width="348px",
                height="48px",
                padding="20px",
                color="#FFFFFF",
                background_color="#3A7DFF",
                on_click=rx.redirect("/docs/api-reference/special_events"),
            ),
            rx.button(
                "회원가입",
                width="348px",
                height="48px",
                padding="20px",
                color="#2B2A2A",
                background_color="#EEEEEE",
                on_click=rx.redirect("/docs/api-reference/special_events"),
            ),
            rx.button(
                "비회원으로 시작하기",
                width="348px",
                height="48px",
                padding="20px",
                color="#2B2A2A",
                background_color="#C8C8C8",
            ),
            width="100%",
            height="25%",
            align="center",
        ),
        spacing="0",
        height="100vh",
    )
