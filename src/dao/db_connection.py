import os
import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection

from utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    Technical class to open only one connection to the DB.
    """
    __connection: connection

    def __init__(self) -> None:
        dotenv.load_dotenv(override=True)
        # Open the connection.
        self.__connection = psycopg2.connect(
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
            database=os.environ["POSTGRES_DATABASE"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
        )

    @property
    def connection(self) -> connection:
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection

    def cursor(self) -> RealDictCursor:
        return self.connection.cursor(cursor_factory=RealDictCursor)
