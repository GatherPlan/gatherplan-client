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


# Thanks 6mini: https://github.com/6mini/holidayskr/blob/main/holidayskr.json
# "year_specific_holidays": {
#         "2024": [
#             {"date": "02-12", "name": "대체 공휴일(설날)"},
#             {"date": "04-10", "name": "제22대 국회의원 선거일"},
#             {"date": "05-06", "name": "대체 공휴일(어린이날)"}
#         ],
#         "2025": [
#             {"date": "03-03", "name": "대체 공휴일(3·1절)"},
#             {"date": "05-06", "name": "대체 공휴일(어린이날, 석가탄신일 중복 공휴일)"}
#         ],
#         "2026": [
#             {"date": "03-02", "name": "대체 공휴일(3·1절)"},
#             {"date": "05-25", "name": "대체 공휴일(석가탄신일)"},
#             {"date": "06-08", "name": "대체 공휴일(현충일)"},
#             {"date": "08-17", "name": "대체 공휴일(광복절)"},
#             {"date": "10-05", "name": "대체 공휴일(한글날)"}
#         ]
#     }
