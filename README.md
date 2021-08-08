# URA-Selenium
Using Selenium to collect URA rental contract

**Requirements**
selenium : pip install selenium

pandas : pip install pandas

You need to install chrome driver to activate selenium: 

Use webdriver.Chrome(ChromeDriverManager().install()) <- installs the correct chrome version

Required to change the path after you have downloaded chrome driver:

chromedriverpath_to_chromedriver = "ur file path"


**files**

function.py -> file which contains all functions

scraper.py -> main file to scrape website

consolidated.csv -> csv file with all data



**Running the program**

when scraper.py is run, the script will request input value:

select a date: 

0 : JUN-2021

1 : MAY-2021

2 : APR-2021

3 : MAR-2021

4 : FEB-2021

5 : JAN-2021

6 : DEC-2020

7 : NOV-2020

8 : OCT-2020

9 : SEP-2020

10 : AUG-2020

...

input interger: 5

Enter an integer for "from date input"

after submission you will be prompt to select a "to date input" -> select a date which is later than your "from date input"

0 : JUN-2021

2 : APR-2021

3 : MAR-2021

4 : FEB-2021

input interger: 0

selected  JAN-2021  to  JUN-2021 <- index 5 and 0 selected


**Clean data**

run Clean_CSV.ipynb to clean data

data will be saved in clean_data.csv

The script will take a while to run. Happy scrapping :)




