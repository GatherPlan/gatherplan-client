import reflex as rx


def buffer_box(buffer_height: str):
    return rx.center(
        text_align="center",
        width="100%",
        height=buffer_height,
    )
