from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    the_video = browser.new_page()
    chosen_video = input("Throw in URL of video: ")
    the_video.goto(chosen_video)

    # time.sleep(5)
    
    the_video.locator("text='Reject all'").click()

    time.sleep(3)

    for i in range(10): 
        the_video.evaluate("window.scrollBy(0, 600)")  

    time.sleep(3)

    comments = the_video.locator('xpath=//*[@id="content-text"]/span').all_text_contents()

    for comment in enumerate(comments):
        print(comment)
    


    # the_title = the_video.get_by_text("style-scope ytd-rich-grid-media")
    # print(the_title)
    
    # for title in the_titles:
    #     print(title)


    the_video.pause()