from tortoise.contrib.fastapi import register_tortoise

from db.config import DATABASE_CONFIG

__all__ = ["connect_to_db"]

def connect_to_db(app) -> None:
    register_tortoise(app, config=DATABASE_CONFIG)