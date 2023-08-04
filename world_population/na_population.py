# to visualise north america population

import pygal
import pygal_maps_world

wm=pygal.maps.world.World()

wm.title=('North america population')
wm.add('North America',{'ca':34126000,'us':309349000, 'mx': 113423000})

wm.render_to_file('na_pop.svg')
