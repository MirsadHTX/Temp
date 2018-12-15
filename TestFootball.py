import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
for x in range(5,20):
#x = 44
    stringInfo1 = '/v2/players/'
    stringInfo2 = str(x)
    stringInfo = stringInfo1 + stringInfo2
    headers = { 'X-Auth-Token': '71028256f3694543bd830eb21f470dfc' }
    connection.request('GET', stringInfo, None, headers )
    response = json.loads(connection.getresponse().read().decode())

    print(json.dumps(response["name"], indent=2))

#print (response)