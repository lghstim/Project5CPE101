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
      line = line.rstrip('\n')
      property_list = line.split(' ', 4)
      earthquake_obj = Earthquake(str(property_list[4]), float(property_list[0]), float(property_list[1]), float(property_list[2]), int(property_list[3]))
      earthquake_objects.append(earthquake_obj) 
   my_file.close()
      
   return earthquake_objects

# TODO: Required function - implement me!
def filter_by_mag(quakes, low, high):
   pass


# TODO: Required function - implement me!
def filter_by_place(quakes, word):
   pass


# TODO: Required function for final part - implement me too!
def quake_from_feature(feature):
   pass



