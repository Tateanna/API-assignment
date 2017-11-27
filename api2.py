import json, requests,csv

output_file = open('api.csv', 'w')
writer = csv.writer(output_file)

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'


def get_votes_by_date(chamber, start_date, end_date):

	url = 'https://api.propublica.org/congress/v1/{chamber}/votes/{start_date}/{end_date}.json'
	response = requests.get(url, headers={'chamber':chamber, 'start_date': start_date, 'end_date': end_date}).content

	data = json.loads(response)

	return data

	def format_nomination_votes(data):
		    
		    output = [['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting']]
	
	for vote in data['results']['votes']: 
    
			date = 'date'

			question = 'question'
			description = 'description'

			result = 'result'

			yes = '{total}:yes'

			no = '{total}:no'

			present = '{total}:present'

			not_voting = '{total}:not_voting'

			output.append([date, question, description, result, yes, no, present, not_voting])
        writer.writerow(data)	
	return output
# API-assignment
