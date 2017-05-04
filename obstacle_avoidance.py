def read_distance():
#GPIO pins for ultra sonic sensor
	TRIG = 20 #trig sends out signal from sensor
	ECHO = 21 #echo recivces signal from sensor
	try:
		#set up pins
		GPIO.setmode(GPIO.BCM)
		GPIOsetup(TRIG, GPIO.OUT)
		GPIO.setup(ECHO, GPIO.IN)
		
		while GPIO.input(ECHO) == 0:
			signaloff = time.time()
			
		while GPIO.input(ECHO) == 1:
			signalon = time.time()
			
			
		timepassed = signalon - signaloff
		distance = timepassed * 17000
		
		return distance
		
		
	except:
		distance = 99
		GPIO.cleanup()
		return distance
		
#wrapper for testing purposes	
def wrapper_read_distance():
	print("inside function wrapper read distance")
	if(DEBUG == True):
		print("in debug mode")
		with open("distance.txt") as f:
			lines = [i.strip() for i in f]
            
      
			
			return lines[randint(0,len(lines)-1)]

				
def check_front():
	try:
		dist = read_distance()
		if dist <= 15:
			reverse()
			turn_left()
			check_front_2()
		else:
			return False
	except:
		print("failed to read distance")
        
#wrapper for testing purposes      
def wrapper_check_front():
    try:
        dist = wrapper_read_distance()
        is_clear = True
        if dist <= 15:
            reverse()
            turn_left()
            wrapper_check_front()
        else:
            return is_clear
    except:
        print("failed to read distance")
		
