import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.calendar import (
    display_select_date,
    calendar_header,
)
from gatherplan_client.components.schema import AppColor, AppFontFamily, TextSize
from gatherplan_client.components.text_box import (
    main_sub_text_box,
    sub_text_box,
    main_text_box,
)
from gatherplan_client.templates.template import template


@template(
    route="/check_meeting_detail",
    header_url="/",
    page_text="약속 현황보기",
    need_login_type="check_meeting_login",
    on_load=State.setting_month_calendar_and_get_check_meeting(),
)
def check_meeting_detail() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.tabs.root(
                rx.hstack(
                    rx.tabs.list(
                        rx.tabs.trigger("약속 정보", value="tab1"),
                        rx.tabs.trigger("참여 정보", value="tab2"),
                        width="270px",
                    ),
                    rx.center(
                        rx.cond(
                            State.is_host,
                            rx.cond(
                                State.meeting_state == "CONFIRMED",
                                rx.box(),
                                rx.drawer.root(
                                    rx.drawer.trigger(
                                        rx.button(
                                            rx.icon(
                                                tag="settings",
                                                size=24,
                                                stroke_width=1,
                                            ),
                                            color=AppColor.BLACK,
                                            background_color=AppColor.WHITE,
                                            padding="0px",
                                        ),
                                    ),
                                    rx.drawer.overlay(z_index="5"),
                                    rx.drawer.portal(
                                        rx.drawer.content(
                                            rx.center(
                                                rx.vstack(
                                                    rx.alert_dialog.root(
                                                        rx.alert_dialog.trigger(
                                                            rx.button(
                                                                "약속 삭제하기",
                                                                width="300px",
                                                                background_color="#DF0000",
                                                            ),
                                                        ),
                                                        rx.alert_dialog.content(
                                                            rx.alert_dialog.title(
                                                                "정말로 약속을 삭제하시겠습니까?"
                                                            ),
                                                            rx.alert_dialog.description(
                                                                "약속을 삭제하면, 약속 생성자를 포함한 모든 참여자의 약속이 삭제됩니다.",
                                                            ),
                                                            rx.flex(
                                                                rx.alert_dialog.cancel(
                                                                    rx.button(
                                                                        "아니요, 삭제하지 않을게요!"
                                                                    ),
                                                                ),
                                                                rx.alert_dialog.action(
                                                                    rx.button(
                                                                        "네, 삭제할게요!",
                                                                        on_click=State.check_meeting_detail_delete_appointment,
                                                                    ),
                                                                ),
                                                                spacing="3",
                                                            ),
                                                        ),
                                                    ),
                                                    rx.button(
                                                        "약속 확정하기",
                                                        width="300px",
                                                        background_color="#00A41A",
                                                        on_click=rx.redirect(
                                                            "/check_candidate"
                                                        ),
                                                    ),
                                                    rx.button(
                                                        "약속 변경하기",
                                                        width="300px",
                                                        on_click=State.change_join_meeting,
                                                    ),
                                                    spacing="3",
                                                ),
                                                width="100%",
                                            ),
                                            align="center",
                                            top="auto",
                                            right="auto",
                                            height="30%",
                                            width="100%",
                                            padding="2em",
                                            background_color="#FFF",
                                            border_radius="1em 1em 0 0",
                                        )
                                    ),
                                    direction="bottom",
                                ),
                            ),
                            rx.box(),
                        ),
                        rx.button(
                            rx.icon(
                                tag="share",
                                size=24,
                                stroke_width=1,
                            ),
                            color=AppColor.BLACK,
                            background_color=AppColor.WHITE,
                            padding_left="5px",
                        ),
                        width="80px",
                        height="40px",
                    ),
                ),
                rx.tabs.content(
                    rx.center(
                        rx.vstack(
                            rx.box(),
                            main_sub_text_box(
                                State.meeting_name, "약속이름", change_position=True
                            ),
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
                                    State.meeting_notice,
                                    "공지사항",
                                    change_position=True,
                                ),
                                rx.box(),
                            ),
                            rx.box(
                                rx.hstack(
                                    sub_text_box("약속코드"),
                                    rx.button(
                                        rx.icon("copy"),
                                        on_click=rx.set_clipboard(
                                            State.check_detail_meeting_code
                                        ),
                                        width="12px",
                                        height="12px",
                                        padding="0",
                                        color=AppColor.GRAY_TEXT,
                                        background_color=AppColor.WHITE,
                                    ),
                                ),
                                main_text_box(State.check_detail_meeting_code),
                            ),
                            main_sub_text_box(
                                State.host_name, "모임장", change_position=True
                            ),
                            rx.box(height="90px"),
                            spacing="4",
                        ),
                        width="100%",
                        height="60%",
                    ),
                    value="tab1",
                ),
                rx.tabs.content(
                    # tab2
                    calendar_header(purpose="check"),
                    rx.box(height="10px"),
                    rx.center(
                        rx.vstack(
                            main_sub_text_box(
                                State.check_meeting_detail_display_clicked_date,
                                "선택한 일정",
                                change_position=True,
                            ),
                            rx.scroll_area(
                                rx.flex(
                                    rx.foreach(
                                        State.check_meeting_detail_display_clicked_date_data,
                                        display_select_date,
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                type="always",
                                scrollbars="vertical",
                                style={"height": 100, "width": 360},
                            ),
                        ),
                        width="100%",
                        height="30%",
                    ),
                    value="tab2",
                ),
                rx.cond(
                    State.meeting_state == "CONFIRMED",
                    rx.button(
                        "확정된 약속입니다.",
                        width="360px",
                        height="35px",
                        disabled=True,
                        color=AppColor.WHITE,
                        background_color="#00A41A",
                    ),
                    rx.cond(
                        State.is_participated,
                        rx.vstack(
                            main_button(
                                text="참여 변경하기",
                                on_click=rx.redirect(
                                    f"/enter_meeting_code/{State.check_detail_meeting_code}"
                                ),
                            ),
                            main_button(
                                text="참여 취소하기",
                                sub_button=True,
                                on_click=State.change_meeting_delete_join,
                            ),
                        ),
                        main_button(
                            text="참여하기",
                            on_click=rx.redirect(
                                f"/enter_meeting_code/{State.check_detail_meeting_code}"
                            ),
                        ),
                    ),
                ),
                width="360px",
                default_value="tab1",
            ),
            width="100%",
        ),
        width="100%",
        height="100%",
    )
