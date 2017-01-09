
############################################
#This program acts as an alarm and plays video or song after time which is given as input.

import webbrowser                                         
import time

break_count = 0
print ("this program started on "+time.ctime())             #ctime stands for current time
while (break_count < 3): 
    time.sleep(60*60)
    webbrowser.open("https://www.youtube.com/watch?v=dSYu8FLVr_Y")
    break_count +=1
