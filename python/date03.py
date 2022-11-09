import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5 :
    print("spring")
    
if 6 <= now.month <= 8 :
    print("summer")
    
if 9 <= now.month <= 11 :
    print("autumm")
    
if 12 <= now.month <= 2 :
    print("winter")