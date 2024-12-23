from typing import Dict

import reflex as rx

from gatherplan_client.backend.state import State


def location_button(button_text: Dict):
    return rx.cond(
        button_text["location_type"] == "DETAIL_ADDRESS",
        rx.drawer.close(
            rx.button(
                rx.vstack(
                    rx.text(button_text["place_name"]),
                    rx.text(button_text["address_name"], font_size="10px"),
                    spacing="0",
                    align="center",
                    width="360px",
                ),
                width="360px",
                height="48px",
                color="#A3A3A3",
                type="button",
                on_click=State.make_meeting_detail_handle_location_submit(button_text),
                background_color="#FFFFFF",
            )
        ),
        rx.drawer.close(
            rx.button(
                button_text["address_name"],
                width="360px",
                height="36px",
                color="#A3A3A3",
                type="button",
                on_click=State.make_meeting_detail_handle_location_submit(button_text),
                background_color="#FFFFFF",
            ),
        ),
    )
