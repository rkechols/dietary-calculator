from typing import Set


class FoodProduct:
    """
    A food product, which has a name and a set of dietary attributes.
    """
    def __init__(self, name: str, attributes: Set[str]):
        self.name = name
        self.attributes = attributes

    def __repr__(self) -> str:
        to_return = f"{self.__class__.__name__}({repr(self.name)}, {repr(self.attributes)})"
        return to_return
