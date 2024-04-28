import reflex as rx
from .index import index
from .join_meeting.join_meeting_date import join_meeting_date
from .join_meeting.enter_meeting_code import enter_meeting_code
from .join_meeting.join_meeting import join_meeting
from .make_meeting.make_meeting_check import make_meeting_check
from .make_meeting.make_meeting_result import make_meeting_result
from .make_meeting.make_meeting_time import make_meeting_time
from .not_member_login import not_member_login
from .sign_up import sign_up
from .make_meeting.make_meeting import make_meeting
from .make_meeting.make_meeting_date import make_meeting_date
from .make_meeting.make_meeting_detail import make_meeting_detail


app = rx.App(stylesheets=["fonts/myfont.css"], title="GatherPlan")
app.add_page(index, route="/")
app.add_page(sign_up, route="/sign_up")
app.add_page(make_meeting, route="/make_meeting")
app.add_page(make_meeting_detail, route="/make_meeting_detail")
app.add_page(make_meeting_date, route="/make_meeting_date")
app.add_page(make_meeting_time, route="/make_meeting_time")
app.add_page(make_meeting_check, route="/make_meeting_check")
app.add_page(make_meeting_result, route="/make_meeting_result")
app.add_page(enter_meeting_code, route="/enter_meeting_code")
app.add_page(join_meeting, route="/join_meeting")
app.add_page(not_member_login, route="/not_member_login")
app.add_page(join_meeting_date, route="/join_meeting_date")
