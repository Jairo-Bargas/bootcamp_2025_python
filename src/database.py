import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import text
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class DatabaseManager:
    def __init__(self):
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.host = os.getenv("POSTGRES_HOST", "localhost")
        self.port = os.getenv("POSTGRES_PORT", "5400")
        self.db = os.getenv("POSTGRES_DB", "bootcamp")

        self.connection_string = (
            f"postgresql+asyncpg://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.db}"
        )

        self.engine = None
        self.async_session = None

    async def initialize(self):
        """Inicializar el engine y sessionmaker"""
        self.engine = create_async_engine(
            self.connection_string,
            echo=True,
            future=True,
        )

        self.async_session = async_sessionmaker(self.engine)

    async def get_all_sales(self) -> pd.DataFrame:
        """Obtener todos los registros de la tabla sales"""
        if not self.engine:
            await self.initialize()

        if self.async_session:
            async with self.async_session() as session:
                try:

                    result = await session.execute(text("SELECT * FROM sales"))
                    rows = result.mappings().all()

                    if rows:
                        df = pd.DataFrame(rows)
                        return df
                    else:
                        return pd.DataFrame()

                except Exception as e:
                    print(f"Error while trying to get data from `sales`: {e}")
                    raise
        return pd.DataFrame()

    async def close(self):
        """Cerrar conexiones"""
        if self.engine:
            await self.engine.dispose()


db = DatabaseManager()
