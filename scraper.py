
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import function



def main():
    def input_to_date(input_dates):
        element = driver.find_element_by_id("searchForm_to_Date_Prj")
        function.search_option(element,input_dates)

    def input_from_date(input_dates):
        element = driver.find_element_by_id("searchForm_from_Date_Prj")
        function.search_option(element,input_dates)

    def get_range():
        print("select a date: \n")
        dates = function.get_dates(soup)
        length = len(dates)
        function.print_dates(dates,length)
        from_input = int(input("input interger: "))
        from_date = dates[from_input]
        function.print_dates(dates,from_input)
        to_input = int(input("input interger: "))
        while (to_input > from_input):
            print("choose within range")
            to_input = int(input("input interger: "))
        to_date = dates[to_input]
        print("selected ",from_date," to ", to_date)
        return [from_date, to_date]

    def search_property(property_chunk):
        search_element = driver.find_element_by_id("projectContainerBox")
        for prop in property_chunk:
            for option in search_element.find_elements_by_link_text(prop):
                option.click()

    path_to_chromedriver = "C:/Users/neo qi xiang/Desktop/modular/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    url = "https://www.ura.gov.sg/realEstateIIWeb/resiRental/search.action"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    range_date = get_range()
    prop_iteration =  function.get_prop(soup)

    for i in prop_iteration:
        input_from_date(range_date[0])
        input_to_date(range_date[1])
        search_property(i)
        search_result = driver.find_element_by_id("searchForm_0")
        search_result.click()
        soup_new = BeautifulSoup(driver.page_source, 'lxml')    
        scrape_data = function.get_table(soup_new)
        try:
            len(main)
            main = main.append(scrape_data)
        except:
            main = scrape_data
            
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchForm_0")))
        input_from_date(range_date[0])
        input_to_date(range_date[1])

    main.to_csv("consolidated.csv", index = False)
    
if __name__ == "__main__":
    main()
else:
    print("nope")