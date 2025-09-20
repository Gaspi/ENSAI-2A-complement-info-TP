class Statistic:
    """
    Inventory all the game statistics
    """
    __hp: int
    __attack: int
    __defense: int
    __sp_atk: int
    __sp_def: int
    __speed: int

    def __init__(self,
                 hp: int = 0,
                 attack: int = 0,
                 defense: int = 0,
                 sp_atk: int = 0,
                 sp_def: int = 0,
                 speed: int = 0) -> None:
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__sp_atk = sp_atk
        self.__sp_def = sp_def
        self.__speed = speed

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        self.__hp = value

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, value: int) -> None:
        self.__attack = value

    @property
    def defense(self) -> int:
        return self.__defense

    @defense.setter
    def defense(self, value: int) -> None:
        self.__defense = value

    @property
    def sp_atk(self) -> int:
        return self.__sp_atk

    @sp_atk.setter
    def sp_atk(self, value: int) -> None:
        self.__sp_atk = value

    @property
    def sp_def(self) -> int:
        return self.__sp_def

    @sp_def.setter
    def sp_def(self, value: int) -> None:
        self.__sp_def = value

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        self.__speed = value
