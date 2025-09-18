import copy

from abc import ABC, abstractmethod

from business_object.attack.abstract_attack import AbstractAttack
from business_object.statistic import Statistic


class AbstractPokemon(ABC):
    """
    An abstract pokemon. As an abstract class, it has to be inherited to be instantiated.
    """

    # -------------------------------------------------------------------------
    # Attributes
    # -------------------------------------------------------------------------

    _id: int | None
    _stat_max: Statistic
    _stat_current: Statistic
    _level: int
    _name: str | None
    _common_attacks: list[AbstractAttack]
    _special_attack: AbstractAttack | None

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(
        self,
        id: int | None = None,
        stat_max: Statistic | None = None,
        stat_current: Statistic | None = None,
        level: int = 0,
        name: str | None = None,
        common_attacks: list[AbstractAttack] = [],
        special_attack: AbstractAttack | None = None,
    ) -> None:
        # -----------------------------
        # Attributes
        # -----------------------------
        self._id = id
        self._stat_max = Statistic() if stat_max is None else stat_max
        self._stat_current = Statistic() if stat_current is None else stat_current
        self._level = level
        self._name = name
        self._common_attacks = common_attacks
        self._special_attack = special_attack

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        pass

    def level_up(self) -> None:
        """
        Increase the level by one
        """
        self._level += 1

    def reset_actual_stat(self) -> None:
        self._stat_current = copy.deepcopy(self._stat_max)

    def get_hit(self, damage: int) -> None:
        if damage > 0:
            if damage < self.hp_current:
                self.hp_current -= damage
            else:
                self.hp_current = 0

    def __str__(self) -> str:
        res = "I am " + str(self.name)
        res += ", level : " + str(self.level)
        res += ", hp : " + str(self.hp_current)
        return res

    # -------------------------------------------------------------------------
    # Getters and Setters
    # -------------------------------------------------------------------------

    @property
    def attack(self) -> int:
        return self._stat_max.attack

    @property
    def hp(self) -> int:
        return self._stat_max.hp

    @property
    def defense(self) -> int:
        return self._stat_max.defense

    @property
    def sp_atk(self) -> int:
        return self._stat_max.sp_atk

    @property
    def sp_def(self) -> int:
        return self._stat_max.sp_def

    @property
    def speed(self) -> int:
        return self._stat_max.speed

    # Current stat_max getter/setter
    @property
    def attack_current(self) -> int:
        return self._stat_current.attack

    @attack_current.setter
    def attack_current(self, value: int):
        self._stat_current.attack = value

    @property
    def hp_current(self) -> int:
        return self._stat_current.hp

    @hp_current.setter
    def hp_current(self, value: int) -> None:
        self._stat_current.hp = value

    @property
    def defense_current(self) -> int:
        return self._stat_current.defense

    @defense_current.setter
    def defense_current(self, value: int) -> None:
        self._stat_current.defense = value

    @property
    def sp_atk_current(self) -> int:
        return self._stat_current.sp_atk

    @sp_atk_current.setter
    def sp_atk_current(self, value: int) -> None:
        self._stat_current.sp_atk = value

    @property
    def sp_def_current(self) -> int:
        return self._stat_current.sp_def

    @sp_def_current.setter
    def sp_def_current(self, value: int) -> None:
        self._stat_current.sp_def = value

    @property
    def speed_current(self) -> int:
        return self._stat_current.speed

    @speed_current.setter
    def speed_current(self, value: int) -> None:
        self._stat_current.speed = value

    # Basic Getter / Setter

    @property
    def id(self) -> int | None:
        """The id property."""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def stat(self) -> Statistic:
        return self.stat

    @property
    def level(self) -> int:
        return self._level

    @property
    def name(self) -> str | None:
        return self._name

    @property
    def common_attacks(self) -> list[AbstractAttack]:
        return self._common_attacks

    @property
    def special_attack(self) -> AbstractAttack | None:
        return self._special_attack
