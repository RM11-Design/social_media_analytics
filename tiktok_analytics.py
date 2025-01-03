import time
import csv
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


time.sleep(4)

with open(f"{title.text}.csv","w",newline="",encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(["VIDEO_NUMBER","VIEWS"])

    for i, view in enumerate(views, start=1):
        write.writerow([f"Video {i} Views:",view.text])

f.close()

# Plot graph based on the results

x = [] 
y = [] 

with open(f'{title.text}.csv','r',encoding="utf-8") as csvfile: 
    
    plots = csv.reader(csvfile, delimiter = ',')
    next(plots) 
                
    for row in plots: 
        x.append(row[0])
        y.append(int(row[1]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Views") 
plt.xlabel('Video Number') 
plt.ylabel('Views') 
plt.title('Views for each video comparsion') 
plt.legend() 
plt.show() 

csvfile.close()

# Get the average number of views

with open(f'{title.text}.csv','r',encoding="utf-8") as csvfile: 
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

