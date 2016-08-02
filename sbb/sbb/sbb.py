"""@package docstring
sbb module

The sbb module interfaces to http://transport.opendata.ch/ and provides
convenient functions to search the transport database.
"""

import json
import requests
import dateutil.parser

def nextConnection(von,bis):
    """
    Returns the time of the next connection
    
    @param von departure station
    @param bis arrival station
    @return string in the form hh:mm signifying the time of the next train leaving the "von" station in direction "bis".

    """
    url = 'http://transport.opendata.ch/v1/connections'
    request = url+'?from={0}&to={1}'.format(von, bis)
    resp = requests.get(request)
    data = json.loads(resp.text)
    mydate= dateutil.parser.parse(data['connections'][0]['from']['departure'])
    return '{0:02d}:{1:02d}'.format(mydate.hour,mydate.minute)
