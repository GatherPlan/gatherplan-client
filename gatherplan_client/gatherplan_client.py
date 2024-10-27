import os
from .pages import *  # noqa: F401, F403

if os.environ.get("ENV") == "prod":
    app = rx.App(
        stylesheets=["fonts/myfont.css"],
        title="GatherPlan",
        head_components=[
            rx.el.script(
                async_=True,
                src="https://www.googletagmanager.com/gtag/js?id=G-Q9R0ZEJ8S6",
            ),
            rx.el.script(
                """
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-Q9R0ZEJ8S6');
                """
            ),
            rx.el.meta(
                name="google-site-verification",
                content="beqAu5H-vKsKPxSVN6z3hpR6ydUfSKqWjcmzqY-6000",
            ),
        ],
    )
else:
    app = rx.App(
        stylesheets=["fonts/myfont.css"],
        title="GatherPlan",
    )


def health_check() -> rx.Component:
    return rx.box("pong")


app.add_page(health_check, route="/ping")
app.add_page(enter_meeting_code, route="/enter_meeting_code/[meeting_code_params]")
