from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
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
time.sleep(5)

candidate_search = driver.find_element_by_id("_ctl0_LeftMenu_hlnkSearchCandidates") #clicks candidate search and waits 3 seconds
candidate_search.click()
time.sleep(5)

select_election_year = Select(driver.find_element_by_id('_ctl0_Content_lstElectionYear')) #selects election year
select_election_year.select_by_index(5)
time.sleep(5)

select_jurisdiction = Select(driver.find_element_by_id("_ctl0_Content_ddlJurisdiction")) #selects "statewide" jurisdiction
select_jurisdiction.select_by_index(2)
time.sleep(2)

select_office = Select(driver.find_element_by_id("_ctl0_Content_ddlOffice")) #selects "colorado house" office
select_office.select_by_index(5)
time.sleep(2)

search_button = (driver.find_element_by_id("_ctl0_Content_btnSearch")) #clicks the search button
search_button.click()
time.sleep(2)

page_size = Select(driver.find_element_by_id("_ctl0_Content_dgdSearchResults__ctl13_dgdSearchResultsPageSizeDropDown")) #sets page size to 50
page_size.select_by_index(2)
time.sleep(3)

#new_page = (driver.find_element_by_id("_ctl0_Content_dgdSearchResults__ctl53_dgdSearchResultsPageLink3")) #clicks new page
#new_page.click()
#time.sleep(2)

ids = ["_ctl0_Content_dgdSearchResults__ctl2_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl3_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl4_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl5_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl6_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl7_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl8_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl9_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl10_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl11_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl12_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl13_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl14_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl15_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl16_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl17_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl18_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl19_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl20_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl21_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl22_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl23_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl24_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl25_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl26_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl27_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl28_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl29_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl30_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl31_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl32_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl33_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl34_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl35_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl36_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl37_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl38_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl39_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl40_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl41_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl42_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl43_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl44_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl45_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl46_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl47_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl48_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl49_lnkCandidate",
"_ctl0_Content_dgdSearchResults__ctl50_lnkCandidate", "_ctl0_Content_dgdSearchResults__ctl51_lnkCandidate"]


for id in ids:
    try:
        select_id = (driver.find_element_by_id(id))  # selects the candidate
        select_id.click()
        time.sleep(2)
    except:
        pass

    try:
        candidate_name = (driver.find_element_by_id("_ctl0_Content_lblCandName")).text  # finds candidate's first and last name
        time.sleep(2)
    except:
        candidate_name = "None"

    try:
        candidate_mailing_address = (driver.find_element_by_id("_ctl0_Content_lblCandMailAddress1")).text  # finds candidate's mailing address
        time.sleep(2)
    except:
        candidate_mailing_address = "None"

    try:
        candidate_website = (driver.find_element_by_id("_ctl0_Content_lnkCandWeb")).text  # finds candidate's website
        time.sleep(2)
    except:
        candidate_website = "None"

    try:
        candidate_phone = (driver.find_element_by_id("_ctl0_Content_lblCandPhone")).text  # finds candidate's phone number
        time.sleep(2)
    except:
        candidate_phone = "None"

    try:
        candidate_email = (driver.find_element_by_id("_ctl0_Content_lnkCandEmail")).text  # finds candidate's email
        time.sleep(2)
    except:
        candidate_email = "None"

    try:
        candidate_party = (driver.find_element_by_id("_ctl0_Content_lblCandParty")).text  # finds candidate's party
        time.sleep(2)

    except:
        candidate_party = "None"

    try:
        candidate_office = (driver.find_element_by_id("_ctl0_Content_lblCandOffice")).text  # finds candidate's office
        time.sleep(2)
    except:
        candidate_office = "None"

    try:
        candidate_district = (driver.find_element_by_id("_ctl0_Content_lblCandDistrict")).text  # finds candidate's district
        time.sleep(2)
    except:
        candidate_district = "None"

    try:
        candidate_committee_name = (driver.find_element_by_id("_ctl0_Content_lblCommName")).text  # finds candidate's committee name
        time.sleep(2)
    except:
        candidate_committee_name = "None"

    try:
        candidate_committee_mailing = (driver.find_element_by_id("_ctl0_Content_lblCommMailAddress1")).text  # finds candidate's committee mailing address
        time.sleep(2)
    except:
        candidate_committee_mailing = "None"

    try:
        candidate_registered_agent = (driver.find_element_by_id("_ctl0_Content_lblRegisteredAgent")).text  # finds candidate's registered agent
        time.sleep(2)
    except:
        candidate_registered_agent = "None"

    try:
        registered_agent_email = (driver.find_element_by_id("_ctl0_Content_lnkAgentEmail")).text  # finds candidate's registered agent's email
        time.sleep(2)
    except:
        registered_agent_email = "None"

    try:
        expenditures = (driver.find_element_by_id("_ctl0_Content_lblCandidateExpenditures_EC")).text  # finds total expenditures
        time.sleep(2)
    except:
        expenditures = "None"

    try:
        contributions = (driver.find_element_by_id("_ctl0_Content_lblCandidateExpenditures_EC")).text  # finds contributions
        time.sleep(2)
    except:
        contributions = "None"

    try:
        ending_balance = (driver.find_element_by_id("_ctl0_Content_lblEndingBalance_EC")).text  # finds ending balance
        time.sleep(2)
    except:
        ending_balance = "None"

    dic = {'name': {candidate_name}, 'mailing_address': {candidate_mailing_address}, 'website': {candidate_website}, 'phone': {candidate_phone},
           'email': {candidate_email}, 'party': {candidate_party}, 'office': {candidate_office},
           'district': {candidate_district},
           'committee_name': {candidate_committee_name}, 'committee_mailing_address': {candidate_committee_mailing},
           'registered_agent': {candidate_registered_agent}, 'expenditures': {expenditures},
           "contributions": {contributions},
           'ending_balance': {ending_balance}}

    field_names = ['name', 'mailing_address', 'website' 'phone', 'email', 'party', 'office', 'district', 'committee_name',
                   'committee_mailing_address', 'registered_agent',
                   'expenditures', "contributions", 'ending_balance']

    df = pd.DataFrame([dic])
    df.to_csv('colorado_senate_races_1.csv', mode='a', header=False)

    driver.back()
    driver.refresh()

    ActionChains(driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

#driver.quit()



