import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, AppFontFamily
from gatherplan_client.templates.template import template


@template(
    route="/check_candidate_result",
    header_url="/check_candidate",
    page_text="",
)
def check_candidate_result() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.vstack(
                rx.text(
                    "정상적으로 약속이 확정되었습니다.",
                    font_size="18px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    font_weight="700",
                    color=AppColor.BLACK,
                    align="center",
                    width="360px",
                ),
                rx.text(
                    "정해진 약속 일정을 참여자들과 공유해보세요",
                    font_size="12px",
                    font_family=AppFontFamily.DEFAULT_FONT,
                    color=AppColor.GRAY_TEXT,
                    font_weight="700",
                    align="center",
                    width="360px",
                ),
            ),
            width="100%",
            height="15%",
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
                        "선택된 약속 시간",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        f"{State.confirm_date} {State.confirm_start_time} ~ {State.confirm_end_time}",
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
                        "사용자 참여 목록",
                        font_size="12px",
                        font_family=AppFontFamily.DEFAULT_FONT,
                        font_weight="700",
                        color=AppColor.GRAY_TEXT,
                    ),
                    rx.text(
                        State.meeting_confirm_display_data_user,
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
            height="55%",
        ),
        rx.center(
            rx.vstack(
                rx.button(
                    "현황보기",
                    width="348px",
                    height="25px",
                    padding="20px",
                    color=AppColor.WHITE,
                    type="button",
                    background_color=AppColor.MAIN_COLOR,
                    on_click=State.check_candidate_result_click_check_button,
                ),
                rx.button(
                    "공유하기",
                    width="348px",
                    height="25px",
                    padding="20px",
                    type="button",
                    color=AppColor.BLACK,
                    background_color=AppColor.BACKGROUND_GRAY_COLOR,
                    margin_top="5px",
                ),
            ),
            width="100%",
        ),
        width="100%",
        height="100%",
    )
