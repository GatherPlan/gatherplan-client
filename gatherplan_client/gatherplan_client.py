import reflex as rx

from gatherplan_client.pages.check_meeting.check_meeting import check_meeting
from gatherplan_client.pages.check_meeting.check_meeting_detail import check_meeting_detail
from gatherplan_client.pages.index import index
from gatherplan_client.pages.join_meeting.join_meeting_result import join_meeting_result
from gatherplan_client.pages.join_meeting.join_meeting_check import join_meeting_check
from gatherplan_client.pages.join_meeting.join_meeting_date import join_meeting_date
from gatherplan_client.pages.join_meeting.enter_meeting_code import enter_meeting_code
from gatherplan_client.pages.join_meeting.join_meeting import join_meeting
from gatherplan_client.pages.make_meeting.make_meeting_check import make_meeting_check
from gatherplan_client.pages.make_meeting.make_meeting_result import make_meeting_result
from gatherplan_client.pages.login.not_member_login import not_member_login
from gatherplan_client.pages.login.sign_up import sign_up
from gatherplan_client.pages.make_meeting.make_meeting import make_meeting
from gatherplan_client.pages.make_meeting.make_meeting_date import make_meeting_date
from gatherplan_client.pages.make_meeting.make_meeting_detail import make_meeting_detail


def health_check() -> rx.Component:
    return rx.box("pong")


app = rx.App(stylesheets=["fonts/myfont.css"], title="GatherPlan")
app.add_page(index, route="/")
app.add_page(sign_up, route="/sign_up")
app.add_page(make_meeting, route="/make_meeting")
app.add_page(make_meeting_detail, route="/make_meeting_detail")
app.add_page(make_meeting_date, route="/make_meeting_date")
app.add_page(make_meeting_check, route="/make_meeting_check")
app.add_page(make_meeting_result, route="/make_meeting_result/[meeting_code]")
app.add_page(enter_meeting_code, route="/enter_meeting_code/[meeting_code]")
app.add_page(enter_meeting_code, route="/enter_meeting_code")


app.add_page(join_meeting, route="/join_meeting")
app.add_page(not_member_login, route="/not_member_login")
app.add_page(join_meeting_date, route="/join_meeting_date")
app.add_page(join_meeting_check, route="/join_meeting_check")
app.add_page(join_meeting_result, route="/join_meeting_result")
app.add_page(check_meeting, route="/check_meeting")
app.add_page(check_meeting_detail, route="/check_meeting_detail")
app.add_page(health_check, route="/ping")
