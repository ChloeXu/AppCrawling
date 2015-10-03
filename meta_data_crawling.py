__author__ = 'xuzhuqing'
import urllib2
import csv

with open("app_id_list.txt", "r") as csv_file:
    app_list = csv.reader(csv_file, delimiter='\n')
    app_ids = []
    for line in app_list:
        app_ids.append(line[0])

i = 0
for item in app_ids:
    response = urllib2.urlopen("https://itunes.apple.com/lookup?id=%s" %item)

    meta_data = response.read()

    with open("metaDataPopularEducation.json", "a") as f:
        f.write(meta_data)
    print "writing in app %s." % item
    i += 1
    l = 241 - i
    print "%s finished. %s left." % (i, l)