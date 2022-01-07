from bs4 import BeautifulSoup
import time 
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
time.sleep(10)
def scrape():
    headers=["name","Distance","Mass","Radius"]
    solar_data=[]
    for i in range(0,489):
        soup = BeautifulSoup("html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index==0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            solar_data.append(temp_list)
scrape()