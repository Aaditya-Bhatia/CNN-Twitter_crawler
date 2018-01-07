'''Author: Aaditya Bhatia
Published Date: 7-01-2018
Version: 1.0
Functionality: This module works as a crawler that looks into the web-page(cnn.com) for the keywords 'trump' or 'Trump'
For Asynchronous calls, selenium has been used. This opens a browser window which can not be disabled as per the chrome development team.
'''

#   Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import json

def loadDriver(baseUrl):
    #   Setting up chrome settings for Selenium
    chrome_options = Options()
    chrome_options.add_argument('--dns-prefetch-disable')
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.add_experimental_option("prefs",prefs)
    service_log_path = "./chromedriver.log"
    service_args = ['--verbose']

    #   Driver location needs to be updated for different systems
    driver = webdriver.Chrome('/var/chromedriver/chromedriver', chrome_options=chrome_options, service_args=service_args, service_log_path=service_log_path)

    #   Loading the web-page and waiting for the entire page to load
    driver.get(baseUrl)
    obj = WebDriverWait(driver, 50)
    obj.until(EC.presence_of_element_located((By.XPATH, "//div[@class='pg-no-rail pg-wrapper ']")))
    html_page = driver.page_source
    driver.quit()
    return html_page

def findKeyword(html_page,baseUrl):
    #   HTML parsing
    soup = BeautifulSoup(html_page, 'html.parser')

    label_url_dict = {}

    #   Iterating the parsed data to find keyword in h2 tag
    for art in soup.find_all('a', class_='link-banner'):
        h2 = art.find('h2')
        if 'trump' in h2.get_text() or 'Trump' in h2.get_text():
            label_url_dict[h2.get_text()] = baseUrl + art['href']

    #   Iterating the parsed data to find the keyword in span tags for all h3 tags
    articles = soup.find_all('h3')
    for article in articles:
        spans_all = article.find_all('span')
        for span in spans_all:
            if 'trump' in span.get_text() or 'Trump' in span.get_text():
                label_url_dict[span.get_text()] =  baseUrl + article.find('a')['href']

    #   Debugging the results
    # print ('Found {} keywords in page {}:').format(len(label_url_dict) , baseUrl)
    # print label_url_dict
    return label_url_dict


if __name__ == '__main__':

    baseUrl = "http://edition.cnn.com"

    #   Calling the methods
    html_driver = loadDriver(baseUrl)
    label_url_dict = findKeyword(html_driver)

    #   Saving the results in json
    with open('trump_cnn.txt', 'w') as json_file:
        json.dump(label_url_dict, json_file)