import requests
import json

#TODO:
#Autogenerate API key if one does not exist
#Exception handling
def unshort(url):
    """
    Take a url as string and returned unshorted form using unshort.me API.
    """
    # TODO: get API key
    query_url = 'http://api.unshort.me/unshorten/v2/?r={0}\
                 &format={1}'.format(url, 'json')
    r = requests.get(query_url)
    output_json = json.loads(r.text)
    return output_json['resolvedURL']

