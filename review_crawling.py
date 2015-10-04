__author__ = 'xuzhuqing'
import urllib2
import csv

with open("app_id_list.txt", "r") as csv_file:
    app_list = csv.reader(csv_file, delimiter='\n')
    app_ids = []
    for line in app_list:
        app_ids.append(line[0])

# response = urllib2.urlopen("https://itunes.apple.com/us/rss/customerreviews/id=490217893/sortBy=mostRecent/json")
# review = response.read()
# with open("review_for_one.json", "a") as f:
#     f.write(review)

i = 0
for item in app_ids:
    response = urllib2.urlopen("https://itunes.apple.com/us/rss/customerreviews/id=%s/sortBy=mostRecent/json" % item)
    review = response.read()

    with open("reviewPopularEducation.json", "a") as f:
        f.write(review)

    print "writing in app %s." % item
    i += 1
    l = 241 - i
    print "%s finished. %s left." % (i, l)