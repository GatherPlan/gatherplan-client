import reflex as rx


def footer(is_vertical: bool = False) -> rx.Component:
    """웹앱의 푸터 컴포넌트."""

    def menu_items():
        items = [
            ("home", "/"),
            ("search", "/search"),
            ("plus", "/new"),
            ("calendar-days", "/my"),
        ]

        if is_vertical:
            # PC 버전 - 왼쪽 사이드바 스타일
            return [
                rx.link(
                    rx.center(
                        rx.icon(tag=icon, size=28, color="black"),
                        border_radius="md",
                        padding="2",
                        width="40px",
                        height="40px",
                        _hover={"bg": "gray.200"},
                    ),
                    href=href,
                    _hover={"text_decoration": "none"},
                )
                for icon, href in items
            ]
        else:
            # 모바일 버전 - 하단 네비게이션 바 스타일
            return [
                rx.link(
                    rx.center(
                        rx.icon(tag=icon, size=28, color="black"),
                        height="100%",
                        _hover={"color": "gray.800"},
                    ),
                    href=href,
                    height="100%",
                    _hover={"text_decoration": "none"},
                )
                for icon, href in items
            ]

    container = rx.vstack if is_vertical else rx.hstack
    return rx.center(
        container(
            *menu_items(),
            spacing="4" if is_vertical else "8",
            justify="center",
            align_items="center",
            width="100%",
            height="100%" if is_vertical else "auto",
            padding_y="2",
        ),
        position="fixed" if not is_vertical else "static",
        bottom="0" if not is_vertical else "auto",
        left="0" if not is_vertical else "auto",
        width="100%" if not is_vertical else "72px",
        height="100%" if is_vertical else "52px",
        background_color="white" if not is_vertical else "rgb(243, 244, 246)",
        border_top="1px solid #eaeaea" if not is_vertical else None,
        border_right="1px solid #eaeaea" if is_vertical else None,
    )
