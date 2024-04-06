import reflex as rx
from .index import index
from .sign_up import sign_up
from .make_meeting.make_meeting import make_meeting
from .login import login


app = rx.App(stylesheets=["fonts/myfont.css"], title="GatherPlan")
app.add_page(index)
app.add_page(sign_up, route="/sign_up")
app.add_page(make_meeting, route="/make_meeting")
app.add_page(login, route="/login")
