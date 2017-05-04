# set up and error check for using the BNO005 sensor 
import logging
import sys
import time
global DEBUG
DEBUG = True

from Adafruit_BNO055 import BNO055  # @UnresolvedImport


#need to enable gpio as input / output and set rst to port 21
#import statment for BNo))5 library
bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)

#-----------------------------------------------------------------------------

# Enable verbose debug logging if -v is passed as a parameter.
#prelim set up to make use of BNO005 sensor
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')


# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

#-----------------------------------------------------------------------------



def robot_cur_bearing():
	
	
	#euler functions return true north heading of robot
	heading, roll, pitch = bno.read_euler()

	
	
	return heading
	
def wrapper_robot_cur_bearing():
	# read from file
	if DEBUG == True:
		
		print("accessing bearing")
		with open("bearings.txt",'r') as myfile:
			
			data = myfile.read()
			
			print(data)
		

