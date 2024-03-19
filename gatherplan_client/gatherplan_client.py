import reflex as rx
from .index import index
from .sign_up import sign_up


app = rx.App(stylesheets=["fonts/myfont.css"], title="GatherPlan")
app.add_page(index)
app.add_page(sign_up, route="/sign_up")
