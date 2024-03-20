import reflex as rx


def sign_up() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "우리 언제 만나?",
                font_size="24px",
                font_family="Pretendard-Regular",
                font_weight="700",
                color="#B5B5B5",
                padding="10px 0 0 20px",
            ),
            rx.text(
                "게더플랜에서 약속시간과 장소를 정해보세요!",
                font_size="16px",
                font_family="Pretendard-Regular",
                font_weight="700",
                padding="0 0 0 20px",
            ),
            width="100%",
            height="10%",
        ),
        rx.center(
            "Gather Plan",
            font_size="36px",
            font_family="JalnanGothic",
            font_weight="700",
            text_align="center",
            width="100%",
            height="72%",
        ),
        rx.vstack(
            rx.button(
                "회원가입",
                width="348px",
                height="48px",
                padding="20px",
                color="#FFFFFF",
                background_color="#0000FF",
                on_click=rx.redirect("/docs/api-reference/special_events"),
            ),
            rx.button(
                "비회원으로 시작하기",
                width="348px",
                height="48px",
                padding="20px",
                color="#2B2A2A",
                background_color="#EEEEEE",
            ),
            width="100%",
            height="18%",
            align="center",
        ),
        spacing="0",
        height="100vh",
    )
