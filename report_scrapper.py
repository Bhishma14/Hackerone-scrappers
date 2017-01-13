
import urllib2
import json
import time

def open_url(page):
	time.sleep(2) # sometimes hackerone block us
	hackerone = "https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=" + str(page)
	opener = urllib2.build_opener()
	opener.addheaders = [('Accept','application/json, text/javascript, */*; q=0.01'),('content-type','application/json'),
	('authority','hackerone.com'),('x-requested-with','XMLHttpRequest')]
	response = opener.open(hackerone,  timeout=60)
	json_string = response.read()
	return json.loads(json_string, 'utf-8')


data = open_url(1)

pages = data['pages']
total_reports = data['count']

print str(total_reports)  + " reports disclosed\n"

for i in range(1, pages):
	data = open_url (i)	
	reports = data['reports']
	for report in reports:
		report_id = report['id']
		bounty_amount = "$0.0"
		title = report['title']

		if 'formatted_bounty' in report:
			bounty_amount = report['formatted_bounty']

		bounty_program = report['team']['handle']
		report_url = report['url']
		reporter = 'unknown'
		if 'reporter' in report:
			reporter = report['reporter']['username']

		print "Report id: " + str(report_id) + ", url: " + report_url + ", title: " + title.encode('utf-8', 'replace') + ", bounty: " + bounty_amount + ", reporter: " + reporter.encode('utf-8', 'replace') 
