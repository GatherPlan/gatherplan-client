import reflex as rx


def header(url: str = "") -> rx.Component:
    """웹앱의 헤더 컴포넌트."""
    return rx.box(
        rx.hstack(
            rx.box(
                rx.hstack(
                    rx.center(
                        rx.icon(
                            "calendar-days",
                            size=32,
                            color="blue.500",
                        ),
                        width="72px",
                        height="60px",
                    ),
                    rx.spacer(),
                    rx.center(
                        rx.button(
                            "로그인",
                            bg="black",
                            color="white",
                            size="2",
                            border_radius="full",
                            _hover={
                                "bg": "rgba(0, 0, 0, 0.8)",
                            },
                        ),
                        width="72px",
                        height="60px",
                    ),
                    width="100%",
                ),
                width="100%",
            ),
            width="100%",
            height="60px",
        ),
        position="sticky",
        top="0",
        z_index="999",
        bg=["white", "white", "rgb(243, 244, 246)"],
        border_bottom="1px solid #eaeaea",
        width="100%",
    )
