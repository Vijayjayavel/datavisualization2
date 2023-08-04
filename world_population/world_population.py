import json
import pygal
import pygal_maps_world
from country_code import get_country_code

filename='population_data.json'

with open(filename) as f:
    pop_data=json.load(f)

    cc_pop={}
    for pop_dict in pop_data:
        if pop_dict['Year']=='2010':
            population = int(float(pop_dict['Value']))
            country_name=pop_dict['Country Name']

            code=get_country_code(country_name)
            if code:
                cc_pop[code]=population

wm=pygal.maps.world.World()

wm.title='World population in 2010,by country'
wm.add('2010',cc_pop)

wm.render_to_file('world_population.svg')






