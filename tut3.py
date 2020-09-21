import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN)
GPIO.setup(3,GPIO.OUT, initial=GPIO.LOW)

def main():
	global flag
	flag = 0
	print(GPIO.input(5))
	time.sleep(20)
def my_callback(channel):
	global flag
	if flag == 1:
		GPIO.output(3,False)
		flag = 0
	else:
		GPIO.output(3,True)
		flag = 1

GPIO.add_event_detect(5,GPIO.RISING,callback=my_callback , bouncetime=200)
if __name__ == "__main__":
	main()

