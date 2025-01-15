import time
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\geckodriver.exe")

# Create the webdriver object using the service
driver = webdriver.Firefox(service=service)


# Navigate to the website
website = input("Enter the URL of TikTok account: ")
time.sleep(6)

driver.get(website)
print("Processing...")

time.sleep(6)

# A variable i.e. the_title, followers_count etc.. were assigned. If I didn't add this, 
# then the printed values will come out as a string representation of the web element.

# Retrieve the account name.
title = driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/div[2]/div[1]/div/h2')
the_title = title.text
print("Account Name:",title.text)

# Automatic scroll
driver.execute_script("window.scrollBy(0,6000)")

time.sleep(3)

# decline_cookie_button = driver.find_element(By.XPATH, '/div/div[2]/button[1]')
# decline_cookie_button.click()

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

for x, view_element in enumerate(views):
    view_text = view_element.text
    if "K" in view_text:
        view_count = float(view_text.replace("K", "")) * 1000
    elif "M" in view_text:
        view_count = float(view_text.replace("M", "")) * 1000000
    else:
        view_count = int(view_text)  # Handles plain numbers without "K" or "M"
    print(f"Video {x + 1} Views:", view_count)

time.sleep(4)

folder_path = f"C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\social_media_analytics\\Reports for {title.text}"
 
# create the folder if it doesn't exist 
if not os.path.exists(folder_path): 
    os.makedirs(folder_path) 
 
# define the file name and path 
file_name = f"{title.text}.csv"
file_path = os.path.join(folder_path, file_name)

with open(file_path,"w",newline="",encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(["VIDEO_NUMBER","VIEWS"])

    for x, view_element in enumerate(views):
        view_text = view_element.text
        if "K" in view_text:
            view_count = float(view_text.replace("K", "")) * 1000
        elif "M" in view_text:
            view_count = float(view_text.replace("M", "")) * 1000000
        else:
            view_count = int(view_text)  # Handles plain numbers without "K" or "M"
        
        write.writerow([f"Video {x + 1} Views:", view_count])

f.close()

# Plot graph based on the the top 5 videos

x = [] 
y = [] 

df = pd.read_csv(file_path)
top_5 = df.nlargest(5, 'VIEWS')
# print(top_5)

# Save top 3 to a CSV file
top_5.to_csv(f"C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\social_media_analytics\\Reports for {title.text}\\top_5 for {title.text}.csv", index=False)

top_5.drop('VIDEO_NUMBER', inplace=True, axis=1) 

top_5.to_csv(f"C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\social_media_analytics\\Reports for {title.text}\\top_5 for {title.text}.csv", index=False)

# Assign a value to each video.
top_5_numbers = ["1","2","3","4","5"]
top_5['VIDEO_NUMBER'] = top_5_numbers
top_5.to_csv(f"C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\social_media_analytics\\Reports for {title.text}\\top_5 for {title.text}.csv", index=False)

# Prepare data for plotting for top 5
x = top_5["VIDEO_NUMBER"].tolist()  # Assuming 'VIDEO_NUMBER' is a column
y = top_5["VIEWS"].tolist()

plt.bar(x, y, color = 'g', width = 0.72, label = "Views") 
plt.xlabel('Video Number') 
plt.ylabel('Views') 
plt.title(f'Top 5 videos for {title.text}') 
plt.legend() 
plt.savefig(f'C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\social_media_analytics\\Reports for {title.text}\\Top 5 videos for {title.text}.png', facecolor='w', bbox_inches="tight",
            pad_inches=0.2, transparent=True)

time.sleep(4)

# Get the average number of views

with open(f'C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\PushingTheBoundaries\\social_media_analytics\\Reports for {title.text}\\{title.text}.csv','r',encoding="utf-8") as csvfile: 
    read_part = csv.reader(csvfile) 
    next(read_part, None)   

    values = []

    for row in read_part:
         value = float(row[1].replace(",",""))
         values.append(value)
         avg = sum(values) / len(values)
    print(f"Average views: {avg:.0f}")

# Find the video with the most of views

max_views = 0
max_video = 0

for x, view in enumerate(views, start=1):
    views_count = int(view.text)
    if views_count > max_views:
        max_views = views_count
        max_video = x

print(f"Video {max_video} has the most views with {max_views} views")
           
driver.quit()

