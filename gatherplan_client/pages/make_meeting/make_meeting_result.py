import reflex as rx

from gatherplan_client.backend.state import State, FRONTEND_URL
from gatherplan_client.components.schema import AppColor, AppFontFamily, TextSize
from gatherplan_client.components.text_box import (
    main_sub_text_center_box,
    sub_text_box,
    main_text_box,
    main_sub_text_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/make_meeting_result/[meeting_code_result]", header_url="/", page_text=""
)
def make_meeting_result() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                main_sub_text_center_box(
                    "정상적으로 약속이 생성되었습니다.",
                    "약속 정보를 확인하고 참여자들에게 공유해보세요.",
                ),
            ),
            rx.vstack(
                main_sub_text_box(State.meeting_name, "약속이름", change_position=True),
                rx.cond(
                    State.meeting_location_detail != "",
                    rx.box(
                        sub_text_box("약속장소"),
                        rx.link(
                            State.meeting_location,
                            href=State.place_url,
                            font_size=TextSize.TINY_SMALL,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            font_weight="700",
                            color=AppColor.SKY_BLUE,
                        ),
                        sub_text_box(State.meeting_location_detail),
                    ),
                    rx.box(),
                ),
                rx.cond(
                    State.meeting_notice != "",
                    main_sub_text_box(
                        State.meeting_notice, "공지사항", change_position=True
                    ),
                    rx.box(),
                ),
                rx.box(
                    sub_text_box("약속 후보 날짜"),
                    rx.scroll_area(
                        rx.grid(
                            rx.foreach(State.select_data, main_text_box),
                            columns="3",
                            width="100%",
                        ),
                        type="auto",
                        scrollbars="vertical",
                        style={"height": 120, "width": 360},
                    ),
                ),
                rx.box(
                    rx.hstack(
                        sub_text_box("약속코드"),
                        rx.button(
                            rx.icon("copy"),
                            on_click=rx.set_clipboard(rx.State.meeting_code_result),
                            width="12px",
                            height="12px",
                            padding="0",
                            color=AppColor.GRAY_TEXT,
                            background_color=AppColor.WHITE,
                        ),
                    ),
                    main_text_box(rx.State.meeting_code_result),
                ),
                rx.box(
                    rx.button(
                        "참여하기",
                        width="360px",
                        height="35px",
                        padding="20px",
                        color=AppColor.WHITE,
                        type="submit",
                        background_color=AppColor.MAIN_COLOR,
                        on_click=rx.redirect(
                            f"/enter_meeting_code/{rx.State.meeting_code_result}"
                        ),
                        margin_bottom="10px",
                    ),
                    rx.button(
                        "공유하기",
                        width="360px",
                        height="35px",
                        padding="20px",
                        color=AppColor.BLACK,
                        on_click=rx.set_clipboard(
                            f"{FRONTEND_URL}/enter_meeting_code/{rx.State.meeting_code_result}"
                        ),
                        background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    ),
                ),
                spacing="5",
            ),
            width="360px",
        ),
        width="100%",
    )
