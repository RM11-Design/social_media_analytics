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

name = driver.find_element(By.XPATH, '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-dynamic-text-view-model/h1/span')
the_title = name.text
print("Account Name:",name.text)

# Retrieve the number of followers
no_of_subs = driver.find_element(By.XPATH, '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
subs_count = no_of_subs.text
print("Number of Subscribers:",subs_count)

time.sleep(4)

videos_button = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]/div[1]')
videos_button.click()

time.sleep(4)

video_titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
print(video_titles[0].text)

views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')

# Retrieve the number of views for each video
# Each video is assigned a number.

# Len has been added to determine the number of videos. 
# Without it, the loop wouldn't know how many items to iterate.
for i in range(len(video_titles)):
    print(f"Video: {video_titles[i].text} | Views: {views[i].text}")

driver.quit()
