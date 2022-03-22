import requests # For sending GET requests from the API
import os # For saving access tokens and for file management
import json # For dealing with json responses we receive from the API
import pandas as pd
import csv
import time

# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata


bearer_token = os.environ.get("BEARER_TOKEN")

def create_url(keyword, start_date, end_date, max_results = 10):

    #tweet_fields = "tweet.fields=id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source"

    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld

    #ids = "ids=1278747501642657792,1255542774432063488"

    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs

    url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {'query': keyword,

                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (url, query_params)


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "test"
    return r



def connect_to_endpoint(url, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, auth = bearer_oauth, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    #Inputs for the request
    keyword = "xbox lang:en"
    start_time = "2022-03-21T00:00:00Z"
    end_time = "2021-03-17T00:00:00Z"
    max_results = 15
    url = create_url(keyword, start_time,end_time, max_results)
    json_response = connect_to_endpoint(url[0], url[1])
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
