from typing import List

import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.form_box import form_box
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize
from gatherplan_client.reflex_assets.text_box import left_align_text_box


class MakeMeetingNameState(rx.State):
    """The app state."""

    form_data: dict = {}
    input_location: str = ""
    search_location: List[str] = ["성수동1", "성수동2", "성수동3", "성수동4"]
    select_location: str = ""

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        return rx.redirect("/make_meeting_detail")

    def handle_detail_submit(self, form_data: dict):
        """Handle the form submit."""
        self.input_location = form_data.get("input_location")
        return rx.redirect("/make_meeting_date")

    def handle_location_submit(self, form_data: dict):
        """Handle the form submit."""
        self.select_location = form_data.get("input_location")


@need_login
def make_meeting() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속 이름을 정해주세요",
            "상대방이 이해하기 좋은 이름으로 만들어요!",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    form_box(
                        explain_text="약속이름",
                        placeholder_text="약속이름을 입력해주세요",
                        form_value="meeting_name",
                    ),
                    basic_button("다음"),
                    on_submit=MakeMeetingNameState.handle_submit,
                    align="center",
                    width="345px",
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
