from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.attack.abstract_attack import AbstractAttack
from business_object.statistic import Statistic


class AttackerPokemon(AbstractPokemon):
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
            power=60,
            name="Flying Strike",
            description="{pokemon.name} dives to it's prey from the sky."
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
        return 1 + (self.speed_current + self.attack_current) / 200
