from abc import ABC, abstractmethod
from typing import Set


class DietaryParadigm(ABC):
    """
    This class is used to represent a set of dietary rules, restrictions, and requirements.
    """

    @abstractmethod
    def allow_attributes(self, attributes: Set[str]) -> bool:
        """
        Return whether the given attribute set is allowed or not.
        """
        raise NotImplementedError(f"{self.__class__.__name__} is an abstract class; this method must be implemented by a child class")
