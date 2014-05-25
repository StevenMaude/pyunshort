#!/usr/bin/env python
# encoding: utf-8
import codecs
import json
import sys
import logging

from csv import DictReader

import requests
from dshelpers import request_url


#TODO: Exception handling
#TODO: Tests
def unshort(url):
    """
    Take a URL as string and returned unshortened form using expandurl API.
    """
    query_url = 'http://expandurl.appspot.com/expand?url={}'.format(url)
    r = request_url(query_url)

    output_json = json.loads(r.text)

    end_url = output_json['end_url']
    if end_url.startswith('http') or end_url.startswith('https'):
        return output_json['end_url']
    # for examples, where "end_url": "/Homepage.aspx",
    # "urls": ["http://t.co/l638KnZ1Zb", "http://starcb.com", "/Homepage.aspx"]
    else:
        return output_json['urls'][-2]


def get_urls_from_csv(csv_filename):
    """
    Yield a list of URLs from csv
    """
    with open(csv_filename, 'r') as csv:
        for row in DictReader(csv):
            yield row['url']


def main():
    try:
        input_arg = sys.argv[1]
    except IndexError:
        print "Usage: unshort.py <URL or CSV of URLs with url as header>"
        print "CSV must have .csv filename."
        sys.exit(2)

    if input_arg.endswith('csv'):
        with codecs.open('unshort.out', 'w', 'utf-8') as f:
            for url in get_urls_from_csv(input_arg):
                unshortened_url = unshort(url)
                if unshortened_url.startswith('http'):
                    output = url + ' ' + unshortened_url + '\n'
                else:
                    output = url + '\n'
                f.write(output)

                print url, unshortened_url
    else:
        print "{0} resolves to {1}".format(sys.argv[1],
                                           unshort(sys.argv[1]))

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main()
