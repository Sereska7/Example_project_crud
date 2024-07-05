from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

from core.config import settings


if settings.MODE == "TEST":
    url_db = settings.TEST_DB_URL
    
else:
    url_db = settings.DB_URL


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(
    url=url_db,
    echo=settings.db_echo,
)
