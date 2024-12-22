import time
import csv
from openpyxl import Workbook
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\geckodriver.exe")

# Create the webdriver object using the service
driver = webdriver.Firefox(service=service)

# Navigate to the website
website = input("Enter the URL of TikTok account: ")
# website = "https://www.tiktok.com/@uccbangladeshsociety"
driver.get(website)
print("Processing...")

time.sleep(6)

# A variable i.e. the_title, followers_count etc.. were assigned. If I didn't add this, 
# then the printed values will come out as a string representation of the web element.

# Retrieve the account name.
title = driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/div[2]/div[1]/div/h2')
the_title = title.text
print("Account Name:",title.text)

# Retrieve the number of followers
no_of_followers = driver.find_element(By.CSS_SELECTOR, 'strong[data-e2e="followers-count"]')
followers_count = no_of_followers.text
print("Number of followers:",followers_count)

# Retrieve the number the total number of likes
likes_element = driver.find_element(By.CSS_SELECTOR, 'strong[data-e2e="likes-count"]')
likes_count = likes_element.text
print("Number of likes",likes_count)

time.sleep(3)

views = driver.find_elements(By.CSS_SELECTOR, 'strong[data-e2e="video-views"]')

# Retrieve the number of views for each video
# Each video is assigned a number.

for x, view in enumerate(views, start=1):
    print(f"Video {x} Views:", view.text)

# Save the results to a excel file.

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Account Name"
sheet["A2"] = "Followers"
sheet["A3"] = "Likes"

sheet["B1"] = title.text
sheet["B2"] = followers_count
sheet["B3"] = likes_count



workbook.save(filename="bsoc_tiktok.xlsx")

    


# with open("Bsoc tiktok.csv","w",newline="",encoding="utf-8") as f:
#     write = csv.writer(f)

#     write.writerow(["ACCOUNT","FOLLOWERS","TOTAL-LIKES","VIDEO","VIEWS"])
#     write.writerow([the_title,followers_count,likes_count,"Video",x,view.text])

#     write.writerow(["Video","Views"])
#     write.writerow([view.text])

driver.quit()

