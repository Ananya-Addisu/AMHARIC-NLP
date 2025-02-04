# from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
import csv



def preprocess(texts):
    num_text = len(texts)
    full_text = [texts[i].text.encode('utf-8')+'\n' for i in range(num_text)]
    full_text = ' '.join(full_text)
    full_text = full_text.strip()
    full_text = full_text.replace('\n',' ')
    return full_text



MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 100

page_link = 'https://ethiopiazare.com/amharic/history/history/4379-abuna-theophilos-by-aklilu-habtewold'


with open('results.csv','w') as f:
    f.write('Text')


driver  = webdriver.Firefox()

for i in range(1,MAX_PAGE_NUM+1):
    print('Going Through:',page_link)
    page_num = (MAX_PAGE_DIG)

    driver.get(page_link)
    texts = driver.find_elements_by_tag_name('p')
    

    with open('results.csv', 'a') as f:
        f.write(preprocess(texts)+',')
        break
    break



    links = driver.find_elements_by_class_name('next')
    page_link = links[0].find_element_by_tag_name('a').get_attribute('href')


driver.close()