from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.attack.abstract_attack import AbstractAttack
from business_object.statistic import Statistic


class AllRounderPokemon(AbstractPokemon):
    def __init__(
        self,
        id: int | None = None,
        stat_max: Statistic | None = None,
        stat_current: Statistic | None = None,
        level: int = 0,
        name: str | None = None,
        common_attacks: list[AbstractAttack] = [],
    ) -> None:
        special_attack = SpecialFormulaAttack(
            power=80,
            name="Dragon laser",
            description="{pokemon.name} shoots a dark laser."
        )

        # Calling the parent class constructor
        super().__init__(
            id=id,
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            common_attacks=common_attacks,
            special_attack=special_attack,
        )

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
