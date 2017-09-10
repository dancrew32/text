import argparse
import json
import requests
import sys
import urllib
import os


try:
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


CLIENT_ID = os.environ['YELP_CLIENT_ID']
CLIENT_SECRET = os.environ['YELP_CLIENT_SECRET']


API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'


def obtain_bearer_token(host, path):
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token


def request(host, path, bearer_token, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {'Authorization': 'Bearer %s' % bearer_token}
    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


def _search(bearer_token, term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'open_now': True,
        'price': '1,2,3',
        'limit': 50,
        'radius': 200
    }
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)


def search(term, location):
    bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)
    response = _search(bearer_token, term, location)
    businesses = response.get('businesses')

    out = []
    for b in businesses:
        rating = b['rating']
        if rating < 2.5:
            continue
        formatted = u'{name} ({rating}/{reviews}) {address}'.format(
            name=b['name'], 
            rating=b['rating'], 
            reviews=b['review_count'], 
            address=' '.join(b['location']['display_address']))
        out.append(formatted)
    return out
