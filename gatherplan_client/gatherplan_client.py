import os
from .pages import *  # noqa: F401, F403

if os.environ.get("ENV") == "prod":
    app = rx.App(
        stylesheets=["fonts/myfont.css"],
        title="GatherPlan",
        head_components=[
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
