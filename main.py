'''
This module generates a map with locations where films were filmed. The user
enters 3 values, which are year, longitute and latitude. The map shows films
of only that year, and the point on the map are the closest ones to the current
location of the user.
'''
import folium
import haversine
# import geopy
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.extra.rate_limiter import RateLimiter
# from geopy.exc import GeocoderUnavailable
from time import  sleep
import doctest

def get_input() -> list:
    '''
    Get the input from user and return a list of 3 values.
    '''
    year = input('Please enter a year you would like to have a map for: ')
    location = input('Please enter your location (format: lat, long),\
 separated by spaces: ')
    values = [year]
    values.extend(location.split())
    return values


def read_file(path: str) -> list:
    r'''
    Read the file with information on films. Return list of lines.
    >>> read_file('locations.list')[0]
    '"#1 Single" (2006)\t\t\t\t\tLos Angeles, California, USA\n'
    '''
    with open(path, 'r', encoding = 'utf-8') as data_lines:
        lines = data_lines.readlines()

    data = []
    for line in lines:
        data.append(line)
    return data


def process_data(data: str) -> list:
    '''
    Process data from file. Form a list, which contains lists with film
    name, year and location.
    >>> process_data('locations.list')[:3]
    [['#1 Single', '2006', 'Los Angeles, California, USA'],\
 ['#1 Single', '2006', 'New York City, New York, USA'],\
 ['#15SecondScare', '2015', 'Coventry, West Midlands, England, UK']]
    '''
    data = read_file('locations_small.list') #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    database = []

    for line in data:
        line_splt = line.split()

        # identify name and year of the film
        for ind, word in enumerate(line_splt):
            if '(' in word:
                try:
                    year = int(word[1:-1])
                    year = word[1:-1]
                    name = ' '.join(line_splt[:ind])[1:-1]
                except ValueError:
                    continue

        # identify location of the film
        place = line.split('\t')[-1]
        if '(' in place:
            place = line.split('\t')[-2]
        
        if '\n' in place:
            place = place[:-1]

        if 'Federal' not in place and 'Highway' not in place:
            database.append([name, year, place])

    return database


def list_to_df(data: str) -> pd.DataFrame:
    '''
    Return a dataframe which contains columns with film name, year and
    location.
    >>> print(list_to_df('locations.list')[:1])
            name  year                      location
    0  #1 Single  2006  Los Angeles, California, USA
    '''
    data = process_data(data)
    df = pd.DataFrame(data)
    df = df.rename(columns={0: 'name', 1: 'year', 2: 'location'})
    # df.to_csv('locations.csv')
    return df


def sort_by_year(values: list) -> pd.DataFrame:
    '''
    Form a database of films filmed in a particular year.
    >>> sort_by_year(['2017'])[:1]
                 name  year                   location
    5  #2WheelzNHeelz  2017  Nashville, Tennessee, USA
    '''
    df = list_to_df('locations_small.list') # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    year = values[0]
    df = df[df['year'] == year]
    return df



def find_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Add all location names as coordinates to new column is df.
    Return modified df.
    >>> find_coordinates(sort_by_year(['2017'])[:2])['coordinates']
    5     (36.1622296, -86.7743531)
    16    (40.7127281, -74.0060152)
    Name: coordinates, dtype: object
    '''
    geolocator = Nominatim(user_agent="main.py")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    df['address'] = df['location'].apply(geocode)
    df['coordinates'] = df['address'].apply(lambda loc: tuple(loc.point)[:2] if loc else None)
    df = df.drop(columns = ['address'])

    return df


def find_distances(values: list, df: pd.DataFrame) -> pd.DataFrame:
    '''
    Add distance between user's location and locations of films to the new
    column in df. Return modified df.

    >>> values = ['2000', '49.83826', '24.02324']
    >>> df = find_coordinates(sort_by_year(['2017']))
    >>> find_distances(values, df)[:2]['distance']
    5     8312.450394
    16    7193.757594
    Name: distance, dtype: float64
    '''
    user_coords = (values[1], values[2])
    film_coords = df['coordinates'].tolist()
    distances = []

    for coord in film_coords:
        if coord != None:
            distance = geodesic(user_coords, coord).km
            distances.append(distance)

    df['distance'] = distances
    return df


def sort_by_distance(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Sort lines in df in ascending order based on distance. Return modified df.

    >>> values = ['2000', '49.83826', '24.02324']
    >>> df = find_distances(values, find_coordinates(sort_by_year(['2017'])))
    >>> sort_by_distance(df)[:3]['distance']
    52     974.139001
    53    1308.213836
    24    1783.764118
    Name: distance, dtype: float64
    '''
    df = df.sort_values(by = ['distance'], kind = 'quicksort')
    return df[:10]


def build_map(user_coords: list, df: pd.DataFrame) -> pd.DataFrame:
    '''
    Build the html map, which consists of 3 layers: labels layer, main layer
    and user's location.
    '''
    pass





# values = ['49.83826', '24.02324']
# df = find_distances(values, find_coordinates(sort_by_year(['2017'])))
# print(sort_by_distance(df))













def main(user_input):
    '''
    Main function that calls other functions and runs the program.
    '''
    pass

# doctest.testmod()

# if __name__ == '__main__':
#     user_input = get_input()
#     main(user_input)
#     print('Map is generating...')
#     sleep(2)
#     print('Please wait...')
#     year = 0
#     print(f'Finished. Please have look at the map {year}_movies_map.html')
