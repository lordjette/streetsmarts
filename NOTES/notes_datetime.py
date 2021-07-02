import datetime
import time

import datetime as jdt, time as j
print ('To Local Time:', jdt.datetime.fromtimestamp(j.time()).strftime('%Y-%m-%d %I:%M:%S')) #jett

timestamp = time.time()
#timestamp = datetime.datetime.now().strftime("%s")

print ("timestamp: ", timestamp)

print ("To Local Time: ", time.ctime(timestamp))

print ("To Local Time: ", time.ctime(time.time()) ) #jett

print ("To Local Time: ", datetime.datetime.fromtimestamp(timestamp))
print ("To Local Time: ", datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

print ("To Local Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %I:%M:%S')) #jett

#python 3 
print ("To Local Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %I:%M:%S.%f')) #jett

print ("To UTC Time: ", datetime.datetime.utcfromtimestamp(timestamp))
print ("To UTC Time: ", datetime.datetime.utcfromtimestamp(time.time())) #jett

import tzlocal # pip install tzlocal
#cat /etc/timezone
local_timezone = tzlocal.get_localzone()
print ("To Local Timezone: ", datetime.datetime.fromtimestamp(timestamp, local_timezone))

#JETTE

import datetime, pytz

local_manila = datetime.datetime.strftime(pytz.utc.localize(datetime.datetime.utcnow()) \
        .astimezone(pytz.timezone("Asia/Manila")), '%Y-%m-%d %I:%M:%S.%f')