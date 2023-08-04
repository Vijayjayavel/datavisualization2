import json
import pygal
import pygal_maps_world
from country_code import get_country_code

filename='GDP.json'

with open(filename) as f:
    gdp_data=json.load(f)

    cc_gdp={}
    for data in gdp_data:
       if data["Year"]=="2014":
           country=data['Country Name']

           code=data['Country Code']
           gdp=data['Value']
           code = get_country_code(country)
           if code:
            cc_gdp[code]=int(float(gdp))
print(cc_gdp)
wm=pygal.maps.world.World()

wm.title='World gdp'
wm.add('2014',cc_gdp)

wm.render_to_file('Gdp_2014.svg')
           
