day = int(input("please enter the day: "))
month = int(input("please enter the month: "))

if 3<=month<6 or (month==3 and day>=21) or (month==6 and day<21) :
  season = "spring"
elif 6<=month<9 or (month==6 and day>=21) or (month==9 and day<22) :
  season = "summer"
elif 9<=month<12 or (month==9 and day>=22) or (month==12 and day<21) :
  season = "fall"
else :
  season = "winter"

print(season)       