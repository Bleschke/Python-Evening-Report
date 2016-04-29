from urllib2 import urlopen
import json
import time
import urllib2
import os
import pyvona


v = pyvona.create_voice('Access Key', 'Secret Key')
v.region = 'us-east'
v.voice_name = 'Salli'

req = urlopen('http://api.wunderground.com/api/API KEY/forecast/q/STATE/CITY.json')
parsed_json = json.load(req)
fcttext = str(parsed_json['forecast']['txt_forecast']['forecastday'][1]['fcttext'])

# The morning weather report!

cmd_string = 'mpg123 -q /home/pi/WeatherAlerts/Notify.mp3'
os.system(cmd_string)
v.speak('Good Evening! Tonights weather report is:')
v.speak(fcttext)


# Give Internet Security Threat Level.


for line in urllib2.urlopen("http://isc.sans.edu/infocon.txt"):
	v.speak('Internet Threat Level:')
   	if line == 'green':
		v.speak('Green. No significant new threats.')
  	elif line == 'yellow':
		v.speak('Yellow. Significant new threats! Local impact: probable.')
   	elif line == 'orange':
		v.speak('Orange. Major threats and disruption in connectivity.')
   	elif line == 'red':
		v.speak('Red. Serious Threats and Loss of connection across internet.')
  	else:
		v.speak('Error: unable to find threat level.')

# Get Current Bitcoin Value from Coinbase API.

coinbase_api = urllib2.urlopen('https://coinbase.com/api/v1/prices/buy')
response = coinbase_api.read()
response_dictionary = json.loads(response)
print response_dictionary['amount']
#print response_dictionary['subtotal']['amount']
v.speak('Current Value:')
v.speak(response_dictionary['amount'])

