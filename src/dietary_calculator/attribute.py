from typing import Dict, Set


class DietaryAttribute:
    """
    Really just a hierarchy of strings
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
    SOY = "soy"
    ALCOHOL = "alcohol"
    COFFEE = "coffee"
    TEA = "tea"

    # key is an attribute,
    # value is a set of attributes that are "parents" of the key
    hierarchy: Dict[str, Set[str]] = {
        DAIRY: {ANIMAL_PRODUCT},
        EGG: {ANIMAL_PRODUCT},
        MEAT: {ANIMAL_PRODUCT},
        FISH: {MEAT},
        SHELLFISH: {FISH},
        PORK: {MEAT},
        WHEAT: {GLUTEN}
    }

    @classmethod
    def get_all_classifications(cls, attribute: str) -> Set[str]:
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
                next_level.update(cls.hierarchy.get(attribute, set()))
            # discard any parents that we've already seen
            next_level -= all_seen
            # move to the next level
            this_level = next_level
        return all_seen
