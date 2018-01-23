#shodan for git
import shodan
import sys

# Configuration
API_KEY = "UR API key here" #need shodan IP key

api = shodan.Shodan(API_KEY)

host = api.host('206.132.22.43')
print('IP address:', host['ip_str'])
print('Country:', host['country_code3'] )
print('Ports: ', host['ports'])
print('Organization:', host.get('org', 'n/a'))
print('OS:', host.get('os', 'n/a'))
for item in host['data']:
    print (item['data'])
