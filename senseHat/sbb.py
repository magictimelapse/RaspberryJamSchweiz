import json
import requests
import dateutil.parser

def nextConnection(von,bis):
    url = 'http://transport.opendata.ch/v1/connections'
    request = url+'?from={0}&to={1}'.format(von, bis)
    resp = requests.get(request)
    data = json.loads(resp.text)
    mydate= dateutil.parser.parse(data['connections'][0]['from']['departure'])
    return '{0}:{1}'.format(mydate.hour,mydate.minute)
