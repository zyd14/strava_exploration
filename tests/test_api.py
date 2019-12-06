from src.explore import StravaClientHandler
from src.config import CONFIG

import requests

def test_er():
    client = StravaClientHandler()

    client.get_athlete()
    #client.get_auth_scope()
    pass

def test1():

    response = requests.get(f'https://www.strava.com/oauth/authorize?client_id={CONFIG["CLIENT_ID"]}&redirect_uri={CONFIG["CALLBACK"]}&response_type=code&scope=read')
    assert response

def test_get_athletes():

    client = StravaClientHandler()
    client.get_athlete(CONFIG['ATHLETE_ID'])