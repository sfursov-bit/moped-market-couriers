from __future__ import annotations

from db.base import Base
from db.session import engine

from models import models


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def main() -> None:
    init_db()
    print("Таблицы успешно созданы в PostgreSQL")


if __name__ == "__main__":
    main()

