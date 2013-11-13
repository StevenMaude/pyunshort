#!/usr/bin/env python
# encoding: utf-8

# Copyright 2013 Steven Maude

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import json
import sys
import logging
import time

from csv import DictReader

import requests


#TODO: Exception handling
def unshort(url):
    """
    Take a URL as string and returned unshortened form using unshort.me API.
    """
    try:
        api_key = load_api_key()
        logging.info("Loaded API key: {}".format(api_key))
    except IOError:
    # TODO: create API key
        create_api_key()
        load_api_key()

    query_url = 'http://api.unshort.me/unshorten/v2/?r={0}\
                 &format={1}&api_key={2}'.format(url, 'json', api_key)
    r = requests.get(query_url)
    output_json = json.loads(r.text)
    try:
        return output_json['resolvedURL']
    except KeyError:
        logging.warning("Error resolving URL: {}".format(url))
        return output_json['error']


def load_api_key(api_key_filename='api_key'):
    """
    Load unshort.me API key
    """
    with open(api_key_filename) as api_key_file:
        return api_key_file.read().strip()


def create_api_key():
    """
    Create unshort.me API key
    """
    pass


def store_api_key():
    """
    Store API key to api_key file.
    """
    pass


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
        print "Usage: unshort.py <URL or CSV of URLs with url as header"

    if input_arg.endswith('csv'):
        for url in get_urls_from_csv(input_arg):
            unshortened_url = unshort(url)
            if not unshortened_url.startswith('http'):
                unshortened_url = ""
            print url, unshortened_url
        time.sleep(1)
    else:
        print "{0} resolves to {1}".format(sys.argv[1], unshort(sys.argv[1]))

if __name__ == '__main__':
    main()
