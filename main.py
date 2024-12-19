import time
from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Users\\tmrom\\OneDrive\\Desktop\\Python\\geckodriver.exe")

# Create the webdriver object using the service
driver = webdriver.Firefox(service=service)

# Navigate to the website
website = "https://www.tiktok.com/@uccbangladeshsociety"
driver.get(website)

time.sleep(5)

likes_element = driver.find_element(By.CSS_SELECTOR, 'strong[data-e2e="likes-count"]')

# Extract the text content
likes_count = likes_element.text

print("Likes count:", likes_count)

# This clicks the cookie button of the website automatically. It finds the element of the button. 
# cookie_button = driver.find_element(By.CLASS_NAME, '_a9-- _ap36 _a9_1')
# cookie_button.click()




# driver.quit()

