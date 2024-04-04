from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(config={
    'host': '127.0.0.1',
    'database': 'vts_db',
    'user': 'nobin',
    'password': 'randompassforme'
})


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=[
    "app.auth.piccolo_app",
    "app.movie.piccolo_app",
])
