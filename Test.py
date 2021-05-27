# Small script for prototyping new features. Delete upon prod release
import requests

# Setting the API key and the url for pull requests
APIKey = 'a0611696c28a1da84a0b196ccdb3e05e'
url = 'http://api.marketstack.com/v1/eod'

# Setting the pull parameters
params ={
    'access_key':APIKey,
    'symbols': ['MSFT']
}

# Sending a get request
response = requests.request('GET', url, params = params)
print(response)
print(type(response.json()))
