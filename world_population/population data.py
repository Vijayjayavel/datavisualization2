import json

from country_code import get_country_code
filename='population_data.json'

with open(filename) as f:
    pop_data=json.load(f)

    for pop_dict in pop_data:
        if pop_dict['Year']=='2010':
            population = int(float(pop_dict['Value']))
            country_name=pop_dict['Country Name']

            code=get_country_code(country_name)
            if code:
                print(country_name + ':' + str(population))
            else:
                print('ERROR: '+country_name)