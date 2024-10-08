import reflex as rx

from gatherplan_client.backend.state import State
from gatherplan_client.components.schema import AppColor, TextSize, AppFontFamily
from gatherplan_client.components.text_box import (
    center_align_text_box,
    input_box,
    main_button,
)


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


@rx.page("/login")
def login() -> rx.Component:
    return rx.center(
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


@rx.page("/login_check_meeting")
def login_check_meeting() -> rx.Component:
    return rx.center(
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
