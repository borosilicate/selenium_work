import subprocess
import time
#image_auto.py  linkedin_swap.py
subprocess.run(["python", "/home/pi/scripts/image_auto.py"])
subprocess.run(["python", "/home/pi/scripts/linkedin_swap.py"])

#If you wanted it on a loop you could use this I chose to
#uses a systemctl timer 
#time.wait(60*60*6)

