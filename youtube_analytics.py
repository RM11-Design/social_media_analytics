import time
import pandas as pd
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

time.sleep(4)

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

driver.execute_script("window.scrollBy(0,4000)")

time.sleep(4)

video_titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# print(video_titles[0].text)

views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')

time.sleep(4)

# Get video with the highest number of views

max_views = 0
max_views_title = ""

# Len has been added to determine the number of videos. 
# Without it, the loop wouldn't know how many items to iterate.

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
    
        write.writerow([i + 1,video_titles[i].text,int(view_count)])

# Plot graph based on the results

x = [] 
y = [] 

df = pd.read_csv('Ron’s gadget Review.csv')
top_5 = df.nlargest(5, 'VIEWS')
# print(top_5)

# Save top 3 to a CSV file
top_5.to_csv(f"top_5 for {name.text}.csv", index=False)

top_5.drop('VIDEO_NUMBER', inplace=True, axis=1) 

top_5.to_csv(f"top_5 for {name.text}.csv", index=False)

# Assign a value to each video.
top_5_numbers = ["1","2","3","4","5"]
top_5['VIDEO_NUMBER'] = top_5_numbers
top_5.to_csv(f"top_5 for {name.text}.csv", index=False)

# Prepare data for plotting for top 3
x = top_5["VIDEO_NUMBER"].tolist()  # Assuming 'VIDEO_NUMBER' is a column
y = top_5["VIEWS"].tolist()

plt.bar(x, y, color = 'g', width = 0.55, label = "Views") 
plt.xlabel('Video Number') 
plt.ylabel('Views') 
plt.title(f'Top 5 Videos for {name.text}') 
plt.legend() 
# plt.show() 

plt.savefig(f'Top 5 videos for {name.text}.png', facecolor='w', bbox_inches="tight",
            pad_inches=0.35, transparent=True)

# Get the average number of views

with open(f'{name.text}.csv','r',encoding="utf-8") as csvfile: 
    read_part = csv.reader(csvfile) 
    next(read_part, None)   

    values = []

    for row in read_part:
         value = float(row[2].replace(",",""))
         values.append(value)
         avg = sum(values) / len(values)
    print(f"Average views: {avg:.0f}")

csvfile.close()
           
driver.quit()
