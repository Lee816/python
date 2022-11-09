import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("Time is morning")
    
if now.hour > 12 :
    print("Time is agternoon")