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

