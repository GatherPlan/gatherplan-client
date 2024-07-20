import os

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://test-backed.gatherplan.site",
)

HEADER = {
    "accept": "*/*",
    "Content-Type": "application/json",
}
