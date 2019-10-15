
#Import all your libraries

#Selenium and BeautifulSoup let us access the web and navigate a webpage
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


#Time lets us sleep allowing webpages to load better and not bog down LinkedIns site with too many automated requests
import time


#The following libraries are what we use to save the data and export it as a csv for easy consumption in a program like Excel
import pandas as pd
from itertools import zip_longest
import itertools
import operator
import csv


#Set your webdriver. Chromedriver opens up a chrome web browser. Geckodriver opens up a firefox browser and runs the program there.
#Be sure to install either driver you want to use and have it installed in the correct location as written below.
#driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver.exe')
driver = webdriver.Firefox(executable_path='C:\Windows\geckodriver.exe')


#Opens up a browser and pulls up the webpage for the NRF 2020 show.
base_url = "http://nrfbigshow.nrf.com/"

#A small buffer to ensure page loads properly.
time.sleep(5)

#Initialize our lists. You can see the things we will be collecting are booth number, booth id, company website, 
#address, phone number, as well a contact person's name who works at that company.
booth_num_list = []
booth_id_list = []
comp_id_list = []
website_list = []
contact_first_name_list = []
contact_last_name_list = []
address_1_list = []
address_2_list = []
city_list = []
state_list = []
country_list = []
zip_code_list = []
phone_list = []
email_list = []
exhibiting_as_list = []

#This number is the number of booths you want to search for in this program. Actually for the NRF show the booth numbers go up to above 6,000 but
#the number below is 300 just as an example.
num-booths = 300

#Here we loop through the 300 URLs we want. This will find us 300 pages of companies that are attending the trade show as well as their company and contact information
for i in range(num-booths):
    driver.get(base_url+str(i+1))

    #Find the elements we want on each web page by their xpaths
    booth_num = driver.find_elements_by_xpath("""//*[@id="main-content-header"]/h1""")
    booth_id = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[3]/div[2]/div""")
    comp_id = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[4]/div[2]/div""")
    website = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[6]/div[2]/div/a""")
    contact_first_name = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[8]/div[2]/div""")
    contact_last_name = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[9]/div[2]/div""")
    address_1 = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[11]/div[2]/div""")
    address_2 = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[12]/div[2]/div""")
    city = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[13]/div[2]/div""")
    state = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[14]/div[2]/div""")
    country = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[15]/div[2]/div""")
    zip_code = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[16]/div[2]/div""")
    phone = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[17]/div[2]/div""")
    email = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[20]/div[2]/div""")
    exhibiting_as = driver.find_elements_by_xpath("""/html/body/div[2]/div[1]/div/div[2]/article/div/div[24]/div[2]/div""")
    
    #print("")
    #print(booth_num[0].text)
    #print("")
    
    #Checks to see if a page has no company listed there (the assigned booth numbers bounce around a lot and aren't all incrementally assigned)
    #If there is no company info on that page then it prints to the console that there is no company and skips to the next URL
    if booth_num[0].text == "Page not found":
        print("Page not found")
    
    #If there is a company found on that page then it tells you it is adding it to the list and adds it to the list.
    else:
        print("Adding to list")
    
    
        for x in booth_num:
            booth_num_list.append(x.text.replace('\n', ' ').replace('\r', ''))

        for x in booth_id:
            booth_id_list.append(x.text.replace('\n', ' ').replace('\r', ''))
            
        for x in comp_id:
            comp_id_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in website:
            website_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in contact_first_name:
            contact_first_name_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in contact_last_name:
            contact_last_name_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in address_1:
            address_1_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in address_2:
            address_2_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in city:
            city_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in state:
            state_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in country:
            country_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in zip_code:
            zip_code_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in phone:
            phone_list.append(x.text.replace('\n', ' ').replace('\r', ''))
        
        for x in email:
            email_list.append(x.text.replace('\n', ' ').replace('\r', ''))
       
        for x in exhibiting_as:
            exhibiting_as_list.append(x.text.replace('\n', ' ').replace('\r', ''))

    print('')
    print("Done with page " + str(i+1))
    print('')
    print("--------------------------------------");  

    
#closes our web page that we opened for this program
driver.close()


#Zips together the three lists of data we created above. Matches the first/second/third of each list with the first/second/third of the other lists.
ziplist = list(itertools.zip_longest(booth_num_list, booth_id_list, comp_id_list, website_list, contact_first_name_list, contact_last_name_list, address_1_list, address_2_list, city_list, state_list, country_list, zip_code_list, phone_list, email_list, exhibiting_as_list))


#Turns that zipped list into a Pandas df
ziplist_df = pd.DataFrame(ziplist)


#Prints first 10 rows of df for basic error checking
print(ziplist_df.head(10))


#Saves df as csv in your current working directory.
ziplist_df.to_csv('list.csv', index = False)
    
   
