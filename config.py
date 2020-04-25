import os
from dotenv import load_dotenv

load_dotenv()


class config:
    database_url = os.getenv('DATABASE_URL')


class Test:
    database_url_test = os.getenv('DATABASE_URL_TEST')
    token_assistant = os.getenv('TOKEN_ASSISTANT')
    token_director = os.getenv('TOKEN_DIRECTOR')
    token_producer = os.getenv('TOKEN_PRODUCER')


class Auth_config:
    domain = os.getenv('AUTH0_DOMAIN')
    algorithm = os.getenv('ALGORITHMS')
    algorithms = [algorithm]
    audience = os.getenv('API_AUDIENCE')
