line = '1h 45m,360s,25m,30m 120s,2h 60s'
count_minutes = 0
new_line = line.replace(",", " ")
lst = new_line.split(" ")
for m in lst:
    if "h" in m:
        count_minutes += int(m[:-1])*60
    elif "s" in m:
        count_minutes += int(int(m[:-1])/60)
    else:
        count_minutes += int(m[:-1])
        
print(count_minutes)