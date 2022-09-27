import pandas as pd
from bs4 import BeautifulSoup

def get_input(container):
    options = container.find_all("option")
    input_option = []
    for opt in options:
        input_option.append(opt.next)
    return input_option

def get_dates(content):
    prop_container = content.find(id ="searchForm_from_Date_Prj")
    date_output = get_input(prop_container)
    return date_output

def get_prop(content):
    prop_container = content.find(id ="select1")
    prop_output = get_input(prop_container)
    chunks = split_chunks(prop_output)
    return chunks

def split_chunks(projects):
    property_chunks = []
    n = 5
    for i in range(0, len(projects), n):
        chunk = projects[i:i+n]
        property_chunks.append(chunk)
    return property_chunks

def print_dates(dates,input_val):
    if input_val != 0:
        for count, value in enumerate(dates[:input_val]):
            print(count,":", value)


def get_table(content):
    tables = content.find_all('table')
    dfs = pd.read_html(str(tables))
    dfs[1].columns = list(dfs[0].columns)
    table = dfs[1]
    return table


def search_option(input_element, input_dates):
    for option in input_element.find_elements_by_tag_name('option'):
        if option.text == input_dates:
            option.click()
            break

