from calculations import *
from motor import *
# global variables for robot constant change in long and latitude

global robot_long
global robot_lat
global DEBUG
DEBUG = True
#***********************************************************************************************************
#minium distance constant(in meters) robot can be from waypoint
global min_waypoint_dist 
min_waypoint_dist= 1.5;



#read from Gps and assign current long**********************************************************************  NEED TO CREATE 2 NEW FUNCTIONS +get_current_gps_lat/ get_current_gps_long
#ro call robot current location use  gpsd.fix.longitude / gpsd.fix.latitude
robot_long = gpsd.fix.longitude;     
class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd
		gpsd = gps(mode=WATCH_ENABLE)
		self.current_value=None
		self.running = True
		
	def run(self):
		global gpsd
		while gpsp.running:
			gpsd.next()
#***********************************************************************************************************
# need to start compass thread so that the program can continually read compas and compare for the turning

#supplementary file to allow for further testing of compare heading
def wrapper_robot_cur_location():
	print("inside function wrapper robot bearing\n")
	if(DEBUG == True):
		print("in debug mode\n")
		with open("robot_current_location.txt") as f:
			lines = [i.strip() for i in f]
			
			return lines[randint(0,len(lines)-1)]


			
#**********************************************************************************
#reading from file to testing functionality 
def compare_heading(waypoint_latitude, waypoint_longitude):
    waypoint_latitude = float(waypoint_latitude)
    waypoint_longitude = float(waypoint_longitude)


    print("inside real navigation driver\n")
    #check if robot is already at waypoint
    with open("robot_start_location.txt") as f:
            mylist = [tuple(map(float, i.split(','))) for i in f]
            num = len(mylist)
            x,y = mylist[randint(0,len(mylist)-1)]# chooses a random starting location from text file
            print("robot starting lat", x)# latitude of starting robot position
            print("robot_starting_long",y)# longitude of starting robot position
    
    dist_from_wp = calculate_distance(x,y,waypoint_latitude,waypoint_longitude)
    if dist_from_wp >= 1.5: # within 1.5 feet of target
    
        current = 0
        target = 0
        #get the current = gps facing of the robot, which will be random for testing purposes
        with open("robot_bearing.txt") as f:
            lines = [i.strip() for i in f]
            current = lines[randint(0,len(lines)-1)]
            print("current:",current)
            


            
        while dist_from_wp >= min_waypoint_dist:
            
            target = way_point_bearing(x, y,waypoint_latitude, waypoint_longitude)
            target = round(target)
            print("target:",target)
            diff = target - int(current)
            diff = round(diff)
            print("diff :",diff)

            absolute_diff = abs(diff)
            print("absolute diff:",absolute_diff)
            

            if diff < 0:
                diff += 360
                print(diff)
            if diff >= 180:
                print("turn left")
                #implement check front
                check_front()

                turn_left()
              
                print(dist_from_wp)
            elif diff == 0:
                print("go forward")
                check_front()
                forward()
                #need to implement check front for each 
                print(dist_from_wp)
                #update distance from waypoint so that it knows to continue loop
                #read from gps for new robot location
                x = gpsd.fix.latitude
                y = gpsd.fix.longitude
                #update distance
                calculate_distance(x,y,waypoint_latitude,waypoint_longitude)

            else:
                print("turn right")
                #implement check front
                check_front()
                turn_right()
                print(dist_from_wp)
            
    else:
        print("already at waypoint")
    
