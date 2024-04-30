from dataclasses import dataclass
from enum import Enum


@dataclass
class AppColor(str, Enum):
    MAIN_BACKGROUND: str = "#3A7DFF"
    GRAY_TEXT: str = "#797979"
    LIGHT_GRAY_TEXT: str = "#D1D1D1"
    BACKGROUND_COLOR: str = "#FAFAFA"
    BACKGROUND_GRAY_COLOR: str = "#EEEEEE"
    WHITE: str = "#FFFFFF"
    BLACK: str = "#000000"
    RED: str = "#FF0000"
    BLUE: str = "#0000FF"
    SKY_BLUE: str = "0085FF"


@dataclass
class AppFontFamily(str, Enum):
    JALNAN_GOTHIC: str = "JalnanGothic"
    DEFAULT_FONT: str = "Pretendard-Regular"


@dataclass
class TextSize(str, Enum):
    VERY_TINY: str = "10px"
    TINY: str = "12px"
    TINY_SMALL: str = "14px"
    SMALL: str = "16px"
    SMALL_MEDIUM: str = "20px"
    MEDIUM: str = "24px"
    LARGE: str = "32px"
