import csv

from country_code import get_country_code

import pygal
import pygal_maps_world

from datetime import datetime

import matplotlib.pyplot as plt

filename='world_bank_data.csv'

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)

    """for index,column in enumerate(header_row):
        print(index,column)""" # to find headers of column

    countries=[]
    forest_covers=[]

    cc_forest={}
    for row in reader:
        country=row[0]
        countries.append(country)

        forest_cover=row[64]
        code = get_country_code(country)
        if len(forest_cover)>1:
            forest_covers.append(round(float(forest_cover)))
            cc_forest[code] = round(float(forest_cover))
        else:
            forest_covers.append(0)
            cc_forest[code] = 0

print(cc_forest)
wm=pygal.maps.world.World()

wm.title='World countires '
wm.add('2020 forest cover',cc_forest)

wm.render_to_file('forest_cover2020.svg')