import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.calendar import display_select_date, calendar_header
from gatherplan_client.components.header import header
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.pages.login.login import need_login


@need_login
def check_meeting_detail() -> rx.Component:
    return rx.vstack(
        header("/check_meeting"),
        rx.center(
            rx.text(
                "약속 현황보기",
                font_size="20px",
                padding_top="28px",
                padding_bottom="40px",
                padding_left="10px",
                font_family=AppFontFamily.DEFAULT_FONT,
                font_weight="700",
                width="300px",
            ),
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
                                                rx.button("아니요, 삭제하지 않을게요!"),
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
                                    on_click=rx.redirect("/check_candidate"),
                                ),
                                rx.button("약속 변경하기", width="300px"),
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
            width="100%",
            height="10%",
        ),
        rx.center(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("약속 정보", value="tab1"),
                    rx.tabs.trigger("참여 정보", value="tab2"),
                ),
                rx.tabs.content(
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
                                        State.full_address,
                                        href=State.address_kakao_link,
                                        font_size="14px",
                                        font_family=AppFontFamily.DEFAULT_FONT,
                                        font_weight="700",
                                        color=AppColor.BLACK,
                                        padding_bottom="5px",
                                    ),
                                    rx.text(
                                        State.place_name,
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
                                rx.vstack(
                                    rx.box(
                                        rx.text(
                                            "선택한 일정",
                                            font_size="14px",
                                            font_family=AppFontFamily.DEFAULT_FONT,
                                            font_weight="700",
                                            color=AppColor.GRAY_TEXT,
                                            padding_left="10px",
                                        ),
                                        width="360px",
                                    ),
                                    rx.hstack(
                                        rx.foreach(
                                            State.candidate_list,
                                            display_select_date,
                                        ),
                                        spacing="2",
                                    ),
                                ),
                                width="100%",
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
                                    rx.box(
                                        rx.text(
                                            State.check_detail_meeting_code,
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
                        padding_top="10px",
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
                                on_click=rx.redirect(
                                    f"/enter_meeting_code/{State.check_detail_meeting_code}"
                                ),
                            ),
                        ),
                        width="100%",
                    ),
                    rx.center(
                        rx.vstack(
                            rx.button(
                                "참여 취소하기",
                                width="348px",
                                height="35px",
                                padding="20px",
                                color=AppColor.BLACK,
                                type="submit",
                                background_color=AppColor.SUB_TEXT,
                                on_click=rx.redirect("/join_meeting_date"),
                            ),
                        ),
                        width="100%",
                        padding_top="10px",
                    ),
                    value="tab1",
                ),
                rx.tabs.content(
                    # tab2
                    calendar_header(),
                    rx.center(
                        rx.vstack(
                            rx.box(
                                rx.text(
                                    "선택한 일정",
                                    font_size="14px",
                                    font_family=AppFontFamily.DEFAULT_FONT,
                                    font_weight="700",
                                    color=AppColor.GRAY_TEXT,
                                    padding_left="10px",
                                ),
                                width="360px",
                            ),
                            rx.scroll_area(
                                rx.flex(
                                    rx.foreach(
                                        State.display_select_date,
                                        display_select_date,
                                    ),
                                    direction="column",
                                    spacing="4",
                                ),
                                type="always",
                                scrollbars="vertical",
                                style={"height": 120, "width": 360},
                            ),
                        ),
                        width="100%",
                        height="30%",
                    ),
                    rx.center(
                        rx.vstack(
                            rx.button(
                                "참여 변경하기",
                                width="348px",
                                height="35px",
                                padding="20px",
                                color=AppColor.WHITE,
                                type="submit",
                                background_color=AppColor.MAIN_COLOR,
                                on_click=rx.redirect(""),
                            ),
                        ),
                        width="100%",
                    ),
                    rx.center(
                        rx.vstack(
                            rx.button(
                                "참여 취소하기",
                                width="348px",
                                height="35px",
                                padding="20px",
                                color=AppColor.BLACK,
                                type="submit",
                                background_color=AppColor.SUB_TEXT,
                                on_click=rx.redirect("/join_meeting_date"),
                            ),
                        ),
                        width="100%",
                        padding_top="10px",
                    ),
                    value="tab2",
                ),
                width="360px",
                default_value="tab1",
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
