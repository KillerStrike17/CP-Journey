timepoints = ["00:00","12:10","10:15","13:15","17:20","18:00","19:45","23:59"]


minutes = []
for _ in timepoints:
    hours = int(_.split(':')[0])
    minute = int(_.split(':')[-1])
    minutes.append(hours*60+minute)

print(minutes)
minutes.sort()
print(minutes)
min_val =99999999
for _ in range(1,len(minutes)):
    diff = minutes[_] - minutes[_-1]
    if diff<min_val:
        min_val = diff
lastDiff = minutes[0] - minutes[_] + 1440
min_val = min(min_val,lastDiff)

print(min_val)