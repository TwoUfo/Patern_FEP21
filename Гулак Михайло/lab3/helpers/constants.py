from classes import (
    BasicContainer,
    HeavyContainer,
    RefrigeratedContainer,
    LiquidContainer,
)

from classes import SmallItem, HeavyItem, RefrigeratedItem, LiquidItem

DESERIALIZATION_FILE_PATH = "input.json"
SERIALIZATION_FILE_PATH = "output.json"

CONTAINERS_MAPPING = {
    "basic": BasicContainer,
    "heavy": HeavyContainer,
    "refrigerated": RefrigeratedContainer,
    "liquid": LiquidContainer,
}

ITEMS_MAPPING = {
    "small": SmallItem,
    "heavy": HeavyItem,
    "refrigerated": RefrigeratedItem,
    "liquid": LiquidItem,
}
