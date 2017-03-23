import time

current_time = time.time()
total_seconds = int(current_time)
current_second = total_seconds % 60
total_minutes = total_seconds // 60
current_minute = total_minutes % 60
total_hours = total_minutes // 60
current_hour = total_hours % 24

print("Current time w.r.t machine (in milliseconds) is:", current_time)
print("Current time in London is", current_hour, ":", current_minute, ":", current_second, "GMT" )

ist_minutes = total_minutes + 330
ist_current_minute = ist_minutes % 60
ist_hours = ist_minutes // 60
ist_current_hour = ist_hours % 24

print("Current time in India is:", ist_current_hour, ":", ist_current_minute, ":", current_second, "IST")


