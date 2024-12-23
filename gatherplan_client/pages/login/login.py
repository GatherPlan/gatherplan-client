import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.buttons import main_button
from gatherplan_client.components.schema import AppColor, TextSize, AppFontFamily
from gatherplan_client.components.text_box import (
    center_align_text_box,
    input_box,
    sub_text_box,
)
from gatherplan_client.components.header import header
from gatherplan_client.components.footer import footer


def need_login(func):
    def inner():
        return rx.cond(
            State.login_token == "",
            rx.cond(State.not_member_login, func(), login()),
            func(),
        )

    return inner


def need_login_check_meeting(func):
    def inner():
        return rx.cond(
            State.login_token == "",
            rx.cond(State.not_member_login, func(), login_check_meeting()),
            func(),
        )

    return inner


def need_login_check_meeting_login_purpose(func):
    def inner():
        return rx.cond(
            State.login_token == "",
            login_check_meeting(),
            func(),
        )

    return inner


def login_layout(content: rx.Component) -> rx.Component:
    return rx.box(
        rx.vstack(
            header(),
            rx.hstack(
                rx.box(
                    footer(is_vertical=True),
                    width="240px",
                    height="100vh",
                    position="sticky",
                    top="0",
                    display=["none", "none", "block"],
                ),
                rx.box(
                    rx.box(
                        content,
                        width="100%",
                        max_width="600px",
                        margin="0 auto",
                        bg="white",
                        border_x="1px solid #eaeaea",
                        min_height="100vh",
                        padding_top="50px",
                    ),
                    flex="1",
                    min_height="100vh",
                ),
                width="100%",
                spacing="0",
                align_items="stretch",
            ),
            rx.box(
                footer(is_vertical=False),
                width="100%",
                position="fixed",
                bottom="0",
                left="0",
                display=["block", "block", "none"],
            ),
            height="100vh",
            spacing="0",
        ),
        bg="rgb(250, 250, 250)",
    )


@rx.page("/login")
def login() -> rx.Component:
    return login_layout(
        rx.center(
            rx.vstack(
                center_align_text_box(
                    main_text="Gather Plan",
                    sub_text="게더플랜에서 모임의 약속을 잡아보세요",
                ),
                rx.cond(
                    State.not_member_login_button,
                    rx.form(
                        rx.text(
                            "이메일",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="email@naver.com",
                            name="email",
                        ),
                        rx.box(
                            "비밀번호",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="2~8자리",
                            name="password",
                            type="password",
                        ),
                        main_button(text="로그인", type="submit"),
                        rx.hstack(
                            rx.button(
                                "비밀번호 찾기",
                                width="180px",
                                height="36px",
                                color="#A3A3A3",
                                type="button",
                                background_color="#FFFFFF",
                                on_click=rx.toast.error(
                                    "비밀번호 찾기 기능은 준비 중입니다."
                                ),
                            ),
                            rx.button(
                                "회원가입",
                                width="180px",
                                height="36px",
                                color="#A3A3A3",
                                type="button",
                                background_color="#FFFFFF",
                                on_click=rx.redirect("/sign_up"),
                            ),
                            width="100%",
                            spacing="0",
                        ),
                        on_submit=State.login_handle_submit,
                        width="100%",
                        align="center",
                    ),
                    rx.form(
                        rx.text(
                            "닉네임",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="닉네임을 입력해주세요",
                            name="nick_name",
                        ),
                        rx.box(
                            "비밀번호",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="비밀번호를 입력해주세요",
                            name="password",
                            type="password",
                        ),
                        main_button(text="시작하기", type="submit"),
                        reset_on_submit=False,
                        on_submit=State.start_not_member_login,
                        width="100%",
                        align="center",
                    ),
                ),
                rx.box(height="40vh"),
                rx.cond(
                    State.not_member_login_button,
                    sub_text_box("회원가입없이 간편하게 이용해보세요"),
                    rx.text(),
                ),
                rx.button(
                    rx.cond(
                        State.not_member_login_button,
                        rx.text(
                            "비회원으로 시작하기",
                        ),
                        rx.text(
                            "회원으로 시작하기",
                        ),
                    ),
                    width="360px",
                    height="35px",
                    color=AppColor.WHITE,
                    type="button",
                    background_color=AppColor.LIGHT_GRAY_TEXT,
                    on_click=State.change_login_not_member,
                ),
                width="360px",
            ),
            width="100%",
        )
    )


@rx.page("/login_check_meeting")
def login_check_meeting() -> rx.Component:
    return login_layout(
        rx.center(
            rx.vstack(
                center_align_text_box(
                    main_text="Gather Plan",
                    sub_text="게더플랜에서 모임의 약속을 잡아보세요",
                ),
                rx.cond(
                    State.not_member_login_button,
                    rx.form(
                        rx.text(
                            "이메일",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="email@naver.com",
                            name="email",
                        ),
                        rx.box(
                            "비밀번호",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="2~8자리",
                            name="password",
                            type="password",
                        ),
                        main_button(text="로그인", type="submit"),
                        rx.hstack(
                            rx.button(
                                "비밀번호 찾기",
                                width="180px",
                                height="36px",
                                color="#A3A3A3",
                                type="button",
                                background_color="#FFFFFF",
                                on_click=rx.toast.error(
                                    "비밀번호 찾기 기능은 준비 중입니다."
                                ),
                            ),
                            rx.button(
                                "회원가입",
                                width="180px",
                                height="36px",
                                color="#A3A3A3",
                                type="button",
                                background_color="#FFFFFF",
                                on_click=rx.redirect("/sign_up"),
                            ),
                            width="100%",
                            spacing="0",
                        ),
                        rx.box(height="43vh"),
                        width="100%",
                        on_submit=State.login_handle_submit,
                    ),
                    rx.form(
                        rx.text(
                            "약속 코드",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="약속 코드를 입력해주세요",
                            name="meeting_code",
                        ),
                        rx.text(
                            "닉네임",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="닉네임을 입력해주세요",
                            name="nick_name",
                        ),
                        rx.box(
                            "비밀번호",
                            font_size=TextSize.VERY_TINY,
                            font_family=AppFontFamily.DEFAULT_FONT,
                            width="360px",
                        ),
                        input_box(
                            placeholder="비밀번호를 입력해주세요",
                            name="password",
                            type="password",
                        ),
                        main_button(text="시작하기", type="submit"),
                        rx.box(height="37vh"),
                        width="100%",
                        on_submit=State.start_not_member_login_check_meeting,
                    ),
                ),
                rx.button(
                    rx.cond(
                        State.not_member_login_button,
                        rx.text(
                            "비회원으로 시작하기",
                        ),
                        rx.text(
                            "회원으로 시작하기",
                        ),
                    ),
                    width="360px",
                    height="35px",
                    color=AppColor.WHITE,
                    type="button",
                    background_color=AppColor.LIGHT_GRAY_TEXT,
                    on_click=State.change_login_not_member,
                ),
                width="360px",
            ),
            width="100%",
        )
    )
