from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.attack.physical_attack import PhysicalFormulaAttack
import random
from services.battle_service import BattleService
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from unittest.mock import patch
from business_object.statistic import Statistic
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from unittest import TestCase


class TestBattleService(TestCase):
    def test_resolve_battle(self) -> None:
        # GIVEN
        pikachu = AttackerPokemon(
            level=10,
            stat_current=Statistic(
                hp=100, attack=50, sp_atk=50, defense=50, sp_def=50, speed=50
            ),
            name="pikachu",
            common_attacks=[
                SpecialFormulaAttack(
                    power=30,
                    description="{pokemon.name} fait tomber la foudre sur son adversaire",
                    name="Tonnerre",
                )
            ],
        )

        snorlax = DefenderPokemon(
            level=10,
            stat_current=Statistic(
                hp=100, attack=10, sp_atk=10, defense=10, sp_def=10, speed=10
            ),
            name="Snorlax",
            common_attacks=[
                PhysicalFormulaAttack(
                    power=30,
                    description="{pokemon.name} plaque le pokemon au sol",
                    name="body_slam",
                )
            ],
        )

        # WHEN
        battle_service = BattleService()
        combat = battle_service.resolve_battle(monstie_1=pikachu, monstie_2=snorlax)

        # THEN
        self.assertEqual(pikachu, combat.winner)
        self.assertIsNotNone(combat.rounds)
        self.assertEqual(0, snorlax.hp_current)

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_get_order_no_draw(self) -> None:
        # GIVEN
        speed_pikachu = 50
        speed_charizard = 40
        pikachu = AbstractPokemon(stat_current=Statistic(speed=speed_pikachu)) # type: ignore[abstract]
        charizard = AbstractPokemon(stat_current=Statistic(speed=speed_charizard)) # type: ignore[abstract]

        battle_service = BattleService()
        random.seed(1)  # les deux nombres générés seront 8 et 46

        # WHEN
        first, second = battle_service.get_order(pikachu, charizard)

        # THEN
        self.assertEqual(charizard, first)
        self.assertEqual(pikachu, second)

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_get_order_draw(self) -> None:
        # GIVEN
        speed_pikachu = 50
        speed_charizard = 22
        pikachu = AbstractPokemon(stat_current=Statistic(speed=speed_pikachu)) # type: ignore[abstract]
        charizard = AbstractPokemon(stat_current=Statistic(speed=speed_charizard)) # type: ignore[abstract]

        battle_service = BattleService()
        # les deux nombres générés seront 8 et 36 (draw), 48 and 4
        random.seed(1)

        # WHEN
        first, second = battle_service.get_order(pikachu, charizard)

        # THEN
        self.assertEqual(pikachu, first)
        self.assertEqual(charizard, second)

    def test_choose_attack_1(self) -> None:
        # GIVEN
        tonnerre = SpecialFormulaAttack(
            power=30,
            description="{pokemon.name} fait tomber la foudre sur son adversaire",
            name="Tonnerre",
        )
        vive_attaque = PhysicalFormulaAttack(
            power=35,
            description="{pokemon.name} fonce sur l'ennemi si rapidement qu'on parvient à peine à le discerner.",
            name="Vive attaque",
        )
        pikachu = AttackerPokemon(
            name="pikachu", common_attacks=[tonnerre, vive_attaque]
        )
        battle_service = BattleService()
        random.seed(1)  # no crit, choose tonnerre

        # WHEN
        choosen_attack = battle_service.choose_attack(pikachu)

        # THEN
        self.assertEqual(tonnerre, choosen_attack)

    def test_choose_attack_special_attack(self) -> None:
        # GIVEN
        tonnerre = SpecialFormulaAttack(
            power=30,
            description="{pokemon.name} fait tomber la foudre sur son adversaire",
            name="Tonnerre",
        )
        vive_attaque = PhysicalFormulaAttack(
            power=35,
            description="{pokemon.name} fonce sur l'ennemi si rapidement qu'on parvient à peine à le discerner.",
            name="Vive attaque",
        )
        pikachu = AttackerPokemon(
            name="pikachu", common_attacks=[tonnerre, vive_attaque]
        )
        battle_service = BattleService()
        random.seed(2)  # crit

        # WHEN
        choosen_attack = battle_service.choose_attack(pikachu)

        # THEN
        self.assertEqual(pikachu.special_attack, choosen_attack)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
