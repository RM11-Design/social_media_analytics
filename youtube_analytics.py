import time
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\geckodriver.exe")

# Create the webdriver object using the service
driver = webdriver.Firefox(service=service)

website = input("Enter the URL of Youtube account: ")
driver.get(website)
print("Processing...")

cookie_button = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span')
cookie_button.click()

time.sleep(6)

title = driver.find_element(By.XPATH, '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-dynamic-text-view-model/h1/span')
the_title = title.text
print("Account Name:",title.text)

# Retrieve the number of followers
no_of_subs = driver.find_element(By.XPATH, '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
subs_count = no_of_subs.text
print("Number of Subscribers:",subs_count)
