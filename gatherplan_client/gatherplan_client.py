import reflex as rx
from .index import index
from .sign_up import sign_up
from .make_meeting.make_meeting import make_meeting
from .make_meeting.make_meeting_detail import make_meeting_detail


app = rx.App(stylesheets=["fonts/myfont.css"], title="GatherPlan")
app.add_page(index, route="/")
app.add_page(sign_up, route="/sign_up")
app.add_page(make_meeting, route="/make_meeting")
app.add_page(make_meeting_detail, route="/make_meeting_detail")
