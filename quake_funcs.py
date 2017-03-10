from urllib.request import urlopen
from json import loads
from datetime import datetime


# GIVEN FUNCTIONS: Use these two as-is and do not change them
def get_json(url):
   """Function to get a JSON dictionary from a website.

   Args:
      url (str): The url from which to get the JSON

   Returns:
      A Python dictionary containing the information from the JSON object
   """
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)


def time_to_str(time):
   """Converts integer seconds since unix epoch to a string.

   Args:
      time (int): Unix time

   Returns:
      A nicely formated time string
   """
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# TODO: Add Earthquake class definition here
class Earthquake:
   '''You must store each line of data in an object whose type is a class called Earthquake. The Earthquake class should have the following attributes: place (a string), mag (a float), longitude (a float), latitude (a float), and time (an int). Put the definition for this class in your quake_funcs.py module.'''
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   ''' Two earthquakes are equal if (and only if) all of their attributes are equal.'''
   def __eq__(quake_1, quake_2):
      return quake_1.place == quake_2.place and quake_1.mag == quake_2.mag and quake_1.longitude == quake_2.longitude and quake_1.latitude == quake_2.latitude and quake_1.time == quake_2.time

   def __repr__(self):
      return "{:s} {:f} {:f} {:f} {:d})".format(self.place, self.mag, self.longitude, self.latitude, self.time)


''' u are required to write a function read_quakes_from_file(filename) that takes a string filename as input and returns a list of Earthquake objects as output. '''
# TODO: Required function - implement me!
def read_quakes_from_file(filename):
   my_file = open(filename, 'r')
   earthquake_objects = []
   property_list = []
   for line in my_file:
      line = line.strip() # get rid of \n and white spaces on left and right
      property_list = line.split(' ', 4)
      earthquake_obj = Earthquake(str(property_list[4]), float(property_list[0]), float(property_list[1]), float(property_list[2]), int(property_list[3]))
      earthquake_objects.append(earthquake_obj) 
   my_file.close() 
   return earthquake_objects

def sort_quakes(quakes, sort_attribute): # quakes is mutable
   if sort_attribute == 'm' or sort_attribute == 'M': # descending
      quakes.sort(key = lambda q:q.mag, reverse = True)
   elif sort_attribute == 't' or sort_attribute == 'T':
      quakes.sort(key = lambda q:q.time, reverse = True)
   elif sort_attribute == 'l' or sort_attribute == 'L':
      quakes.sort(key = lambda q:q.longitude)
   elif sort_attribute == 'a' or sort_attribute == 'A':
      quakes.sort(key = lambda q:q.latitude)

def filter_quakes(quakes, filter_attribute):
   filtered_quakes = []
   if filter_attribute == 'm' or filter_attribute == 'M':
      low = float(input("Lower bound: "))
      high = float(input("Higher bound: "))
      filtered_quakes = filter_by_mag(quakes, low, high)
   elif filter_attribute == 'p' or filter_attribute == 'P':
      search_string = input("Search for what string? ")
      filtered_quakes = filter_by_place(quakes, search_string)
   return filtered_quakes


def filter_by_mag(quakes, low, high):
   filtered_quakes = []
   for quake in quakes:
      if quake.mag >= low and quake.mag <= high:
         filtered_quakes.append(quake)
   return filtered_quakes



def filter_by_place(quakes, word):
   filtered_quakes = []
   for quake in quakes:      
      if word.upper() in quake.place.upper(): # compare uppercase
         filtered_quakes.append(quake)
   return filtered_quakes



def quake_from_feature(feature):
   ''' takes a feature dictionary as input and returns an Earthquake object as output'''
   place = feature['properties']['place']
   mag = feature['properties']['mag']
   longitude = feature['geometry']['coordinates'][0]
   latitude = feature['geometry']['coordinates'][1]
   time = int(feature['properties']['time'] / 1000)
   quake_obj = Earthquake(place, mag, longitude, latitude, time)
   return quake_obj

'''If the user chooses to quit, then write the earthquake data back out to the “quakes.txt” file to assure the earthquakes are written in the order they were last sorted, and to assure that any new earthquake data is saved. I suggest writing a function to do this. Note that you must write the data to the file in the same format from which it was read.'''
def write_data(quakes):
   out_file = open("quakes.txt", "w")
   for quake in quakes: 
      out_file.write("{:.2f} {:f} {:f} {:d} {:s}\n".format(quake.mag, quake.longitude, quake.latitude, quake.time, quake.place))
   out_file.close()

def quake_check_in_list(quake, quakes):
  return quake in quakes


