import os

PGSQL_DB = os.environ.get('PGSQL_DB', 'annamae')
PGSQL_HOST = os.environ.get('PGSQL_HOST', 'localhost')
PGSQL_PASS = os.environ.get('PGSQL_PASS', 'annamae')
PGSQL_PORT = os.environ.get('PGSQL_PORT', '5432')
PGSQL_USR = os.environ.get('PGSQL_USR', 'annamae')

EMAIL_PASS = os.environ.get('EMAIL_PASS', None)

# openssl rand -hex 32
SECRET_KEY = '4d3dd578d2c2cacc4505eff68e205136b1dc2cd7d939038ae96cbbee9fa42003'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


DESCRIPTION = """Fairy Chess TFT Tournament and Statistics<br>
    <b>** To test the API using the swagger query the endpoint: `/swagger`.</b>"""
