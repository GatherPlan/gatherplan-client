from typing import List

import reflex as rx

from gatherplan_client.login import need_login
from gatherplan_client.reflex_assets.buffer_box import buffer_box
from gatherplan_client.reflex_assets.buttons import make_meeting_time_button
from gatherplan_client.reflex_assets.header import header
from gatherplan_client.reflex_assets.schema import TextSize, AppColor
from gatherplan_client.reflex_assets.text_box import left_align_text_box


class TimeSelect(rx.State):
    select_time: List[str] = ["오전", "오후"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def click_button(self, click_data: List):
        if click_data in self.select_time:
            self.select_time.remove(click_data)
        else:
            self.select_time.append(click_data)


@need_login
def make_meeting_time() -> rx.Component:
    return rx.vstack(
        header("약속만들기"),
        left_align_text_box(
            "약속 시간대를 골라주세요",
            "사용자 지정은 중복 선택이 불가합니다.",
            main_font_size=TextSize.TINY_SMALL,
            sub_font_size=TextSize.TINY,
        ),
        rx.center(
            rx.vstack(
                rx.cond(
                    TimeSelect.select_time.contains("오전"),
                    make_meeting_time_button(
                        main_text="오전",
                        sub_text="06:00 ~ 12:00",
                        on_click_func=TimeSelect.click_button("오전"),
                        text_color="#3A7DFF",
                    ),
                    make_meeting_time_button(
                        main_text="오전",
                        sub_text="06:00 ~ 12:00",
                        on_click_func=TimeSelect.click_button("오전"),
                    ),
                ),
                rx.cond(
                    TimeSelect.select_time.contains("오후"),
                    make_meeting_time_button(
                        main_text="오후",
                        sub_text="06:00 ~ 12:00",
                        on_click_func=TimeSelect.click_button("오후"),
                        text_color="#3A7DFF",
                    ),
                    make_meeting_time_button(
                        main_text="오후",
                        sub_text="06:00 ~ 12:00",
                        on_click_func=TimeSelect.click_button("오후"),
                    ),
                ),
                rx.cond(
                    TimeSelect.select_time.contains("저녁"),
                    make_meeting_time_button(
                        main_text="저녁",
                        sub_text="06:00 ~ 12:00",
                        on_click_func=TimeSelect.click_button("저녁"),
                        text_color="#3A7DFF",
                    ),
                    make_meeting_time_button(
                        main_text="저녁",
                        sub_text="06:00 ~ 12:00",
                        on_click_func=TimeSelect.click_button("저녁"),
                    ),
                ),
            ),
            width="100%",
        ),
        buffer_box("5%"),
        rx.center(
            rx.button(
                "다음",
                width="348px",
                height="48px",
                padding="20px",
                color=AppColor.WHITE,
                type="submit",
                background_color=AppColor.MAIN_BACKGROUND,
                on_click=rx.redirect("/make_meeting_check"),
            ),
            width="100%",
        ),
        spacing="0",
        height="100vh",
    )
