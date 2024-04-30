import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.make_meeting.make_meeting import MakeMeetingNameState
from gatherplan_client.reflex_assets.buttons import basic_button
from gatherplan_client.reflex_assets.form_box import form_box
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
def make_meeting_detail() -> rx.Component:
    return rx.vstack(
        header("약속만들기", "/make_meeting"),
        left_align_text_box(
            "약속 장소를 정해주세요",
            "행정구역 또는 구체적인 장소를 입력해주세요",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                rx.form(
                    rx.hstack(
                        form_box(
                            explain_text="약속장소",
                            placeholder_text="약속장소를 입력해주세요",
                            form_value="location",
                        ),
                        rx.drawer.root(
                            rx.drawer.trigger(
                                rx.button(
                                    "검색",
                                    type="button",
                                    height="48px",
                                    margin_top="15px",
                                )
                            ),
                            rx.drawer.overlay(z_index="5"),
                            rx.drawer.portal(
                                rx.drawer.content(
                                    rx.tabs.root(
                                        rx.tabs.list(
                                            rx.tabs.trigger(
                                                "행정구역", value="tab1", width="174px"
                                            ),
                                            rx.tabs.trigger(
                                                "상세주소", value="tab2", width="174px"
                                            ),
                                            font_size="16px",
                                        ),
                                        rx.tabs.content(
                                            rx.grid(
                                                rx.foreach(
                                                    MakeMeetingNameState.search_location,
                                                    location_button,
                                                ),
                                                columns="1",
                                            ),
                                            value="tab1",
                                        ),
                                        rx.tabs.content(
                                            rx.text("item on tab 2"),
                                            value="tab2",
                                        ),
                                        default_value="tab1",
                                        width="360px",
                                        align="center",
                                    ),
                                    align="center",
                                    top="auto",
                                    right="auto",
                                    height="60%",
                                    width="100%",
                                    padding="2em",
                                    background_color="#FFF",
                                    border_radius="2em 2em 0 0",
                                )
                            ),
                            direction="bottom",
                        ),
                    ),
                    rx.cond(
                        MakeMeetingNameState.select_location == "",
                        rx.text(""),
                        left_align_text_box(
                            MakeMeetingNameState.select_location,
                            "선택한 장소를 확인하고, 다음 단계로 이동하세요",
                            main_font_size=TextSize.TINY_SMALL,
                            sub_font_size=TextSize.TINY,
                        ),
                    ),
                    basic_button("다음"),
                    on_submit=MakeMeetingNameState.handle_detail_submit,
                    align="center",
                    width="345px",
                ),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
