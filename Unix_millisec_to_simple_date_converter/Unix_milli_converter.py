#!/usr/bin/env python3

##  Simple program to convert UNIX time (the time in milliseconds since the UNIX epoch (January 1, 1970 00:00:00 UTC)) to UTC datetime, and simplyfy to UTC date.
import datetime

# Take UNIX time as string (default) input, and convert to integer.
unix_time = int(input("Enter the UNIX time in milliseconds: "))

# Convert the unix time from milliseconds to seconds, also removing the fractional seconds by using floor division (as a fraction of .000 is ignored, thus causes an error as the fractional time is missing).
current_date = datetime.datetime.fromtimestamp(unix_time//1000)

# Convert date-time format of current_date (Y-m-d H-M-S) to the new, simple format (Y-m-d)
simple_date = str(datetime.datetime.strptime(str(current_date), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"))

print(simple_date)