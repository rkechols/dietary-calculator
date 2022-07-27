from typing import Set

from dietary_calculator.attribute import DietaryAttributeHierarchy
from dietary_calculator.paradigm import DietaryParadigm
from dietary_calculator.product import FoodProduct


class DietaryCalculator:
    def __init__(self, attribute_hierarchy: DietaryAttributeHierarchy = None):
        self.attribute_hierarchy = attribute_hierarchy if attribute_hierarchy is not None else DietaryAttributeHierarchy()

    def get_all_classifications(self, food: FoodProduct) -> Set[str]:
        to_return = set()
        for base_attribute in food.attributes:
            to_return.update(self.attribute_hierarchy.get_all_classifications(base_attribute))
        return to_return

    def paradigm_allows_food(self, paradigm: DietaryParadigm, food: FoodProduct) -> bool:
        all_classifications = self.get_all_classifications(food)
        to_return = paradigm.allow_attributes(all_classifications)
        return to_return
