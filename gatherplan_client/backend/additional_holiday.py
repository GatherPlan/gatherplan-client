import datetime
from typing import List


def additional_holiday(year: int) -> List[datetime.date]:
    if year == 2024:
        return [
            datetime.date(2024, 2, 12),
            datetime.date(2024, 4, 10),
            datetime.date(2024, 5, 6),
        ]
    elif year == 2025:
        return [
            datetime.date(2025, 3, 3),
            datetime.date(2025, 5, 6),
        ]

    elif year == 2026:
        return [
            datetime.date(2026, 3, 2),
            datetime.date(2026, 5, 25),
            datetime.date(2026, 6, 8),
            datetime.date(2026, 8, 17),
            datetime.date(2026, 10, 5),
        ]
    else:
        return []
