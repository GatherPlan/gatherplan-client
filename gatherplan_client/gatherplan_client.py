from .pages import *  # noqa: F401, F403

app = rx.App(stylesheets=["fonts/myfont.css"], title="GatherPlan")


def health_check() -> rx.Component:
    return rx.box("pong")


app.add_page(health_check, route="/ping")
app.add_page(enter_meeting_code, route="/enter_meeting_code/[meeting_code_params]")
