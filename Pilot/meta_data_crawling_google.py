__author__ = 'xuzhuqing'

import re
import csv
import urllib2
from bs4 import BeautifulSoup

with open("pilot_app_list_google.txt", "r") as csv_file:
    app_list = csv.reader(csv_file, delimiter='\n')
    app_ids = []
    for line in app_list:
        app_ids.append(line[0])

def get_meta_data(app_id):
    target_url = "https://play.google.com/store/apps/details?id=%s" % app_id
    response = urllib2.urlopen(target_url)

    soup = BeautifulSoup(response)
    # get description
    html_description = str(soup.find_all(itemprop="description"))
    description = remove_tags(html_description)

    html_meta = str(soup.find_all(class_="meta-info")).decode(encoding='utf-8')
    meta = remove_tags(html_meta)
    print meta
    return {"app": app_id,
            "meta_data": meta,
            "description": description}

def remove_tags(text):
    tag_re = re.compile(r'<[^>]+>')
    return tag_re.sub('', text)




with open("pilot_meta_google.txt", "a") as csvfile:
    for app in app_ids:
        result = get_meta_data(app)
        csvfile.write(str(result) + '\n')

