from __future__ import print_function  

from faceit_api import PlayersApi, ApiClient
import faceit_api
from faceit_api.rest import ApiException
from pprint import pprint


FACEIT_API_KEY = 'switch_to_created_key_in_app' #change

configuration = faceit_api.Configuration()
configuration.api_key['Authorization'] = FACEIT_API_KEY
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_client = faceit_api.ApiClient(configuration)
matches_api = faceit_api.MatchesApi(api_client)
players_api = faceit_api.PlayersApi(api_client)  

player_id = "switch_to_finding_id" #change
player_info = players_api.get_player(player_id)

print(player_info)
