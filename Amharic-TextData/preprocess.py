try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import codecs
import os
from tqdm import tqdm


files = os.listdir('news/.')

import csv
with open('tikvahethiopia.csv','w') as f1:
    writer=csv.writer(f1)
    for i in tqdm(files):
        if '.html' in i:
            html=codecs.open("news/"+i, 'r', 'utf-8')
            parsed_html = BeautifulSoup(html)
            for j in parsed_html.findAll("div",{"class":"text"}):
                if len(j.text) > 30:
                    print(len(j.text))
                    writer.writerow([str(j.text)])
    