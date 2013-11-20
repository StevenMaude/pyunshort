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
#TODO: Tests
def unshort(url):
    """
    Take a URL as string and returned unshortened form using expandurl API.
    """
    query_url = 'http://expandurl.appspot.com/expand?url={}'.format(url)
    r = requests.get(query_url)

    output_json = json.loads(r.text)

    if output_json['end_url'].startswith('http'):
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
        print "Usage: unshort.py <URL or CSV of URLs with url as header"
        sys.exit(2)

    if input_arg.endswith('csv'):
        with open('unshort.out', 'w') as f:
            for url in get_urls_from_csv(input_arg):
                unshortened_url = unshort(url)
                if unshortened_url.startswith('http'):
                    output = url + ' ' + unshortened_url + '\n'
                else:
                    output = url + '\n'
                f.write(output)

                print url, unshortened_url
    #            time.sleep(1)
    else:
        print "{0} resolves to {1}".format(sys.argv[1],
                                           unshort(sys.argv[1]))

if __name__ == '__main__':
    main()
