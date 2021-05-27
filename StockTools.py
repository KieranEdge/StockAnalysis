"""This script locates the objects for processing stock data"""
# Small script for prototyping new features. Delete upon prod release
import requests


# Setting the pull parameters
#params ={
#    'access_key':APIKey,
#   'symbols': ['MSFT']
#

class StockData:
    """This class contains the tools required to get data from the API"""
    def __init__(self):
        """Initialising the key variables for the class"""
        self.APIKey = 'a0611696c28a1da84a0b196ccdb3e05e'
        self.eodurl = 'http://api.marketstack.com/v1/eod'

    def requestJSON(self, company):
        """This method returns a JSON file given a specific company symbol
        Keyword argument:
        company -- string value of a company e.g. 'AAPL' for Apple inc.

        """
        # Setting the request parameters
        params = {
            'access_key': self.APIKey,
            'symbols': company
        }

        # Requesting the information from the url
        response = requests.request('GET', self.eodurl, params = params)

        # Converting the requested response to a legible JSON file
        self.results = response.json()
