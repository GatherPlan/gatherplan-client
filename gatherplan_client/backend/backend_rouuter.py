import os

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "https://test.gatherplan.site",
)

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://test-backed.gatherplan.site",
)

HEADER = {
    "accept": "*/*",
    "Content-Type": "application/json",
}
