"""Common templates used between pages in the app."""

from __future__ import annotations

import os
from typing import Callable

import reflex as rx

from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppFontFamily
from gatherplan_client.pages.login import need_login_check_meeting, need_login
from gatherplan_client.pages.login.login import need_login_check_meeting_login_purpose

default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


GA_ID = "G-Q9R0ZEJ8S6" if os.environ.get("ENV") == "prod" else ""


def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
    header_url: str | None = "/",
    page_text: str | None = None,
    need_login_type: str | None = "default",
) -> Callable[[Callable[[], rx.Component]], rx.Component]:

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.vstack(
                rx.script(
                    src=f"https://www.googletagmanager.com/gtag/js?id={GA_ID}",
                    strategy="afterInteractive",
                ),
                rx.script(
                    f"""
                    window.dataLayer = window.dataLayer || [];
                    function gtag(){{window.dataLayer.push(arguments);}}
                    gtag('js', new Date());
                    gtag('config', '{GA_ID}');
                    """,
                    id="google-analytics",
                    strategy="afterInteractive",
                ),
                rx.cond(
                    header_url == "",
                    rx.box(),
                    header(header_url),
                ),
                rx.cond(
                    page_text == "",
                    rx.box(),
                    rx.center(
                        rx.text(
                            page_text,
                            font_size="20px",
                            padding_top="28px",
                            padding_bottom="40px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_weight="700",
                            width="360px",
                        ),
                        width="100%",
                        height="15%",
                    ),
                ),
                page_content(),
                spacing="0",
                height="100vh",
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
