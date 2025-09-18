from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(ABC):
    _id: int | None
    _power: int
    _name: str | None
    _description: str
    _accuracy: int | None
    _element: str | None
    _TYPE_NAME: str

    def __init__(
        self,
        id: int | None = None,
        power: int | None = None,
        name: str | None = None,
        description: str | None = None,
        accuracy: int | None = None,
        element: str | None = None,
    ) -> None:
        self._id = id
        self._power = 0 if power is None else power
        self._name = name
        self._description = "" if description is None else description
        self._accuracy = accuracy
        self._element = element

    @abstractmethod
    def compute_damage(
        self, attacker: "AbstractPokemon", defender: "AbstractPokemon"
    ) -> int:
        """
         Return the damage of the attack.
         It's an abstract method because some attack will
         have variable damages, others have fixed damages

        Returns:
            int : the damage of the attack
        """
        pass

    @property
    def power(self) -> int:
        return self._power

    @property
    def name(self) -> str | None:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def id(self) -> int | None:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def element(self) -> str | None:
        return self._element

    @property
    def accuracy(self) -> int | None:
        return self._accuracy

    @property
    def type(self):
        return self._TYPE_NAME
