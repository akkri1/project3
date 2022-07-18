# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:35:17 2021

@author: HP
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

with open('Bank_information.csv', mode='w') as csv_file:
   fieldnames = ['Bank/finance company name', 'review/trustscore', 'service type', 'Address']
   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
   writer.writeheader()

#creating an empty list to store values
bank_name = []
review_trustscore = []
servicetype = []
address = []

#Defining the opencodezscraping function
def scraping(webpage):
    #next_page = webpage + str(page_number)
    page = requests.get(webpage)
    soup = BeautifulSoup(page.content,"html.parser")
    result_by_id = soup.find(id="__next")
    result_by_class = result_by_id.find(class_="styles_categoryBusinessListWrapper__2H2X5")
    result_by_class_new = result_by_class.findAll(class_="styles_businessUnitCard__contentContainer__12iZd")
    for i in result_by_class_new:
        Bank_name = i.find(class_="styles_businessTitle__1IANo")
        review = i.find(class_="styles_textRating__19_fv")
        service_type = i.find(class_="styles_categories__c4nU-")
        Address = i.find(class_="styles_location__3JATO")
    #Avoiding attribute error
        if None in (Bank_name,review,service_type,Address):
            continue
        bank_name.append(Bank_name.text)
        review_trustscore.append(review.text)
        servicetype.append(service_type.text)
        address.append(Address.text)
    
    #Generating the next page url
    '''if page_number < 15:
        
        page_number = page_number + 1
        scraping(webpage, page_number)'''
    
scraping("https://www.trustpilot.com/categories/bank")  
#print(bank_name)
#print()
#print(review_trustscore)
#print()
#print(servicetype)
#print()
#print(address)

#creating the data frame and populating its data into the csv file
data = { 'bank_name':bank_name ,'Review':review_trustscore, 'service_type':servicetype, 'Address':address}
#print(data)
#print()
df = pd.DataFrame(data, columns = ['bank_name','Review','service_type','Address'])
#print(df)
#df.to_csv(r'F:\Pentagon\practice\web scrapping/Bank_information.csv')
