from quake_funcs import *

def main():
   earthquake_objects = read_quakes_from_file("quakes.txt")
   print()
   display_quake_data(earthquake_objects)
   choice = None
   while choice != 'q' and choice != 'Q': # while user hasn't quit
      choice = prompt_options(earthquake_objects)
      
'''ur program should format and output all of the earthquake data to the screen in a table. (See above for sample output.) The magnitude should be printed to 2 decimal places, the "place" of the earthquake in a column of 40 spaces, then the data and time of the earthquake, followed by the longitude and latitude printed to 3 decimal places each.

I give you a function to convert from an integer time to a formatted string displaying the time in local time. Use this function to display the time in your able. The function is called time_to_str and is located in the given quake_funcs.py module.'''
def display_quake_data(earthquake_objects):
   print("Earthquakes:")
   print("------------")
   for quake in earthquake_objects:
       print('({:.2f}) {:>40s} at {:s} ({:8.3f}, {:.3f})'.format(quake.mag, quake.place, time_to_str(quake.time), quake.longitude, quake.latitude))

def prompt_options(earthquake_objects):
   print()
   print("Options:")
   print("  (s)ort")
   print("  (f)ilter")
   print("  (n)ew quakes")
   print("  (q)uit")
   print()
   choice = str(input("Choice: "))
   if choice == 's' or choice == 'S': # sort
      sort_attribute = str(input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? "))
      sort_quakes(earthquake_objects, sort_attribute) # sort quakes 
      print()
      display_quake_data(earthquake_objects)
   elif choice == 'f' or choice == 'F': # filter
      filter_attribute = str(input("Filter by (m)agnitude or (p)lace? "))
      filtered_quakes = filter_quakes(earthquake_objects, filter_attribute)
      print()
      display_quake_data(filtered_quakes) 
   elif choice == 'n' or choice == 'N': # new quakes
      quakes_dict = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
      features_dict = quakes_dict['features']
      new_quakes_found = False
      for feature in features_dict:
         quake = quake_from_feature(feature)
         if quake_check_in_list(quake, earthquake_objects) == False:
            earthquake_objects.append(quake) # append new found quake to sorted/unsorted list
            new_quakes_found = True
      if new_quakes_found:
         print()
         print("New quakes found!!!")
      print()  
      display_quake_data(earthquake_objects)
   elif choice == 'q' or choice == 'Q': # quit
      write_data(earthquake_objects) # write to file
   return choice



if __name__ == "__main__":
   main()
      


