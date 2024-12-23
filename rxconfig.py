import reflex as rx
import os

config = rx.Config(
    app_name="gatherplan_client",
    api_url=os.getenv("API_URL", "http://localhost:8000"),
    deploy_url=os.getenv("DEPLOY_URL", "http://localhost:3000"),
    dev_mode=True,
    fronted_packages=[],
    tailwind=None,
)
