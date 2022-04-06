from sqlalchemy import create_engine # Creates the engine that connects to the database.
from sqlalchemy_utils import database_exists, create_database # To verify a database exists or else create it.

engine = create_engine("mysql+pymysql://root@localhost:3306/db_new")

if not database_exists(engine.url):
    create_database(engine.url)


