import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.form_box import form_box, form_box_with_value
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize
from gatherplan_client.reflex_assets.text_box import left_align_text_box


def location_button(button_text: str):
    return rx.drawer.close(
        rx.button(
            button_text,
            width="340px",
            height="36px",
            color="#A3A3A3",
            type="button",
            on_click=MakeMeetingNameState.handle_location_submit(
                {"input_location": button_text}
            ),
            background_color="#FFFFFF",
        )
    )


@need_login
def make_meeting_date() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속 날짜를 선택해 주세요",
            "최대 30일까지 선택할 수 있어요",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        # TODO: Implement the date picker
        rx.vstack(
            rx.chakra.hstack(
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
            ),
            rx.chakra.hstack(
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
                rx.chakra.checkbox("4/16", color_scheme="red", size="sm"),
            ),
        ),
        basic_button("다음"),
        spacing="0",
        height="100vh",
    )
