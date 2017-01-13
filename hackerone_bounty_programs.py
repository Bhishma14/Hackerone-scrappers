
import urllib2
import json


hackerone = "https://hackerone.com/programs/search?query=bounties%3Ayes&sort=name%3Aascending&limit=1000"
opener = urllib2.build_opener()
opener.addheaders = [('Accept','application/json, text/javascript, */*; q=0.01'),('content-type','application/json'),('x-requested-with','XMLHttpRequest')]
response = opener.open(hackerone)
print "Read the response..."
json_string = response.read()
print "Loading json..."
data = json.loads(json_string, encoding='latin-1')

print "Total programs: " + str(data['total'])

programs = data['results']

for program in programs:
	about = program['about']
	disclosure_email = ''

	if 'disclosure_email' in program:
		disclosure_email = program['disclosure_email']

	disclosure_url = ''
	if 'disclosure_url' in program:
		disclosure_url = program['disclosure_url']
	
	handle = program['handle']
	name = program['name']

	offers_rewards = '0'
	if 'offers_rewards' in program:
		offers_rewards = program['offers_rewards']

	offers_thanks = '0'
	if 'offers_thanks' in program:
		offers_thanks = program['offers_thanks']

	stripped_policy = program['stripped_policy']
	url = program['url']
	
	# DO WHAT YOU WANT HERE
