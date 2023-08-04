import pygal
import pygal_maps_world

wm=pygal.maps.world.World()

wm.title='North,central and south america'
wm.add('North America',['ca','mx','us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
