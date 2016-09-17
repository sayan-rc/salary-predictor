import requests
import csv

def is_valid_state_num(num):
    lst = [3, 7, 43]
    return type(num)==type(5) and num not in lst and (num > 0 and num < 57 or num == 72)

def select_state():
    params = {
        'get': 'NAME',
        'for': 'state:*',
        'key': '65574da907a7e319b5fabb998098789b74e2092a'
    }
    data = requests.get("http://api.census.gov/data/2015/acs1", params=params)

    print('Please select your desired state to work in.')
    for state in data.json()[1:]:
        print(state[1], state[0])
    workplace = int(input())
    while not is_valid_state_num(workplace):
        workplace = int(input('Not a valid state input. Please try again.'))
    print('-----------')
	return workplace

def select_field_of_work():
    print('Please select your desired field of work')
    menu = """*** Fields of Work Menu ***
04 - Management occupations
05 - Business and financial operations occupations
07 - Computer and mathematical occupations
08 - Architecture and engineering occupations
09 - Life, physical, and social science occupations
11 - Community and social service occupations
12 - Legal occupations
13 - Education, training, and library occupations
14 - Arts, design, entertainment, sports, and media occupations
16 - Health diagnosing and treating practitioners and other technical occupations
17 - Health technologists and technicians
19 - Healthcare support occupations
21 - Fire fighting and prevention, and other protective service workers including supervisors
22 - Law enforcement workers including supervisors
23 - Food preparation and serving related occupations
24 - Building and grounds cleaning and maintenance occupations
25 - Personal care and service occupations
27 - Sales and related occupations
28 - Office and administrative support occupations
30 - Farming, fishing, and forestry occupations
31 - Construction and extraction occupations
32 - Installation, maintenance, and repair occupations
34 - Production occupations
35 - Transportation occupations
36 - Material moving occupations"""
    field = int(input(menu))
    while type(field)!=type(5) or field < 1 or field > 36:
        print('Not a valid Field of work. Please try again.')
        field = int(input())
    return field
	
def return_average_salary():
	occupation = select_field_of_work()
	state_num = select_state()
	
	census_variables = ['NAME', occupation]
	state = 'state:{}'.format(state_num)

	params = {
		'get': ','.join(census_variables),
		'for': state,
		'key': '65574da907a7e319b5fabb998098789b74e2092a'
	}
	
	data = requests.get("http://api.census.gov/data/2015/acs1", params=params)
	income = []
	for row in data.json()[1:]:
		income.append(float(row[1]))
	print(income)
return_average_salary()
