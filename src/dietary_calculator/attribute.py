import copy
from typing import Dict, Set


class DietaryAttribute:
    """
    Extensible enum for different attributes of food, relating to dietary restrictions.
    Add a value for your runtime by simple assignment:
    ```python
    DietaryAttribute.MY_ATTR = "new_value"
    ```
    """
    DAIRY = "dairy"
    EGG = "egg"
    MEAT = "meat"
    FISH = "fish"
    SHELLFISH = "shellfish"
    PORK = "pork"
    ANIMAL_PRODUCT = "animal product"
    WHEAT = "wheat"
    GLUTEN = "gluten"
    NUTS = "nuts"
    PEANUTS = "peanuts"
    SOY = "soy"
    ALCOHOL = "alcohol"
    COFFEE = "coffee"
    TEA = "tea"

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("DietaryAttribute is an extensible enum and cannot be instantiated")


class DietaryAttributeHierarchy:
    """
    A hierarchy of dietary attributes.
    Really represented as a dictionary that maps a string to a set of strings,
    where each key is an attribute, and its value is its set of direct parents.
    e.g. If a key "dairy" maps to a set including "animal product", we know that
    "dairy" is a type of "animal product".
    """

    # key is an attribute,
    # value is a set of attributes that are "parents" of the key
    _DEFAULT_HIERARCHY: Dict[str, Set[str]] = {
        DietaryAttribute.DAIRY: {DietaryAttribute.ANIMAL_PRODUCT},
        DietaryAttribute.EGG: {DietaryAttribute.ANIMAL_PRODUCT},
        DietaryAttribute.MEAT: {DietaryAttribute.ANIMAL_PRODUCT},
        DietaryAttribute.PORK: {DietaryAttribute.MEAT},
        DietaryAttribute.FISH: {DietaryAttribute.MEAT},
        DietaryAttribute.SHELLFISH: {DietaryAttribute.FISH},
        DietaryAttribute.WHEAT: {DietaryAttribute.GLUTEN},
        DietaryAttribute.PEANUTS: {DietaryAttribute.NUTS},
    }

    def __init__(self, hierarchy: Dict[str, Set[str]] = None):
        self.hierarchy = hierarchy if hierarchy is not None else copy.deepcopy(self._DEFAULT_HIERARCHY)

    def get_all_classifications(self, attribute: str) -> Set[str]:
        """
        Get all the ways of naming an attribute,
        i.e. itself and all of its parents / ancestors in the hierarchy.
        """
        all_seen: Set[str] = set()
        this_level: Set[str] = {attribute}
        while len(this_level) > 0:
            # record this level
            all_seen.update(this_level)
            # get all the parents
            next_level: Set[str] = set()
            for attribute in this_level:
                next_level.update(self.hierarchy.get(attribute, set()))
            # discard any parents that we've already seen
            next_level -= all_seen
            # move to the next level
            this_level = next_level
        return all_seen

    def __str__(self) -> str:
        lines = ["DietaryAttributeHierarchy:"]
        for attribute, parents in self.hierarchy.items():
            lines.append(f"  {repr(attribute)}\tis a type of\t{parents}")
        to_return = "\n".join(lines)
        return to_return
