from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from help_functions.api_requests import post_request, refactoring_text
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import time
import re



display = Display(visible=0, size=(800, 800))
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
    "--disable-user-data-dir"
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    # '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get("https://www.ndtv.com/science")
print("open page")
time.sleep(3)
list_href_news = driver.find_elements(By.XPATH, '//a[@class="NwsLstPg_ttl-lnk"]')

href_list = []
for link in list_href_news:
    href_list.append(link.get_attribute("href"))

counter = 0
for href in href_list:
    try:
        print("open article")
        time.sleep(3)
        driver.get(href)
        title = driver.find_element(By.XPATH,'//h1[contains(@class, "sp-ttl")]')
        print(f"Title {title}")

        content_div = driver.find_element(By.XPATH,
                                      '//div[@id="ignorediv"]')

        list_of_news = content_div.find_elements(By.TAG_NAME, "p")

        content = ""
        for el in range(len(list_of_news)):
            content += list_of_news[el].text
            content += " "

        print(f"Content {content}")

        try:
            image_url = driver.find_element(By.XPATH,'//img[@id="story_image_main"]')
        except:
            image_url = \
                "https://s.france24.com/media/display/e6279b3c-db08-11ee-b7f5-005056bf30b7/w:1280/p:16x9/news_en_1920x1080.jpg"

        category = "science-news"

        if not content == False:
            data = {
                "category": category,
                "title": title.text,
                "image_url": image_url.get_attribute("src"),
                "content": content
            }
            print(title)
            print(image_url)
            print(content)
            print("________________________________")

            post_request(data)
    except:
        print("issue")


print("counter")
print(counter)

driver.close()
