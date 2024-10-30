import os
from .pages import *  # noqa: F401, F403


def create_app() -> rx.App:
    """애플리케이션 인스턴스를 생성합니다."""
    common_head_components = [
        rx.el.meta(
            name="viewport",
            content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0",
        ),
    ]

    if os.environ.get("ENV") == "prod":
        # 프로덕션 환경일 때는 Google 사이트 인증 메타 태그 추가
        prod_meta = rx.el.meta(
            name="google-site-verification",
            content="beqAu5H-vKsKPxSVN6z3hpR6ydUfSKqWjcmzqY-6000",
        )
        head_components = [prod_meta] + common_head_components
    else:
        head_components = common_head_components

    return rx.App(
        stylesheets=["fonts/myfont.css"],
        title="GatherPlan",
        head_components=head_components,
    )


app = create_app()


def health_check() -> rx.Component:
    """헬스 체크 엔드포인트"""
    return rx.box("pong")


# 라우트 등록
app.add_page(health_check, route="/ping")
app.add_page(enter_meeting_code, route="/enter_meeting_code/[meeting_code_params]")
