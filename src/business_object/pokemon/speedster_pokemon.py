from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.attack.abstract_attack import AbstractAttack
from business_object.statistic import Statistic


class SpeedsterPokemon(AbstractPokemon):
    def __init__(
        self,
        id: int | None = None,
        stat_max: Statistic | None = None,
        stat_current: Statistic | None = None,
        level: int = 0,
        name: str | None = None,
        common_attacks: list[AbstractAttack] = [],
    ) -> None:
        special_attack = PhysicalFormulaAttack(
            power=90,
            name="Shadow claw",
            description="{pokemon.name} hits with all the power of the darkness."
        )

        super().__init__(
            id=id,
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            special_attack=special_attack,
            common_attacks=common_attacks,
        )

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.speed_current + self.sp_atk_current) / 200
