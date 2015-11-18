__author__ = 'xuzhuqing'
import urllib2
import csv

with open("pilot_app_list_apple.txt", "r") as csv_file:
    app_list = csv.reader(csv_file, delimiter='\n')
    app_ids = []
    for line in app_list:
        app_ids.append(line[0])

i = 0
for item in app_ids:
    headers = {'User-Agent': 'Mozilla/5.0'}
    print "https://itunes.apple.com/lookup?id=%s" % item
    req = urllib2.Request("https://itunes.apple.com/lookup?id=%s" % item, None, headers)
    response = urllib2.urlopen(req)

    meta_data = response.read()

    with open("pilot_meta_apple.txt", "a") as f:
        f.write(meta_data)
    print "writing in app %s." % item
    i += 1
    l = 241 - i
    print "%s finished. %s left." % (i, l)
