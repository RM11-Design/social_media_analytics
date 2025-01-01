import time
import csv
import matplotlib.pyplot as plt 
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\geckodriver.exe")

# Create the webdriver object using the service
driver = webdriver.Firefox(service=service)

website = input("Enter the URL of Youtube account: ")
driver.get(website)
print("Processing...")

time.sleep(3)

cookie_button = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span')
cookie_button.click()

time.sleep(6)

name = driver.find_element(By.XPATH, '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-dynamic-text-view-model/h1/span')
the_title = name.text
print("Youtuber:",name.text)

# Retrieve the number of followers
no_of_subs = driver.find_element(By.XPATH, '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
subs_count = no_of_subs.text
print("Number of Subscribers:",subs_count)

time.sleep(4)

videos_button = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]/div[1]')
videos_button.click()

time.sleep(4)

video_titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# print(video_titles[0].text)

views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')

# Len has been added to determine the number of videos. 
# Without it, the loop wouldn't know how many items to iterate.

time.sleep(4)

# Get video with the highest number of views

max_views = 0
max_views_title = ""

for i in range(len(video_titles)):
    # Clean the view count text
    view_text = views[i].text.strip().strip("views")
    
    # Convert "K" and "M" into numeric values
    if "K" in view_text:
        view_count = float(view_text.replace("K", "")) * 1000
    elif "M" in view_text:
        view_count = float(view_text.replace("M", "")) * 1000000
    else:
        view_count = int(view_text)  # Handles plain numbers without "K" or "M"

    # Print video title and views
    print(f"Video: {video_titles[i].text} | Views: {int(view_count)}")

    # Update max views
    if view_count > max_views:
        max_views = view_count
        max_views_title = video_titles[i].text

# Output the result
print(f"Video with the highest number of views: {max_views_title} | Views: {int(max_views)}")


time.sleep(4)

# Save results to a csv file

with open(f"{name.text}.csv","w",newline="",encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(["VIDEO_NUMBER","VIDEO","VIEWS"])

    for i in range(len(video_titles)):
        view_text = views[i].text.strip("views")
        if "K" in view_text:
            view_count = float(view_text.replace("K", "")) * 1000
        elif "M" in view_text:
            view_count = float(view_text.replace("M", "")) * 1000000
        else:
            view_count = int(view_text)  # Handles plain numbers without "K" or "M"
            write.writerow([i + 1,video_titles[i].text,view_count])

# Plot graph based on the results

x = [] 
y = [] 

with open(f'{name.text}.csv','r',encoding="utf-8") as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',')
    next(plots) 
                
    for row in plots: 
        x.append(row[0])
        y.append(int(row[2]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Views") 
plt.xlabel('Video Number') 
plt.ylabel('Views') 
plt.title('Views for each video comparsion') 
plt.legend() 
plt.show() 
           
driver.quit()
