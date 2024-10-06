import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.components.text_box import text_for_each
from gatherplan_client.templates.template import template


@template(route="/make_meeting_check", header_url="/make_meeting_date", page_text="")
def make_meeting_check() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.vstack(
                rx.text(
                    "선택한 약속 정보를 확인해주세요",
                    font_size="18px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    align="center",
                    width="360px",
                ),
                rx.text(
                    "약속 정보 변경은 약속 현황보기에서 가능합니다.",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                    align="center",
                    width="360px",
                ),
            ),
            width="100%",
            height="20%",
        ),
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
                            rx.foreach(State.select_data, text_for_each),
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
            ),
            width="100%",
            height="60%",
        ),
        rx.center(
            rx.button(
                "약속 만들기",
                width="348px",
                height="35px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_COLOR,
                on_click=State.make_meeting_check_handle_submit,
            ),
            width="100%",
        ),
        width="100%",
        height="100%",
    )
