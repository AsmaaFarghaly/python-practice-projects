import time  #for sleep condition
print("welcome to the promodoro timer.")

mins=input("enter time in minutes: ")
mins=int(mins)

total_seconds= mins*60

while total_seconds >0:
    mins=total_seconds//60
    secs=total_seconds%60

    clock= f"{mins:02d}:{secs:02d}"

    print( f"\rtime remaining : {clock}",end="")

    time.sleep(1)

    total_seconds-=1
    
print("\n time's up , take a rest")