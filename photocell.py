import RPi.GPIO as GPIO, time, sys

GPIO.setmode(GPIO.BOARD)
dc = raw_input("Hit enter to start!")
numBit = 120
threshhold = 0.35
#RCtime = recharge time for capacitor
def RCtime(RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.02)
	start = time.time()
	GPIO.setup(RCpin, GPIO.IN)
	while(GPIO.input(RCpin) == GPIO.LOW):
		pass
	end =time.time()
	#print (end-start) * 1000 
	return (end-start) * 1000

def getLetter (arg):
	#Translates back 4 bits into letter equivalent
	switcher = {
		"0001" : "B",
		"0010" : "A",
		"0011" : "C",
		"0100" : "O",
		"0101" : "N",
		"0110" : "I",
		"0111" : "T",
		"1000" : "S",
		"1001" : " ",
	}
	return switcher.get(arg, "error")

while(1):
	rcTotal = 0
	rcCount = 0
	rcRead = 0
	bit = 0
	bitCount = 0
	list = []
	finalist = ""
	index = 0
	if(RCtime(22) < threshhold):
		time.sleep(0.01)
		rcRead = RCtime(22)
		for x in range(0,numBit):
			#Begins reading capacitor values and
			#seperates them based on threshhold
			if(rcRead > threshhold):
				#Reads until low ->high, or High ->Low, or 5 values read
				while(rcRead >= threshhold and rcCount < 5):
					rcCount = rcCount + 1
					rcTotal += rcRead
					rcRead = RCtime(22)
				#print (rcTotal / rcCount)
				bit = rcTotal/rcCount
				rcCount = 0
				rcTotal = 0
			else:
				while(rcRead < threshhold and rcCount < 5):
					rcCount = rcCount + 1
					rcTotal += rcRead
					rcRead = RCtime(22)
				#print (rcTotal / rcCount)
				bit = rcTotal/rcCount
				rcCount = 0
				rcTotal = 0
			#Determines transmitted bit based on avg
			if(bit < threshhold):
				bit = 1	
			else:
				bit = 0
			bitCount = bitCount + 1
			if(bitCount > 2):
				print bit
				list.append(bit)
		print len(list)
		for x in range(0,numBit/4-1):
			s = str(list[index]) + str(list[index+1]) + str(list[index+2]) + str(list[index+3])
			finalist += (getLetter(s))
			index = index + 4
		print finalist	
		break
			 
