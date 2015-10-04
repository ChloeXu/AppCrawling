__author__ = 'xuzhuqing'

import re
import time
import urllib2


response = urllib2.urlopen("https://play.google.com/store/apps/top")
url_html = response.read()

app_id = []
matchObj = re.compile(r'(?<= data-docid\=").*?(?=")')
app_ids = matchObj.findall(url_html)

date = time.strftime("%x")
current_time = time.strftime("%X")

# get unique app list
app_list = []
for item in app_ids:
    if item in app_list:
        pass
    else:
        app_list.append(item)

# record time of crawling
with open("general_google_app_list.txt", "a") as f:
    f.write('\n' + '*'*25 + "\n" + "Date Recorded starts at: \n" + str(date) + str(current_time) + "\n" + "\n")


for item in app_list:
    with open("general_google_app_list.txt", "a") as f:
        f.write(item + "\n")

with open("general_google_app_list.txt", "a") as f:
    f.write("\n" + "Date Recorded ends at: \n" + str(date) + str(current_time) + "\n" + '*'*25 + "\n")

# print out status
print 'Done!'
