import os

import requests
import pandas as pd

from stravalib import Client

from src.config import CONFIG

class StravaClientHandler:

    def __init__(self):
        self.connect_to_strava()

    def reset_client(self, access_token: str = None) -> Client:
        if not access_token:
            access_token = CONFIG['ACCESS_TOKEN']
        return Client(access_token=access_token)

    def connect_to_strava(self):
        strava_client = Client()

        if os.getenv('DEPLOYMENT_STAGE', 'dev'):
            redirect_url = 'http://127.0.0.1:5000/authorization'
        else:
            redirect_url = CONFIG['WEBSITE']

        strava_client.authorization_url(client_id=CONFIG['CLIENT_ID'],
                                              redirect_uri=redirect_url)
    def get_athlete(self):
        client = self.reset_client()
        return client.get_athlete()



class NoMoreAttributes(Exception):

    def __init__(self, error_msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_msg = error_msg

def get_access():
    url = 'https://www.strava.com.oath/authorize'
    client_id = CONFIG['CLIENT_ID']
    client_secret = CONFIG['CLIENT_SECRET']

def authorizer():
    url = "https://strava.com/oauth/authorize"

def get_access():
    url = 'https://www.strava.com.oath/authorize'
    client_id = CONFIG['CLIENT_ID']
    client_secret = CONFIG['CLIENT_SECRET']
    final_url =f'{url}?client_id={client_id}?client_secret={client_secret}&code=acitivity:read&grant_type=authorization_code&scope=activity:read'
    return requests.get(final_url, headers={'Authorization': f'Bearer ${ACCESS_TOKEN}'})

def get_local_access():
    url = 'https://www.strava.com.oath/authorize'
    client_id = CONFIG['CLIENT_ID']
    client_secret = CONFIG['CLIENT_SECRET']
    final_url = f'{url}?client_id={client_id}?client_secret={client_secret}&code=acitivity:read&scope=activity:read&approval_prompt=auto&response_type=code&redirect_url='
    return requests.get(final_url, headers={f'Authorization': 'Bearer #{ACCESS_TOKEN}'})

def get_activities() -> pd.DataFrame:
    fields = ['id', 'type']
    activities = pd.DataFrame(columns=fields)

    page = 1
    while True:
        activities = retrieve_paginated_activies(activities, page)

        page +=1
    return activities

def retrieve_paginated_activies(activities: pd.DataFrame, page: int) -> pd.DataFrame:
    url = f'{ACTIVITIES_URL}?access_token={ACCESS_TOKEN}&per_page=50&page={str(page)}'
    response = requests.get(url)
    data = response.json()
    if not data:
        raise NoMoreAttributes('No more attributes found for this request')

    for i in range(len(data)):
        activities.loc[i + (page - 1) * 50, 'id'] = data[i]['id']
        activities.loc[i + (page - 1) * 50, 'type'] = data[i]['id']

    return activities

if __name__ == '__main__':
    print(get_access())