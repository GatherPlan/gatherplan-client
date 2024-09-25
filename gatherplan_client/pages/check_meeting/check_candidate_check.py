# import reflex as rx
#
# from gatherplan_client.backend.state import State
# from gatherplan_client.components.header import header
# from gatherplan_client.components.schema import AppFontFamily, AppColor
#
#
# @rx.page("/check_candidate", on_load=State.get_appointments_candidates)
# # @need_login
# def check_candidate() -> rx.Component:
#     return rx.vstack(
#         header("/check_meeting_detail"),
#         rx.center(
#             rx.text(
#                 "약속 확정하기",
#                 font_size="20px",
#                 padding_top="28px",
#                 padding_bottom="40px",
#                 padding_left="10px",
#                 font_family=AppFontFamily.DEFAULT_FONT,
#                 font_weight="700",
#                 width="360px",
#             ),
#             width="100%",
#             height="15%",
#         ),
#         rx.center(
#             rx.vstack(
#                 rx.text(
#                     "약속 시간 후보 목록",
#                     font_size="14px",
#                     font_family=AppFontFamily.DEFAULT_FONT,
#                     font_weight="700",
#                     padding_left="10px",
#                     color=AppColor.BLACK,
#                     width="360px",
#                 ),
#                 rx.text(
#                     "참여율, 약속 구간 길이, 날씨를 기준으로 정렬된 결과가 반환됩니다.",
#                     font_size="12px",
#                     font_family=AppFontFamily.DEFAULT_FONT,
#                     color=AppColor.GRAY_TEXT,
#                     font_weight="700",
#                     padding_left="10px",
#                     padding_bottom="5px",
#                     width="360px",
#                 ),
#                 align="center",
#                 width="100%",
#             ),
#             width="100%",
#         ),
#         rx.scroll_area(
#             rx.flex(
#                 rx.box(
#                     rx.vstack(
#                         rx.box(
#                             rx.vstack(
#                                 rx.text(
#                                     "검색결과",
#                                     font_size="12px",
#                                     font_family=AppFontFamily.DEFAULT_FONT,
#                                     font_weight="700",
#                                     color=AppColor.SUB_TEXT,
#                                     padding_left="10px",
#                                 ),
#                                 rx.foreach(
#                                     State.meeting_confirm_display_data,
#                                     list_view_candidate,
#                                 ),
#                             ),
#                             width="360px",
#                         ),
#                         width="100%",
#                         align="center",
#                         padding_top="20px",
#                     ),
#                     width="100%",
#                 ),
#                 direction="column",
#                 spacing="4",
#             ),
#             type="scroll",
#             scrollbars="vertical",
#             style={"height": "40%"},
#         ),
#         rx.center(
#             rx.vstack(
#                 rx.text(
#                     "사용자 참여 목록",
#                     font_size="14px",
#                     font_family=AppFontFamily.DEFAULT_FONT,
#                     font_weight="700",
#                     padding_left="10px",
#                     color=AppColor.BLACK,
#                     width="360px",
#                 ),
#                 rx.text(
#                     State.meeting_confirm_display_data_user,
#                     font_size="12px",
#                     font_family=AppFontFamily.DEFAULT_FONT,
#                     color=AppColor.GRAY_TEXT,
#                     font_weight="700",
#                     padding_left="10px",
#                     padding_bottom="5px",
#                     width="360px",
#                 ),
#                 align="center",
#                 width="100%",
#             ),
#             width="100%",
#         ),
#         rx.center(
#             rx.vstack(
#                 rx.button(
#                     "다음",
#                     width="348px",
#                     height="35px",
#                     padding="20px",
#                     color=AppColor.BLACK,
#                     type="submit",
#                     background_color=AppColor.SUB_TEXT,
#                     on_click=State.change_meeting_delete_join,
#                 ),
#             ),
#             width="100%",
#             padding_top="10px",
#         ),
#         spacing="0",
#         height="100vh",
#     )
