class Singleton(type):
    """
    -> https://refactoring.guru/fr/design-patterns/singleton
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs): # type: ignore[no-untyped-def]
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in Singleton._instances:
            Singleton._instances[cls] = super().__call__(*args, **kwargs)
        return Singleton._instances[cls]
