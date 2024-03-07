import reflex as rx
from .index import index
from .sign_up import sign_up_page

app = rx.App()
app.add_page(index)
app.add_page(sign_up_page, route="/sign_up")
