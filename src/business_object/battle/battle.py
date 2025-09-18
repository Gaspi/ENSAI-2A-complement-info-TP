from business_object.battle.round import Round
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class Battle:
    def __init__(
        self, first_monstie: AbstractPokemon, second_monstie: AbstractPokemon
    ) -> None:
        self.__first_monstie: AbstractPokemon = first_monstie
        self.__second_monstie: AbstractPokemon = second_monstie
        self.__rounds: list[Round] = []
        self.__winner: AbstractPokemon | None = None
        self.__final_phrase: str = ""

    def add_round(
        self,
        attacker: AbstractPokemon,
        defender: AbstractPokemon,
        dealt_damage: int,
        attack_description: str
    ) -> None:
        self.__rounds.append(
            Round(
                attacker=attacker,
                defender=defender,
                dealt_damage=dealt_damage,
                attack_description=attack_description,
            )
        )

    def __str__(self) -> str:
        res = f"Battle between {self.first_monstie.name} and {self.second_monstie.name}\n"
        for round_number, round in enumerate(self.rounds):
            res += f"Round {round_number} : {round}\n"
        if self.winner is not None:
            res += f"Winner : {self.winner.name}"
        return res

    @property
    def first_monstie(self) -> AbstractPokemon:
        return self.__first_monstie

    @property
    def second_monstie(self) -> AbstractPokemon:
        return self.__second_monstie

    @property
    def rounds(self) -> list[Round]:
        return self.__rounds

    @property
    def winner(self) -> AbstractPokemon | None:
        return self.__winner

    @winner.setter
    def winner(self, value: AbstractPokemon):
        self.__winner = value

    @property
    def final_phrase(self) -> str:
        return self.__final_phrase

    @final_phrase.setter
    def final_phrase(self, value: str):
        self.__final_phrase = value
