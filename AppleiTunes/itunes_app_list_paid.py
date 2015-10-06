__author__ = 'xuzhuqing'

import re
import time
import urllib2


response = urllib2.urlopen("http://www.apple.com/itunes/charts/paid-apps/")

url_html = response.read()

date = time.strftime("%x")
current_time = time.strftime("%X")
app_id = []

matchObj = re.compile(r'(?<=id)\d{9}')

app_id = matchObj.findall(url_html)

with open("paid_list.txt", "a") as f:
    f.write("\n" + "Date Recorded starts at: \n" + str(date) + ' ' + str(current_time) + "\n" + '*'*25 + "\n")



app_list = []
for item in app_id:
    if item in app_list:
        pass
    else:
        app_list.append(item)

for item in app_list:
    with open("paid_list.txt", "a") as f:
        f.write(str(item)+'\n')

with open("paid_list.txt", "a") as f:
    f.write("\n" + "Date Recorded ends at: \n" + str(date) + ' ' + str(current_time) + "\n" + '*'*25 + "\n")


print len(app_list)
print 'Done!'