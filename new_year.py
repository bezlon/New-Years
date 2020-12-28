from datetime import datetime
from os import system

while True:
  current_time = str(datetime.today())
  year = current_time[0:4]
  
  if year == "2021":
    system("shutdown") # Go spend some time with your family bruh