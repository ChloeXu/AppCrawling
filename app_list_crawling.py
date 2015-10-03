__author__ = 'xuzhuqing'

import re
import urllib2

app_info = "https://itunes.apple.com/lookup?id=490217893"

response = urllib2.urlopen("https://itunes.apple.com/us/genre/ios-education/id6017?mt=8")

url_html = response.read()


app_id = []

matchObj = re.compile(r'(?<=id)\d{9}')

app_id = matchObj.findall(url_html)

print type(app_id)
print len(app_id)

id_list = []
for item in app_id:
    with open("app_id_list.txt","a") as f:
        f.write(str(item)+'\n')
