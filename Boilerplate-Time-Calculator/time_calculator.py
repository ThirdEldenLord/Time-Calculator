def add_time(start, duration, weekday = None):
  start_time, start_period = start.split(" ")
  start_time_hour, start_time_minutes = start_time.split(":")
  duration_hour, duration_minutes = duration.split(":")

  if start_period == "PM" and int(start_time_hour) == 12:
    start_time_hour24 = 12
  elif start_period == "PM":
    start_time_hour24 = int(start_time_hour) + 12
  elif start_period == "AM" and int(start_time_hour) == 12:
    start_time_hour24 = 0    
  else:
    start_time_hour24 = start_time_hour  

  new_time_hour24 = int(start_time_hour24) + int(duration_hour)
  new_time_minutes = int(start_time_minutes) + int(duration_minutes) 
  if new_time_minutes >= 60:
    new_time_hour24 = int(new_time_hour24) + int(new_time_minutes) // 60
    new_time_minutes = int(new_time_minutes) - 60
  new_day = ""
  time_hour24 = new_time_hour24

  if new_time_hour24 >= 24 and new_time_hour24 < 48:
    new_day = "(next day)"
    new_time_hour24 = new_time_hour24 - 24
  elif new_time_hour24 >= 48:
    new_day = "(" + str(int(new_time_hour24) // 24) +  " days later)" 
    new_time_hour24 = new_time_hour24 % 24

  if new_time_hour24 <= 11:
    new_period = "AM"
  else:
    new_period = "PM"  

  if new_time_hour24 > 12:
    new_time_hour = int(new_time_hour24) - 12
  elif new_time_hour24 == 0:
    new_time_hour = 12  
  else:
    new_time_hour = new_time_hour24 

  if new_time_minutes <= 9:
    new_time_minutes = "0" + str(new_time_minutes)

  if new_day == "":
    new_time = str(new_time_hour) + ":" + str(new_time_minutes) + " " +\
   str(new_period)  
  else:
    new_time = str(new_time_hour) + ":" + str(new_time_minutes) + " " +\
   str(new_period) + " " + str(new_day)

  
  if weekday == None:
    return new_time
  else:
    days_dict = {"Sunday":1, "Monday":2, "Tuesday":3, "Wednesday":4, 
                 "Thursday":5, "Friday":6, "Saturday":7}
    
    day = days_dict.get(weekday.capitalize())
      
    if new_day == "(next day)":
      day = day + 1
    elif new_day == "(" + str(int(time_hour24) // 24) +  " days later)":
      day = day + int(time_hour24) // 24
    
    if day > 7:
      day = day % 7  
    
    for key, value in days_dict.items():
      if value == day:
        nameday = key
    
    if new_day == "":
      new_time = str(new_time_hour) + ":" + str(new_time_minutes) + " " +\
     new_period + "," + " " + nameday
    else: 
      new_time = str(new_time_hour) + ":" + str(new_time_minutes) + " " +\
     new_period + "," + " " + nameday + " " + new_day       
    return new_time
