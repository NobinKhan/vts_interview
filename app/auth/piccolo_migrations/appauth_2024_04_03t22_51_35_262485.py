from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Varchar


ID = "2024-04-03T22:51:35:262485"
VERSION = "1.5.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID,
        app_name="app.auth",
        description=DESCRIPTION,
    )

    manager.alter_column(
        table_class_name="AuthUser",
        tablename="auth_user",
        column_name="name",
        db_column_name="name",
        params={"unique": False},
        old_params={"unique": True},
        column_class=Varchar,
        old_column_class=Varchar,
        schema=None,
    )

    return manager
