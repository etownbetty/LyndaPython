#
# Example file for formatting time and date output
#

from datetime import datetime

def main():

  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now() # get the current date and time

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  #print now.strftime("%y") # full year with century
  #print now.strftime("%A, %d %B, %Y") # abbreviated day, num, full month, abbreviated year

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  #print now.strftime("%c")
  #print now.strftime("%x")
  #print now.strftime("%X")

  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print now.strftime("%I:%M:%S %p") # 12-Hour:Minute:Second:AM
  print now.strftime("%H:%M") # 24-Hour:Minute


if __name__ == "__main__":
  main();
