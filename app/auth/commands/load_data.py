from app.auth.commands._example_data import USERS
from app.auth.tables import AuthUser


async def load_data():
    """
    Load some example data into the database.
    """
    for table_class in [AuthUser]:
        await table_class.delete(force=True)

    [await AuthUser.create_user(username=data["name"], **data) for data in USERS]

    # We need to update the sequence, as we explicitly set the IDs.
    await AuthUser.raw(
        "SELECT setval('auth_user_id_seq', max(id)) FROM auth_user"
    )
