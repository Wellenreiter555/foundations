from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            
                return resp.content
            

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'http://www.fabpedigree.com/james/greatmm.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

def convert(response):

    try:
        tup_json = json.loads(response.decode('utf-8'))
        return tup_json
    except ValueError:
        logger.error(error)
        return None



def get_hits_on_name(mathematician):

    name = mathematician.split()
    name = "_".join(name)

    url_root = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/{}/daily/20180101/20181231"
    response = simple_get(url_root.format(name))


    data = convert(response)

    if data is not None:

        index = 0 
        total_views = 0


        for views in data:
            try:
                views = data["items"][index]["views"]
                index += 1
                total_views += views
            except KeyError:
                return None
        average_views = total_views / (index)
        print("{} checked".format(name))
        return int(average_views)










mathematician_list = get_names()
popularity = {}


for mathematician in mathematician_list:

    average_views = get_hits_on_name(mathematician)

    if average_views == None:
        continue
    else:
        popularity.update( {mathematician: average_views} )

ranking = sorted(popularity.items(), key = lambda x: x[1], reverse=True)

index = 0

for mathematician in ranking:
    index += 1
    print("{}: {} with {} average views in 2018".format(index, mathematician[0], mathematician[1]))























