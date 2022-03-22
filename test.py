import twitter_stream as tws

# Set up twitter_stream inputs
bearer_token = tws.auth()
headers = tws.create_header(bearer_token)
keyword = 'democrat ukraine'
start_time = '2021-03-01T00:00.000Z'
end_time = '2021-03-31T00:00.000Z'
max_results = 15

url = tws.create_url(keyword, start_time, end_time, max_results)
json_response = tws.connect_to_endpoint(url[0], headers, url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))
