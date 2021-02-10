from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)


def scrape():
    header = ["v", "proper_name", "bayer_designation", "ly",
              "spectral_class", "mass", "radius", "luminosity"]
    stars_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
        th_tags = soup.find_all("th", attrs={"class", "headerSort"})
        temp_list = []
        for index, th_tag in enumerate(th_tags):
            if index == 0:
                temp_list.append(th_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(th_tag.contents[0])
                except:
                    temp_list.append("")
        stars_data.append(temp_list)
    with open("I_Scrapped_Data_From_Web.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerow(stars_data)


scrape()
