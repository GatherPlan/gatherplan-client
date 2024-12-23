"""Common templates used between pages in the app."""

from __future__ import annotations

from typing import Callable

import reflex as rx

from gatherplan_client.pages.login import need_login_check_meeting, need_login
from gatherplan_client.pages.login.login import need_login_check_meeting_login_purpose

default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

COMMON_LAYOUT = rx.vstack(
    # 공통으로 사용되는 레이아웃 컴포넌트
)


def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
    need_login_type: str | None = "default",
) -> Callable[[Callable[[], rx.Component]], rx.Component]:

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            from gatherplan_client.components.header import header
            from gatherplan_client.components.footer import footer

            return rx.box(
                rx.vstack(
                    header(),
                    rx.hstack(
                        # PC에서는 footer를 왼쪽에 세로로 표시
                        rx.box(
                            footer(is_vertical=True),
                            width="240px",
                            height="100vh",
                            position="sticky",
                            top="0",
                            display=["none", "none", "block"],
                        ),
                        rx.box(
                            rx.box(
                                page_content(),
                                width="100%",
                                max_width="600px",
                                margin="0 auto",
                                bg="white",
                                border_x="1px solid #eaeaea",
                                min_height="100vh",
                                padding_top="50px",
                            ),
                            flex="1",
                            min_height="100vh",
                            bg="rgb(250, 250, 250)",
                        ),
                        width="100%",
                        spacing="0",
                        align_items="stretch",
                        bg="rgb(250, 250, 250)",
                    ),
                    # 모바일에서는 footer를 아래에 가로로 표시
                    rx.box(
                        footer(is_vertical=False),
                        width="100%",
                        position="fixed",
                        bottom="0",
                        left="0",
                        display=["block", "block", "none"],
                    ),
                    height="100%",
                    spacing="0",
                    bg="rgb(250, 250, 250)",
                ),
                width="100%",
                min_height="100vh",
                bg="rgb(250, 250, 250)",
            )

        if need_login_type == "default":

            @rx.page(
                route=route,
                title=title,
                description=description,
                meta=all_meta,
                script_tags=script_tags,
                on_load=on_load,
            )
            @need_login
            def theme_wrap():
                return templated_page()

        elif need_login_type == "check_meeting_login":

            @rx.page(
                route=route,
                title=title,
                description=description,
                meta=all_meta,
                script_tags=script_tags,
                on_load=on_load,
            )
            @need_login_check_meeting
            def theme_wrap():
                return templated_page()

        elif need_login_type == "need_login_check_meeting_login_purpose":

            @rx.page(
                route=route,
                title=title,
                description=description,
                meta=all_meta,
                script_tags=script_tags,
                on_load=on_load,
            )
            @need_login_check_meeting_login_purpose
            def theme_wrap():
                return templated_page()

        else:

            @rx.page(
                route=route,
                title=title,
                description=description,
                meta=all_meta,
                script_tags=script_tags,
                on_load=on_load,
            )
            def theme_wrap():
                return templated_page()

        return theme_wrap

    return decorator
