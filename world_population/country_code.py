import pygal
import pygal_maps_world

COUNTRIES=pygal.maps.world.COUNTRIES

# missing_coun=['Antigua and Barbuda', 'Aruba', 'Bahamas, The', 'Barbados', 'Bermuda', 'Bolivia',
#               'Cayman Islands', 'Channel Islands', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.',
#               'Curacao', 'Dominica', 'Egypt, Arab Rep.', 'Faeroe Islands', 'Fiji', 'French Polynesia',
#               'Gambia, The', 'Gibraltar', 'Grenada', 'Hong Kong SAR, China', 'Iran, Islamic Rep.',
#               'Isle of Man', 'Kiribati', 'Korea, Dem. Rep.', 'Korea, Rep.', 'Kosovo', 'Kyrgyz Republic',
#               'Lao PDR', 'Libya', 'Macao SAR, China', 'Macedonia, FYR', 'Marshall Islands', 'Micronesia,'
#               ' Fed. Sts.', 'Moldova', 'New Caledonia', 'Northern Mariana Islands', 'Palau', 'Qatar', 'Samoa',
#               'Sint Maarten (Dutch part)', 'Slovak Republic', 'Solomon Islands', 'St. Kitts and Nevis',
#               'St. Lucia', 'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Tanzania',
#               'Tonga', 'Trinidad and Tobago', 'Turks and Caicos Islands', 'Tuvalu', 'Vanuatu', 'Venezuela,'
#               ' RB', 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza', 'Yemen, Rep.'] # these are missing country while finding country code
def get_country_code(country_name):

    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    return None


