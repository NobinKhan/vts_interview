from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from app.movie.tables import Movie


ID = "2024-04-02T13:50:37:816635"
VERSION = "1.5.0"
DESCRIPTION = "Create Unique Constraints on Movie Table"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="movie", description=DESCRIPTION
    )

    async def run():
        print(f"running {ID}\n{DESCRIPTION}\n")
        # await Movie.raw("ALTER TABLE rating ADD CONSTRAINT unique_rating UNIQUE (user_id, movie_id);")
        await Movie.raw("ALTER TABLE rating ADD CONSTRAINT movie_unique_rating_constraints UNIQUE (user_id, movie_id);")

    manager.add_raw(run)

    async def run_backwards():
        await Movie.raw("ALTER TABLE rating DROP CONSTRAINT movie_unique_rating_constraints;")

    manager.add_raw_backwards(run_backwards)
    return manager
