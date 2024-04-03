from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from enum import Enum
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import Date
from piccolo.columns.column_types import Decimal
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.date import DateNow
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table
import decimal


class AuthUser(Table, tablename="auth_user", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class Movie(Table, tablename="movie", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2024-04-03T22:12:03:430568"
VERSION = "1.5.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="app.movie", description=DESCRIPTION
    )

    manager.add_table(
        class_name="Movie", tablename="movie", schema=None, columns=None
    )

    manager.add_table(
        class_name="Rating", tablename="rating", schema=None, columns=None
    )

    manager.add_column(
        table_class_name="Movie",
        tablename="movie",
        column_name="name",
        db_column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 50,
            "default": "",
            "null": True,
            "primary_key": False,
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Movie",
        tablename="movie",
        column_name="genre",
        db_column_name="genre",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 20,
            "default": "",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": Enum(
                "Genre",
                {
                    "action": "Action",
                    "adventure": "Adventure",
                    "animation": "Animation",
                    "biography": "Biography",
                    "comedy": "Comedy",
                    "crime": "Crime",
                    "documentary": "Documentary",
                    "drama": "Drama",
                    "family": "Family",
                    "fantasy": "Fantasy",
                    "film_noir": "Film-Noir",
                    "history": "History",
                    "horror": "Horror",
                    "music": "Music",
                    "musical": "Musical",
                    "mystery": "Mystery",
                    "romance": "Romance",
                    "science_fiction": "Science-Fiction",
                    "sport": "Sport",
                    "superhero": "Superhero",
                    "thriller": "Thriller",
                    "war": "War",
                    "western": "Western",
                },
            ),
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Movie",
        tablename="movie",
        column_name="rating",
        db_column_name="rating",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 8,
            "default": "",
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": Enum(
                "Rating",
                {
                    "g": "G",
                    "pg": "PG",
                    "pg_13": "PG-13",
                    "r": "R",
                    "nc_17": "NC-17",
                },
            ),
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Movie",
        tablename="movie",
        column_name="release_date",
        db_column_name="release_date",
        column_class_name="Date",
        column_class=Date,
        params={
            "default": DateNow(),
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Rating",
        tablename="rating",
        column_name="user_id",
        db_column_name="user_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": AuthUser,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Rating",
        tablename="rating",
        column_name="movie_id",
        db_column_name="movie_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Movie,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Rating",
        tablename="rating",
        column_name="rating",
        db_column_name="rating",
        column_class_name="Decimal",
        column_class=Decimal,
        params={
            "default": decimal.Decimal("0"),
            "digits": (2, 1),
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
