import math
from random import randint
import GPIO as GPIO
import settings

global DEBUG
DEBUG = True	
	

	
	
def calculate_distance(robot_lat, robot_long, waypoint_lat, waypoint_long):
	#radius of earth in Km used to calculate distance

	if waypoint_lat > 90 or waypoint_lat < -90:
		print("ERROR: INVALID WAYPOINT")
	if waypoint_long > 180 or waypoint_long < -180:
		print("ERROR: INVALID WAYPOINT")

	else:
		rad = 6372.8
		robot_lat_radians = math.radians(robot_lat)
		waypoint_lat_radians = math.radians(waypoint_lat)
		
		
		diff_lat_radians = math.radians(waypoint_lat - robot_lat)
		diff_long_radians = math.radians(waypoint_long - robot_long)
		
		a = (math.sin(diff_lat_radians/ 2) * math.sin(diff_lat_radians / 2)) + ((math.cos(robot_lat_radians) * math.cos(waypoint_lat_radians)) * (math.sin(diff_long_radians/2) * math.sin(diff_long_radians/2)))
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		d = rad * c
		
		# convert to feet
		return d * 3280.84
	
        
def way_point_bearing(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    

    dLon = lon2 - lon1

	
    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2)- math.sin(lat1) * math.cos(lat2) * math.cos(dLon)
    anss = math.degrees(math.atan2(y, x))
    fnl = ((anss + 360) % 360.00) # normalize
    
    return fnl


def new_location():
	#while robot cur heading != desired bearing
	#call turn 
	print("in ne wlocation")

def turn_amount(radius_diff):
	# previous test show: robot turns 90 degrees in 1 second time interval
	# time interval (.015625) s = 1.40625 degree turn (left / right)
	x = ((radius_diff / 1.40625) * .015625)
	return x

