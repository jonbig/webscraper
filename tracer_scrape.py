from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import csv
import pandas as pd

path = ("/Users/jon.biggerstaff/Desktop/pythonProject1/lib/python3.10/site-packages/chromedriver 3")
s = Service(path)
driver = webdriver.Chrome(service=s)

driver.get("https://tracer.sos.colorado.gov/PublicSite/homepage.aspx") #goes to tracer homepage

search = driver.find_element_by_id("_ctl0_LeftMenu_hlnkSearch") #clicks "search" and waits 2 seconds"
search.click()
time.sleep(3)

candidate_search = driver.find_element_by_id("_ctl0_LeftMenu_hlnkSearchCandidates") #clicks candidate search and waits 3 seconds
candidate_search.click()
time.sleep(3)

select_election_year = Select(driver.find_element_by_id('_ctl0_Content_lstElectionYear')) #selects election year
select_election_year.select_by_index(5)
time.sleep(3)

select_jurisdiction = Select(driver.find_element_by_id("_ctl0_Content_ddlJurisdiction")) #selects "statewide" jurisdiction
select_jurisdiction.select_by_index(2)
time.sleep(2)

select_office = Select(driver.find_element_by_id("_ctl0_Content_ddlOffice")) #selects "colorado house" office
select_office.select_by_index(3)
time.sleep(2)

search_button = (driver.find_element_by_id("_ctl0_Content_btnSearch")) #clicks the search button
search_button.click()
time.sleep(2)

page_size = Select(driver.find_element_by_id("_ctl0_Content_dgdSearchResults__ctl13_dgdSearchResultsPageSizeDropDown")) #sets page size to 50
page_size.select_by_index(2)
time.sleep(5)

page_number = (driver.find_element_by_id("_ctl0_Content_dgdSearchResults__ctl53_dgdSearchResultsPageLink1")) #clicks page numbers 2
page_number.click()
time.sleep(4)


select_allen = (driver.find_element_by_id("_ctl0_Content_dgdSearchResults__ctl13_lnkCandidate")) #selects the allen candidate
select_allen.click()
time.sleep(5)

candidate_name = (driver.find_element_by_id("_ctl0_Content_lblCandName")).text #finds candidate's first and last name
time.sleep(2)

candidate_mailing_address = (driver.find_element_by_id("_ctl0_Content_lblCandMailAddress1")).text #finds candidate's mailing address
time.sleep(2)

candidate_phone = (driver.find_element_by_id("_ctl0_Content_lblCandPhone")).text #finds candidate's phone number
time.sleep(2)

candidate_email = (driver.find_element_by_id("_ctl0_Content_lnkCandEmail")).text #finds candidate's email
time.sleep(2)

candidate_party = (driver.find_element_by_id("_ctl0_Content_lblCandParty")).text #finds candidate's party
time.sleep(2)

candidate_office = (driver.find_element_by_id("_ctl0_Content_lblCandOffice")).text #finds candidate's office
time.sleep(2)

candidate_district = (driver.find_element_by_id("_ctl0_Content_lblCandDistrict")).text #finds candidate's district
time.sleep(2)

candidate_committee_name = (driver.find_element_by_id("_ctl0_Content_lblCommName")).text #finds candidate's committee name
time.sleep(2)

candidate_committee_mailing = (driver.find_element_by_id("_ctl0_Content_lblCommMailAddress1")).text #finds candidate's committee mailing address
time.sleep(2)

candidate_registered_agent = (driver.find_element_by_id("_ctl0_Content_lblRegisteredAgent")).text #finds candidate's registered agent
time.sleep(2)

registered_agent_email = (driver.find_element_by_id("_ctl0_Content_lnkAgentEmail")).text #finds candidate's registered agent's email
time.sleep(2)

expenditures = (driver.find_element_by_id("_ctl0_Content_lblCandidateExpenditures_EC")).text #finds total expenditures
time.sleep(2)

contributions = (driver.find_element_by_id("_ctl0_Content_lblCandidateExpenditures_EC")).text #finds contributions
time.sleep(2)

ending_balance = (driver.find_element_by_id("_ctl0_Content_lblEndingBalance_EC")).text #finds ending balance
time.sleep(2)


dic = {'name': {candidate_name}, 'mailing_address': {candidate_mailing_address}, 'phone': {candidate_phone},
       'email': {candidate_email}, 'party': {candidate_party}, 'office': {candidate_office}, 'district': {candidate_district},
       'committee_name': {candidate_committee_name}, 'committee_mailing_address': {candidate_committee_mailing},
       'registered_agent': {candidate_registered_agent}, 'expenditures': {expenditures}, "contributions": {contributions},
       'ending_balance': {ending_balance}}

field_names = ['name', 'mailing_address', 'phone', 'email', 'party', 'office', 'district', 'committee_name', 'committee_mailing_address', 'registered_agent',
'expenditures', "contributions", 'ending_balance']


df = pd.DataFrame([dic])
df.to_csv('test_17.csv', mode='a', header=False)


driver.quit()
