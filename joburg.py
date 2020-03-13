strAvg_speed= int(input("What was your average speed in km/h? "))
strAllwd_speed= int(input("What was the allowed speed on the road? "))
# declaring variables
if (strAvg_speed<=60):
    print("ok")
elif (strAvg_speed >60):
    demerits=(strAvg_speed-strAllwd_speed)//5
    print(demerits, "demerits points")
if (strAvg_speed>=120):
    print("Time to go to jail!!!")





