from server.settings import settings

__all__ = ["create_db_connection"]

# DATABASE_URL = ""

DATABASE_CONFIG = {
    "connections": {
        "default": f"{settings.db_schema}://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "server.models"],
            "default_connection": "default",
        },
    },
}
