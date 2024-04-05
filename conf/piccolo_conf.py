from os import environ
from dotenv import load_dotenv
from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


load_dotenv(".env")

DB = PostgresEngine(
    config={
        "host": environ.get("POSTGRES_HOST", "localhost"),
        "database": environ.get("POSTGRES_DB", "postgres"),
        "user": environ.get("POSTGRES_USER", "postgres"),
        "password": environ.get("POSTGRES_PASSWORD", "postgres"),
    },
)


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(
    apps=[
        "app.auth.piccolo_app",
        "app.movie.piccolo_app",
    ],
)
