from typing import Set

from dietary_calculator.attribute import DietaryAttribute
from dietary_calculator.paradigm import DietaryParadigm


class SimpleDisallowParadigm(DietaryParadigm):
    def __init__(self, disallowed_attributes: Set[str]):
        super().__init__()
        self.disallowed_attributes = disallowed_attributes

    # override
    def allow_attributes(self, attributes: Set[str]) -> bool:
        overlap = self.disallowed_attributes & attributes
        is_safe = (len(overlap) == 0)
        return is_safe

    def __repr__(self) -> str:
        to_return = f"{self.__class__.__name__}(disallowed_attributes={self.disallowed_attributes})"
        return to_return


VEGETARIAN = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.MEAT
})

LACTO_VEGETARIAN = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.EGG,
    DietaryAttribute.MEAT
})

VEGAN = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.ANIMAL_PRODUCT
})

HALAL = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.ALCOHOL,
    DietaryAttribute.PORK
})

LATTER_DAY_SAINT = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.COFFEE,
    DietaryAttribute.TEA,
    DietaryAttribute.ALCOHOL
})

DAIRY_FREE = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.DAIRY
})

GLUTEN_FREE = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.GLUTEN
})

WHEAT_ALLERGY = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.WHEAT
})

SOY_ALLERGY = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.SOY
})

PEANUT_ALLERGY = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.PEANUTS
})

TREE_NUT_ALLERGY = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.NUTS
})

SHELLFISH_ALLERGY = SimpleDisallowParadigm(disallowed_attributes={
    DietaryAttribute.SHELLFISH
})
