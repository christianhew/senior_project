
#*************************************************************************************************************
# initalization of variables & initilzation of pinss done here 
# import classes 
import os
import time
import sys
from settings import *
from navigation import *



#create a set of tuples 
num_waypoints = 0
waypoint_counter = 0

#need variable to track num waypoints until last waypoint




if __name__ == '__main__':
	print("initalizing globals")
	settings.init_globals()
	
	# prompt the user to enter the a file containing the waypoints
	
	print("Enter a file name, example : waypoint.txt")
	file_name = input("Enter file name:")
	if os.path.exists(file_name):
		try:
			with open(file_name, 'r') as myfile:
				data = myfile.read()
				print(data)
				
			with open(file_name) as f: # mapps lat and long to tuple pair
				mylist = [tuple(map(str, i.split(','))) for i in f]

				print(mylist[0])

			print("Number of waypoints entered:", len(mylist))
			num_waypoints = len(mylist)

			for i in range(0,num_waypoints):
				print(i)
				tmp_lat,tmp_long = mylist[i]

				tmp_long = float(tmp_long)
				tmp_lat = float(tmp_lat)

				if tmp_lat < -90 or tmp_lat > 90:
					print("ERROR: INVALID LATITUDE\nCHECK WAYPOINT FILE")

					break
				if tmp_long < -180 or tmp_long > 180:
					print("ERROR: INVALID LONGITUDE \n CHECK WAYPOINT FILE")
					break
				else:
					compare_heading(tmp_lat,tmp_long)
		except:
			print("ERROR: COULD NOT OPEN FILE\n")
	else:
		print("ERROR: NO SUCH FILE EXISTS")

			#	real_nav(tmp_lat, tmp_long)
    