import reflex as rx
import os

config = rx.Config(
    app_name="gatherplan_client",
    api_url=os.getenv("API_URL", 'http://localhost:8000'),

)
