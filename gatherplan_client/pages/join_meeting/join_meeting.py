import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import (
    text_for_each,
)
from gatherplan_client.templates.template import template


@template(
    route="/join_meeting",
    header_url="/enter_meeting_code",
    page_text="약속 정보",
    need_login_type="no_login",
)
def join_meeting() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.vstack(
                rx.box(
                    rx.text(
                        "약속이름",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        State.meeting_name,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
                    rx.text(
                        "약속장소",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.vstack(
                        rx.link(
                            State.meeting_location,
                            href=State.place_url,
                            font_size="14px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_weight="700",
                            color=AppColor.BLACK,
                            padding_bottom="5px",
                        ),
                        rx.text(
                            State.meeting_location_detail,
                            font_size="12px",
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_weight="500",
                            color=AppColor.GRAY_TEXT,
                            margin="0",
                            padding="0",
                        ),
                        spacing="0",
                    ),
                    width="360px",
                    padding_left="10px",
                    height="60px",
                ),
                rx.box(
                    rx.text(
                        "약속 후보 날짜",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.scroll_area(
                        rx.grid(
                            rx.foreach(State.meeting_date, text_for_each),
                            columns="3",
                            width="360px",
                        ),
                        type="always",
                        scrollbars="vertical",
                        style={"height": 70, "width": 360},
                    ),
                    padding_left="10px",
                ),
                rx.box(
                    rx.text(
                        "공지사항",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        State.meeting_notice,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "약속코드",
                                font_size="12px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                font_weight="700",
                                color=AppColor.GRAY_TEXT,
                            ),
                            rx.button(
                                rx.icon("copy"),
                                on_click=rx.set_clipboard(State.meeting_code),
                                width="12px",
                                height="12px",
                                padding="0",
                                color=AppColor.GRAY_TEXT,
                                background_color=AppColor.WHITE,
                            ),
                        ),
                        rx.box(
                            rx.text(
                                State.meeting_code,
                                font_size="14px",
                                font_family=AppFontFamily.DEFAULT_FONT,
                                color=AppColor.BLACK,
                                font_weight="700",
                                width="170px",
                            ),
                        ),
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
                rx.box(
                    rx.text(
                        "모임장",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        State.host_name,
                        font_size="14px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.BLACK,
                    ),
                    width="360px",
                    padding_left="10px",
                    height="50px",
                ),
            ),
            width="100%",
            height="60%",
        ),
        rx.center(
            rx.vstack(
                rx.button(
                    "참여하기",
                    width="348px",
                    height="35px",
                    padding="20px",
                    color=AppColor.WHITE,
                    type="submit",
                    background_color=AppColor.MAIN_COLOR,
                    on_click=rx.redirect("/join_meeting_date"),
                ),
            ),
            width="100%",
        ),
        width="100%",
        height="100%",
    )
