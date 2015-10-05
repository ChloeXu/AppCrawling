__author__ = 'xuzhuqing'

import re
import urllib2


response = urllib2.urlopen("http://www.apple.com/itunes/charts/free-apps/")

url_html = response.read()


app_id = []

matchObj = re.compile(r'(?<=id)\d{9}')

app_id = matchObj.findall(url_html)


app_list = []
for item in app_id:
    if item in app_list:
        pass
    else:
        app_list.append(item)

for item in app_list:
    with open("free_list.txt", "a") as f:
        f.write(str(item)+'\n')

print len(app_list)
print 'Done!'